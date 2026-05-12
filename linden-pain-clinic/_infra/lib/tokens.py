"""
Deterministic pseudonym token generation.

Tokens are derived from values via HMAC-SHA256 with a secret key kept on the
vault host. Same value + same key = same token, so the LLM can reason about
entities coherently across the brain without ever seeing the real value.

Different installations (different keys) produce entirely different token
universes, so a leaked brain from clinic A cannot be cross-referenced with a
leaked brain from clinic B.
"""

from __future__ import annotations

import hashlib
import hmac
import secrets
import unicodedata
from pathlib import Path

# Length of the token suffix in hex chars (24 chars = 96 bits, very low collision risk).
_TOKEN_LEN = 12


def load_or_create_token_key(key_path: Path) -> bytes:
    """Read the HMAC key from disk, or create a fresh 32-byte random key if missing."""
    if key_path.exists():
        return key_path.read_bytes()
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key = secrets.token_bytes(32)
    key_path.write_bytes(key)
    key_path.chmod(0o600)
    return key


def _normalise(value: str) -> str:
    """
    Normalise a value so semantically-equal values produce the same token.

    "  Sarah  Müller " and "sarah müller" must produce the same token, otherwise
    a single patient with whitespace or case variations would split into multiple
    pseudonyms and break cross-referencing.
    """
    return unicodedata.normalize("NFKC", value).strip().lower()


def token_for(kind: str, value: str, key: bytes) -> str:
    """
    Generate a stable pseudonym token for `value` of category `kind`.

    Returns e.g. "PERSON_a3f9b2c4d8e1".

    `kind` partitions the token namespace so a person's name and an address
    that happen to normalise to the same string can't collide.
    """
    normalised = _normalise(value)
    payload = f"{kind}|{normalised}".encode("utf-8")
    mac = hmac.new(key, payload, hashlib.sha256).hexdigest()
    return f"{kind.upper()}_{mac[:_TOKEN_LEN]}"


# Token kinds used by the scrubber. Keeping this as a flat enum-like set so the
# vault can validate kinds it accepts.
KINDS = frozenset(
    {
        "PERSON",
        "DOB",          # birth dates specifically (most-sensitive date)
        "DATE",         # any other date (encounter, follow-up, etc.)
        "MRN",
        "SSN",
        "PASSPORT",
        "DRIVER_LICENSE",
        "PHONE",
        "EMAIL",
        "ADDRESS",
        "CITY",
        "POSTCODE",
        "GEO",
        "URL",
    }
)
