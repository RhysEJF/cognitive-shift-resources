"""
FHIR Bundle → clinical narrative.

Synthea outputs are 3-5MB FHIR Bundles per patient with 1,000+ entries. A real
clinic's team brain would never store these wholesale — it would store concise
clinical summaries that humans can scan quickly. This module produces those
summaries.

A `PatientNarrative` carries the markdown narrative plus a structured list of
the known PII fields it contains. The scrubber uses that structured list for
deterministic substitution (no relying on NER alone for identifiers we already
have).
"""

from __future__ import annotations

import re
import uuid
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Iterator

# Numeric suffix Synthea adds to all synthetic names: "Sarah123", "Müller456"
_SYNTHEA_NUMERIC_SUFFIX = re.compile(r"\d+$")

# Conditions we treat as pain-related for narrative framing
_PAIN_KEYWORDS = ("pain", "arthr", "fibro", "neuropathy", "neuralgia", "myalg")


@dataclass(frozen=True)
class IdentifiedField:
    """
    A known PII field with kind and real value.

    `aliases` lists other strings that should resolve to THIS field's token
    (not their own). Used so e.g. "Sarah", "Müller", and "Sarah Müller" all
    pseudonymise to one canonical patient token rather than three.
    """
    kind: str      # "PERSON", "DOB", "MRN", ...
    value: str     # "Sarah Müller" — used to derive the token
    prod_id: str | None = None  # optional foreign key into the prod system
    aliases: tuple[str, ...] = ()


@dataclass
class PatientNarrative:
    """A clinical summary for one patient, with all PII enumerated."""
    patient_uuid: str               # the Patient resource's FHIR id (the prod_id)
    identifiers: list[IdentifiedField] = field(default_factory=list)
    markdown: str = ""              # narrative text, contains PII inline
    has_pain_condition: bool = False


def _clean_synthea_name(name: str) -> str:
    """Strip Synthea's numeric suffix from a name (e.g., 'Sarah123' → 'Sarah')."""
    return _SYNTHEA_NUMERIC_SUFFIX.sub("", name)


def _age_years(birth_date: str) -> int:
    """Compute age in years from an ISO birthdate string."""
    bd = date.fromisoformat(birth_date)
    today = date(2026, 5, 11)  # demo reference date — keeps narratives stable across runs
    return (today - bd).days // 365


def _extract_patient_resource(bundle: dict) -> dict:
    for entry in bundle.get("entry", []):
        r = entry.get("resource", {})
        if r.get("resourceType") == "Patient":
            return r
    raise ValueError("no Patient resource in bundle")


def _extract_conditions(bundle: dict) -> list[dict]:
    """Return active conditions only."""
    out = []
    for entry in bundle.get("entry", []):
        r = entry.get("resource", {})
        if r.get("resourceType") != "Condition":
            continue
        status = r.get("clinicalStatus", {}).get("coding", [{}])[0].get("code")
        if status and status != "active":
            continue
        out.append(r)
    return out


def _extract_recent_encounters(bundle: dict, limit: int = 5) -> list[dict]:
    """Return the most recent N encounters."""
    encs = [
        e["resource"]
        for e in bundle.get("entry", [])
        if e.get("resource", {}).get("resourceType") == "Encounter"
    ]
    encs.sort(
        key=lambda r: r.get("period", {}).get("start", ""),
        reverse=True,
    )
    return encs[:limit]


def _extract_practitioner_names(bundle: dict) -> list[str]:
    """
    Pull practitioner names referenced anywhere in the bundle.
    Synthea bundles don't always include Practitioner resources; the names show
    up inside Encounter.participant.individual.display.
    """
    names = set()
    for entry in bundle.get("entry", []):
        r = entry.get("resource", {})
        if r.get("resourceType") != "Encounter":
            continue
        for participant in r.get("participant", []):
            display = participant.get("individual", {}).get("display", "")
            if display:
                # Strip the trailing UUID-ish suffix Synthea sometimes adds
                display = re.sub(r"\d+$", "", display).strip()
                if display:
                    names.add(display)
    return sorted(names)


