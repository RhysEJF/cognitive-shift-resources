"""
Prod-system interface.

Two backends with an identical method surface so the executor is backend-
agnostic. The selection is made via the URL scheme:

    sqlite:///path/to/prod.db
    postgresql://user:pass@host:port/db

For the demo, SQLite is the default (fast, no deps). The Postgres backend is
used when re-running against Railway EU to demonstrate that the trust-boundary
architecture is identical across local and hosted infrastructure — only the
connection string changes.
"""

from __future__ import annotations

import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


# -------- shared interface --------

class ProdStore(ABC):
    """Abstract prod-system interface. Both SQLite and Postgres implement this."""

    @abstractmethod
    def set_review_status(self, patient_id: str, status: str) -> None: ...

    @abstractmethod
    def flag_for_review(self, patient_id: str, reason: str) -> None: ...

    @abstractmethod
    def schedule_followup(self, patient_id: str, weeks_out: int, reason: str) -> None: ...

    @abstractmethod
    def append_note(self, patient_id: str, note: str) -> None: ...

    @abstractmethod
    def summarize(self) -> dict[str, int]: ...

    @abstractmethod
    def get_patient(self, patient_id: str) -> dict | None: ...

    @abstractmethod
    def close(self) -> None: ...

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


# -------- factory --------

def prod_store_from_url(url: str) -> ProdStore:
    """Pick the backend based on the URL scheme."""
    scheme = urlparse(url).scheme
    if scheme == "sqlite":
        path = url.removeprefix("sqlite:///")
        return SqliteProdStore(Path(path))
    if scheme in ("postgres", "postgresql"):
        return PostgresProdStore(url)
    raise ValueError(f"unsupported prod backend scheme: {scheme!r}")


# -------- SQLite backend --------

_SQLITE_SCHEMA = """
CREATE TABLE IF NOT EXISTS patients (
    patient_id     TEXT PRIMARY KEY,
    review_status  TEXT NOT NULL DEFAULT 'stable',
    flagged_reason TEXT,
    updated_at     TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS followups (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id     TEXT NOT NULL,
    weeks_out      INTEGER NOT NULL,
    reason         TEXT NOT NULL,
    created_at     TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

CREATE TABLE IF NOT EXISTS notes (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id     TEXT NOT NULL,
    note           TEXT NOT NULL,
    created_at     TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
"""


class SqliteProdStore(ProdStore):
    def __init__(self, db_path: Path):
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(db_path))
        self._conn.executescript(_SQLITE_SCHEMA)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def _ensure_patient(self, patient_id: str) -> None:
        self._conn.execute(
            "INSERT OR IGNORE INTO patients (patient_id, updated_at) VALUES (?, ?)",
            (patient_id, _now()),
        )

    def set_review_status(self, patient_id, status):
        self._ensure_patient(patient_id)
        self._conn.execute(
            "UPDATE patients SET review_status = ?, updated_at = ? WHERE patient_id = ?",
            (status, _now(), patient_id),
        )
        self._conn.commit()

    def flag_for_review(self, patient_id, reason):
        self._ensure_patient(patient_id)
        self._conn.execute(
            "UPDATE patients SET flagged_reason = ?, updated_at = ? WHERE patient_id = ?",
            (reason, _now(), patient_id),
        )
        self._conn.commit()

    def schedule_followup(self, patient_id, weeks_out, reason):
        self._ensure_patient(patient_id)
        self._conn.execute(
            "INSERT INTO followups (patient_id, weeks_out, reason, created_at) "
            "VALUES (?, ?, ?, ?)",
            (patient_id, weeks_out, reason, _now()),
        )
        self._conn.commit()

    def append_note(self, patient_id, note):
        self._ensure_patient(patient_id)
        self._conn.execute(
            "INSERT INTO notes (patient_id, note, created_at) VALUES (?, ?, ?)",
            (patient_id, note, _now()),
        )
        self._conn.commit()

    def summarize(self):
        return {
            "patients": self._conn.execute("SELECT COUNT(*) FROM patients").fetchone()[0],
            "followups": self._conn.execute("SELECT COUNT(*) FROM followups").fetchone()[0],
            "notes": self._conn.execute("SELECT COUNT(*) FROM notes").fetchone()[0],
        }

    def get_patient(self, patient_id):
        row = self._conn.execute(
            "SELECT patient_id, review_status, flagged_reason, updated_at FROM patients WHERE patient_id = ?",
            (patient_id,),
        ).fetchone()
        if not row:
            return None
        return {
            "patient_id": row[0],
            "review_status": row[1],
            "flagged_reason": row[2],
            "updated_at": row[3],
        }


