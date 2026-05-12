"""
Tamper-evident audit log.

Append-only JSONL where each entry's `prev_hash` field is the SHA-256 hash of
the previous entry's canonical JSON. Modifying any entry breaks the chain from
that point forward, which a verifier can detect.

This is the simplest cryptographic primitive that gives you "no silent edits":
not a full Merkle tree, not a blockchain, just hash chaining. Good enough to
prove integrity for a GDPR Article 30 records-of-processing log.

Production deployments would write this stream to append-only object storage
(S3 with object lock, GCS retention policy) and periodically anchor the latest
hash externally (e.g., publish to a transparency log) so even the audit-log
owner cannot rewrite history.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


_GENESIS_HASH = "0" * 64  # sentinel for the first entry


class AuditLog:
    """Hash-chained append-only audit log."""

    def __init__(self, path: Path):
        self._path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.touch()

    # ------------------------------------------------------------------
    # Append
    # ------------------------------------------------------------------

    def append(self, *, event: str, **fields: Any) -> str:
        """
        Append an entry. Returns the entry's hash (so callers can pin it).

        Refuses to append if `event` or fields contain reserved keys.
        """
        reserved = {"ts", "prev_hash", "hash", "event"}
        bad = reserved & set(fields)
        if bad:
            raise ValueError(f"audit fields cannot use reserved keys: {sorted(bad)}")
        prev_hash = self._last_hash()
        entry = {
            "ts": _now(),
            "event": event,
            "prev_hash": prev_hash,
            **fields,
        }
        entry["hash"] = _hash_entry(entry)
        line = json.dumps(entry, sort_keys=True, separators=(",", ":")) + "\n"
        with self._path.open("a", encoding="utf-8") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        return entry["hash"]

    # ------------------------------------------------------------------
    # Verify
    # ------------------------------------------------------------------

    def verify(self) -> tuple[bool, str | None, int]:
        """
        Walk the chain. Returns (ok, error_message, entries_verified).

        Stops at the first broken link. `error_message` is None when ok.
        """
        prev_hash = _GENESIS_HASH
        count = 0
        with self._path.open("r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, start=1):
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    entry = json.loads(raw)
                except json.JSONDecodeError as e:
                    return False, f"line {line_no}: invalid JSON ({e})", count
                if entry.get("prev_hash") != prev_hash:
                    return (
                        False,
                        f"line {line_no}: prev_hash mismatch (expected {prev_hash[:12]}…)",
                        count,
                    )
                expected = _hash_entry({k: v for k, v in entry.items() if k != "hash"})
                if entry.get("hash") != expected:
                    return False, f"line {line_no}: entry hash mismatch", count
                prev_hash = entry["hash"]
                count += 1
        return True, None, count

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _last_hash(self) -> str:
        # Tail the file. For an MVP volume this is fine; production swaps for
        # a sidecar file holding the latest hash + length.
        last = _GENESIS_HASH
        with self._path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    last = json.loads(line)["hash"]
                except (json.JSONDecodeError, KeyError):
                    # Corruption mid-chain; refuse to extend.
                    raise RuntimeError(
                        f"audit log appears corrupted at {self._path} — run verify() to locate"
                    )
        return last


def _hash_entry(entry: dict[str, Any]) -> str:
    canonical = json.dumps(entry, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")