def compose(bundle: dict) -> PatientNarrative:
    """Build a PatientNarrative from a Synthea FHIR Bundle."""
    patient = _extract_patient_resource(bundle)
    patient_uuid = patient["id"]

    # ---- Structured identifiers ----
    name_obj = patient["name"][0]
    given = " ".join(_clean_synthea_name(g) for g in name_obj.get("given", []))
    family = _clean_synthea_name(name_obj.get("family", ""))
    full_name = f"{given} {family}".strip()

    birth_date = patient["birthDate"]
    age = _age_years(birth_date)
    gender = patient.get("gender", "unknown")

    mrn = None
    ssn = None
    for ident in patient.get("identifier", []):
        type_text = ident.get("type", {}).get("text", "")
        value = ident.get("value", "")
        if type_text == "Medical Record Number":
            mrn = value
        elif type_text == "Social Security Number":
            ssn = value

    phone = None
    email = None
    for tc in patient.get("telecom", []):
        if tc.get("system") == "phone" and not phone:
            phone = tc.get("value")
        elif tc.get("system") == "email" and not email:
            email = tc.get("value")

    addr_obj = patient.get("address", [{}])[0]
    addr_line = ", ".join(addr_obj.get("line", []))
    addr_city = addr_obj.get("city", "")
    addr_postcode = addr_obj.get("postalCode", "")
    address_full = f"{addr_line}, {addr_city} {addr_postcode}".strip(", ").strip()

    identifiers: list[IdentifiedField] = []
    # Single canonical patient PERSON token; family/given names alias to it.
    if full_name:
        person_aliases = []
        if family and family != full_name:
            person_aliases.append(family)
        if given and given != full_name:
            person_aliases.append(given)
        identifiers.append(
            IdentifiedField(
                "PERSON",
                full_name,
                patient_uuid,
                aliases=tuple(person_aliases),
            )
        )
    if birth_date:
        identifiers.append(IdentifiedField("DOB", birth_date, patient_uuid))
    if mrn:
        identifiers.append(IdentifiedField("MRN", mrn, patient_uuid))
    if ssn:
        identifiers.append(IdentifiedField("SSN", ssn, patient_uuid))
    if phone:
        identifiers.append(IdentifiedField("PHONE", phone, patient_uuid))
    if email:
        identifiers.append(IdentifiedField("EMAIL", email, patient_uuid))
    if addr_line:
        identifiers.append(IdentifiedField("ADDRESS", addr_line, patient_uuid))
    if addr_city:
        identifiers.append(IdentifiedField("CITY", addr_city, patient_uuid))
    if addr_postcode:
        identifiers.append(IdentifiedField("POSTCODE", addr_postcode, patient_uuid))

    # ---- Conditions ----
    conditions = _extract_conditions(bundle)
    condition_texts = [c.get("code", {}).get("text", "?") for c in conditions]
    pain_conditions = [
        c for c in condition_texts if any(k in c.lower() for k in _PAIN_KEYWORDS)
    ]
    has_pain = bool(pain_conditions)

    # ---- Encounters ----
    encounters = _extract_recent_encounters(bundle, limit=5)
    encounter_lines = []
    for enc in encounters:
        start = enc.get("period", {}).get("start", "")[:10]
        reason = (
            enc.get("type", [{}])[0].get("text")
            or enc.get("reasonCode", [{}])[0].get("text", "")
            or "Visit"
        )
        encounter_lines.append((start, reason))
        if start:
            identifiers.append(IdentifiedField("DATE", start, patient_uuid))

    # ---- Practitioner names mentioned ----
    practitioners = _extract_practitioner_names(bundle)
    for p in practitioners:
        identifiers.append(IdentifiedField("PERSON", p, None))

    # ---- Compose the narrative ----
    # No frontmatter: the patient_uuid is a back-channel link to prod and must
    # NEVER appear in the team brain. The patient is identified solely by their
    # pseudonym token, which the scrubber writes into the filename.
    md_lines = []
    md_lines.append(f"# Patient Summary — {full_name}")
    md_lines.append("")
    md_lines.append("## Identifiers")
    md_lines.append(f"- **MRN**: {mrn or '—'}")
    md_lines.append(f"- **DOB**: {birth_date} ({age} y/o, {gender})")
    md_lines.append(f"- **Phone**: {phone or '—'}")
    md_lines.append(f"- **Email**: {email or '—'}")
    md_lines.append(f"- **Address**: {address_full or '—'}")
    md_lines.append("")
    md_lines.append("## Presenting Complaint")
    if pain_conditions:
        md_lines.append(
            f"Chronic pain: {pain_conditions[0]}. Referred by GP for multidisciplinary assessment."
        )
    else:
        md_lines.append(
            "Chronic pain (unspecified). Referred by GP for multidisciplinary assessment."
        )
    md_lines.append("")
    md_lines.append("## Active Conditions")
    for c in condition_texts[:12]:
        md_lines.append(f"- {c}")
    md_lines.append("")
    md_lines.append("## Recent Encounters")
    for date_str, reason in encounter_lines:
        md_lines.append(f"- {date_str}: {reason}")
    md_lines.append("")
    md_lines.append("## Care Team")
    for p in practitioners[:5]:
        md_lines.append(f"- {p}")
    md_lines.append("")
    md_lines.append("## Clinician Notes")
    md_lines.append(
        f"{given} continues under multidisciplinary care for chronic pain management. "
        f"Patient is a {age}-year-old {gender} residing in {addr_city or 'the catchment area'}. "
        f"Reachable on {phone or 'no phone on file'}; correspondence via {email or 'post'}. "
        f"MRN {mrn} on file. Last contact recorded "
        f"{encounter_lines[0][0] if encounter_lines else 'unknown date'}. "
        f"Continue current regimen; review in 6 weeks."
    )
    md_lines.append("")

    return PatientNarrative(
        patient_uuid=patient_uuid,
        identifiers=identifiers,
        markdown="\n".join(md_lines),
        has_pain_condition=has_pain,
    )
