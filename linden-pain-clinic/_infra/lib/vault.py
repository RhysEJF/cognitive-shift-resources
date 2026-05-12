"""
Token → real-value vault.

SQLite database with values encrypted via libsodium (XSalsa20-Poly1305) per row.
Lives on customer infrastructure only. The LLM never sees this file.

Schema:
    tokens(
        token       TEXT PRIMARY KEY,   -- e.g., "PERSON_a3f9b2c4d8e1"
        kind        TEXT NOT NULL,      -- "PERSON", "DOB", etc.
        ciphertext  BLOB NOT NULL,      -- nacl SecretBox encrypted real value
        nonce       BLOB NOT NULL,      -- 24-byte nonce, unique per row
        prod_id     TEXT,               -- optional foreign key into prod system
        created_at  TEXT NOT NULL       -- ISO timestamp
    )

Every read is logged via the audit module before returning.
"""

from __future__ import annotations

import secrets
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

import nacl.secret
import nacl.utils

from lib.tokens import KINDS


_SCHEMA = """
CREATE TABLE IF NOT EXISTS tokens (
    token       TEXT PRIMARY KEY,
    kind        TEXT NOT NULL,
    ciphertext  BLOB NOT NULL,
    nonce       BLOB NOT NULL,
    prod_id     TEXT,
    created_at  TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS tokens_kind ON tokens(kind);
CREATE INDEX IF NOT EXISTS tokens_prod_id ON tokens(prod_id);
"""


def load_or_create_encryption_key(key_path: Path) -> bytes:
    """Read the SecretBox key from disk, or create a fresh 32-byte random key if missing."""
    if key_path.exists():
        return key_path.read_bytes()
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
    key_path.write_bytes(key)
    key_path.chmod(0o600)
    return key


class Vault:
    """
    Encrypted token store.

    Usage:
        audit = AuditLog(path_to_log)
        v = Vault(db_path, encryption_key, audit)
        v.put("PERSON_a3f9", "PERSON", "Sarah Müller", prod_id="patient-7421")
        real = v.resolve("PERSON_a3f9", purpose="executor:run_xyz")   # -> "Sarah Müller"  (logged)

    The `audit` parameter is REQUIRED. Constructing a Vault without an audit
    logger bypasses the GDPR Article 30 records-of-processing requirement,
    so the constructor refuses. Every public query on the vault — plaintext
    read, metadata read, iteration — leaves an audit-log entry.
    """

    def __init__(self, db_path: Path, encryption_key: bytes, audit):
        if audit is None:
            raise ValueError(
                "Vault requires an audit logger. Constructing a Vault without "
                "auditing would bypass the GDPR Art. 30 records-of-processing "
                "requirement. Pass an AuditLog (or any object with an "
                "`append(event=..., **fields)` method)."
            )
        if not hasattr(audit, "append"):
            raise TypeError(
                f"audit logger must implement .append(event=..., **fields); "
                f"got {type(audit).__name__}"
            )
        self._db_path = db_path
        self._box = nacl.secret.SecretBox(encryption_key)
        self._audit = audit
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(db_path))
        self._conn.executescript(_SCHEMA)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> "Vault":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    # ------------------------------------------------------------------
    # Writes
    # ------------------------------------------------------------------

    def put(self, token: str, kind: str, real_value: str, prod_id: str | None = None) -> None:
        """
        Insert (or no-op) a token mapping.

        Deterministic tokens mean repeated calls with the same value are
        expected — we simply ignore duplicates rather than re-encrypt with a
        new nonce, so the row stays stable across scrubber runs.
        """
        if kind not in KINDS:
            raise ValueError(f"unknown token kind: {kind!r}")
        existing = self._conn.execute(
            "SELECT 1 FROM tokens WHERE token = ?", (token,)
        ).fetchone()
        if existing:
            return
        nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
        ciphertext = self._box.encrypt(real_value.encode("utf-8"), nonce).ciphertext
        self._conn.execute(
            "INSERT INTO tokens (token, kind, ciphertext, nonce, prod_id, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (token, kind, ciphertext, nonce, prod_id, _now()),
        )
        self._conn.commit()

    # ------------------------------------------------------------------
    # Reads (audited)
    # ------------------------------------------------------------------

    def resolve(self, token: str, *, purpose: str) -> str:
        """
        Look up the real value for a token. EVERY call is audit-logged.

        `purpose` is a free-form string describing why the resolution happened
        (e.g., "executor:update_status:run_abc123"). It lands in the audit log
        and is part of the GDPR Art. 30 records-of-processing story.
        """
        row = self._conn.execute(
            "SELECT kind, ciphertext, nonce FROM tokens WHERE token = ?", (token,)
        ).fetchone()
        if not row:
            self._log("vault.resolve.miss", token=token, purpose=purpose)
            raise KeyError(f"token not in vault: {token}")
        kind, ciphertext, nonce = row
        plaintext = self._box.decrypt(ciphertext, nonce).decode("utf-8")
        self._log("vault.resolve.hit", token=token, kind=kind, purpose=purpose)
        return plaintext

    def resolve_many(self, tokens: list[str], *, purpose: str) -> dict[str, str]:
        """Convenience: resolve many tokens in one go. Each is individually audited."""
        return {t: self.resolve(t, purpose=purpose) for t in tokens}

    def prod_id_for(self, token: str, *, purpose: str) -> str | None:
        """Look up the prod_id linked to a token, if any."""
        row = self._conn.execute(
            "SELECT prod_id FROM tokens WHERE token = ?", (token,)
        ).fetchone()
        if not row:
            self._log("vault.prod_id.miss", token=token, purpose=purpose)
            raise KeyError(f"token not in vault: {token}")
        self._log("vault.prod_id.hit", token=token, purpose=purpose)
        return row[0]

    # ------------------------------------------------------------------
    # Introspection (audited — every query leaves a trace, even
    # metadata-only ones that don't expose plaintext)
    # ------------------------------------------------------------------

    def count(self, *, purpose: str) -> int:
        n = self._conn.execute("SELECT COUNT(*) FROM tokens").fetchone()[0]
        self._log("vault.count", purpose=purpose, result=n)
        return n

    def count_by_kind(self, *, purpose: str) -> dict[str, int]:
        result = dict(
            self._conn.execute(
                "SELECT kind, COUNT(*) FROM tokens GROUP BY kind ORDER BY kind"
            ).fetchall()
        )
        self._log("vault.count_by_kind", purpose=purpose, kinds=sorted(result.keys()))
        return result

    def iter_tokens(self, *, purpose: str) -> Iterator[tuple[str, str, str | None]]:
        """Yield (token, kind, prod_id) — never plaintext."""
        self._log("vault.iter_tokens", purpose=purpose)
        for row in self._conn.execute(
            "SELECT token, kind, prod_id FROM tokens ORDER BY kind, token"
        ):
            yield row

    # ------------------------------------------------------------------
    # Audit hook
    # ------------------------------------------------------------------

    def _log(self, event: str, **fields) -> None:
        # Vault refuses to construct without an audit logger, so this is
        # always non-null at runtime — no guard needed.
        self._audit.append(event=event, **fields)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
