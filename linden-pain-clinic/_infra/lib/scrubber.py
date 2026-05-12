"""
Scrubber: PatientNarrative → pseudonymized markdown + vault entries.

Two-pass approach:

    1. STRUCTURED PASS — for every PII field we already know about (from FHIR),
       do exact-string substitution in the narrative. Reliable because we have
       the value directly. Populates the vault.

    2. NER PASS — run Presidio over the result to catch any PII that slipped
       through (free-text references to other people, places, dates). Generate
       tokens for these too.

The structured pass is the trust crown jewel. Presidio is a safety net, not the
primary defense — production deployments tune custom recognizers for their
domain (MRN formats, internal IDs, etc.).
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from presidio_analyzer import AnalyzerEngine

from lib.composer import IdentifiedField, PatientNarrative
from lib.tokens import KINDS, token_for
from lib.vault import Vault


# Presidio entity → our token KIND. Anything not in this map is ignored.
# We default Presidio's DATE_TIME to DATE (not DOB); the composer marks the
# actual birth date explicitly as DOB in the structured pass.
_PRESIDIO_TO_KIND = {
    "PERSON": "PERSON",
    "DATE_TIME": "DATE",
    "PHONE_NUMBER": "PHONE",
    "EMAIL_ADDRESS": "EMAIL",
    "LOCATION": "CITY",
    "URL": "URL",
    "US_SSN": "SSN",
}

# Presidio confidence floor. Below this we trust the entity is noise.
_MIN_CONFIDENCE = 0.5


@dataclass
class ScrubResult:
    pseudonymised: str
    structured_subs: int   # number of structured-pass substitutions
    ner_subs: int          # number of NER-pass substitutions
    new_vault_entries: int


def scrub(
    narrative: PatientNarrative,
    vault: Vault,
    token_key: bytes,
    *,
    analyzer: AnalyzerEngine | None = None,
) -> ScrubResult:
    """
    Scrub a PatientNarrative. Returns a ScrubResult and mutates the vault.

    The analyzer is injected so callers can reuse a warm Presidio engine across
    many patients (cold start is ~5s; reuse drops per-patient cost to ms).
    """
    text = narrative.markdown
    structured_subs = 0
    ner_subs = 0
    new_vault_entries_before = vault.count(
        purpose=f"scrubber:before:{narrative.patient_uuid}"
    )

    # ---- PASS 1: Structured substitution ----
    # Sort by descending length so e.g. "Sarah Müller" is replaced before "Sarah".
    # We flatten identifiers into (kind, replace_string, canonical_value) so
    # aliases substitute to the canonical token, not their own.
    substitutions: list[tuple[str, str, str, str | None]] = []
    for ident in narrative.identifiers:
        if ident.kind not in KINDS:
            continue
        token = token_for(ident.kind, ident.value, token_key)
        vault.put(token, ident.kind, ident.value, prod_id=ident.prod_id)
        substitutions.append((ident.kind, ident.value, token, ident.prod_id))
        for alias in ident.aliases:
            substitutions.append((ident.kind, alias, token, ident.prod_id))

    substitutions.sort(key=lambda s: len(s[1]), reverse=True)
    for kind, search_str, token, _prod_id in substitutions:
        pattern = re.compile(
            r"(?<![A-Za-z0-9])" + re.escape(search_str) + r"(?![A-Za-z0-9])"
        )
        text, n = pattern.subn(f"[{token}]", text)
        structured_subs += n

    # ---- PASS 2: NER safety net ----
    if analyzer is None:
        analyzer = AnalyzerEngine()
    findings = analyzer.analyze(text=text, language="en")
    findings = [f for f in findings if f.score >= _MIN_CONFIDENCE]
    # Process from right-to-left so spans stay stable while we substitute.
    findings.sort(key=lambda f: f.start, reverse=True)
    for f in findings:
        kind = _PRESIDIO_TO_KIND.get(f.entity_type)
        if not kind:
            continue
        original = text[f.start : f.end]
        # Skip if the original is already a token (Presidio sometimes flags them
        # because tokens look like names: "PERSON_a3f9b2c4d8e1").
        if original.startswith("[") and original.endswith("]"):
            continue
        if re.match(r"^[A-Z]+_[a-f0-9]+$", original.strip("[]")):
            continue
        token = token_for(kind, original, token_key)
        vault.put(token, kind, original, prod_id=None)
        text = text[: f.start] + f"[{token}]" + text[f.end :]
        ner_subs += 1

    new_vault_entries = vault.count(
        purpose=f"scrubber:after:{narrative.patient_uuid}"
    ) - new_vault_entries_before
    return ScrubResult(
        pseudonymised=text,
        structured_subs=structured_subs,
        ner_subs=ner_subs,
        new_vault_entries=new_vault_entries,
    )