# -------- Postgres backend --------

_PG_SCHEMA = """
CREATE TABLE IF NOT EXISTS patients (
    patient_id     TEXT PRIMARY KEY,
    review_status  TEXT NOT NULL DEFAULT 'stable',
    flagged_reason TEXT,
    updated_at     TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS followups (
    id             BIGSERIAL PRIMARY KEY,
    patient_id     TEXT NOT NULL REFERENCES patients(patient_id),
    weeks_out      INTEGER NOT NULL,
    reason         TEXT NOT NULL,
    created_at     TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS notes (
    id             BIGSERIAL PRIMARY KEY,
    patient_id     TEXT NOT NULL REFERENCES patients(patient_id),
    note           TEXT NOT NULL,
    created_at     TIMESTAMPTZ NOT NULL
);
"""


class PostgresProdStore(ProdStore):
    def __init__(self, url: str):
        import psycopg  # imported lazily so SQLite-only runs don't pay the cost
        self._psycopg = psycopg
        self._conn = psycopg.connect(url, autocommit=False)
        with self._conn.cursor() as cur:
            cur.execute(_PG_SCHEMA)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def _ensure_patient(self, patient_id: str, cur) -> None:
        cur.execute(
            "INSERT INTO patients (patient_id, updated_at) VALUES (%s, %s) "
            "ON CONFLICT (patient_id) DO NOTHING",
            (patient_id, _now_dt()),
        )

    def set_review_status(self, patient_id, status):
        with self._conn.cursor() as cur:
            self._ensure_patient(patient_id, cur)
            cur.execute(
                "UPDATE patients SET review_status = %s, updated_at = %s WHERE patient_id = %s",
                (status, _now_dt(), patient_id),
            )
        self._conn.commit()

    def flag_for_review(self, patient_id, reason):
        with self._conn.cursor() as cur:
            self._ensure_patient(patient_id, cur)
            cur.execute(
                "UPDATE patients SET flagged_reason = %s, updated_at = %s WHERE patient_id = %s",
                (reason, _now_dt(), patient_id),
            )
        self._conn.commit()

    def schedule_followup(self, patient_id, weeks_out, reason):
        with self._conn.cursor() as cur:
            self._ensure_patient(patient_id, cur)
            cur.execute(
                "INSERT INTO followups (patient_id, weeks_out, reason, created_at) "
                "VALUES (%s, %s, %s, %s)",
                (patient_id, weeks_out, reason, _now_dt()),
            )
        self._conn.commit()

    def append_note(self, patient_id, note):
        with self._conn.cursor() as cur:
            self._ensure_patient(patient_id, cur)
            cur.execute(
                "INSERT INTO notes (patient_id, note, created_at) VALUES (%s, %s, %s)",
                (patient_id, note, _now_dt()),
            )
        self._conn.commit()

    def summarize(self):
        with self._conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM patients")
            p = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM followups")
            f = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM notes")
            n = cur.fetchone()[0]
        return {"patients": p, "followups": f, "notes": n}

    def get_patient(self, patient_id):
        with self._conn.cursor() as cur:
            cur.execute(
                "SELECT patient_id, review_status, flagged_reason, updated_at "
                "FROM patients WHERE patient_id = %s",
                (patient_id,),
            )
            row = cur.fetchone()
        if not row:
            return None
        return {
            "patient_id": row[0],
            "review_status": row[1],
            "flagged_reason": row[2],
            "updated_at": row[3].isoformat(timespec="seconds") if row[3] else None,
        }


# -------- time helpers --------

def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _now_dt() -> datetime:
    return datetime.now(timezone.utc)
