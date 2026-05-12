"""
CLI: scrub Synthea FHIR Bundles → pseudonymised markdown notes in the team brain.

Usage:
    uv run scrub                  # scrub all pain-flagged patients
    uv run scrub --limit 10       # quick test with first 10
    uv run scrub --include-all    # don't filter by pain condition
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click
from presidio_analyzer import AnalyzerEngine

from lib.audit import AuditLog
from lib.composer import compose
from lib.scrubber import scrub
from lib.tokens import load_or_create_token_key
from lib.vault import Vault, load_or_create_encryption_key


# Paths anchored to _infra/, regardless of where uv run is invoked from.
_INFRA = Path(__file__).resolve().parent.parent
_SYNTHEA_OUT = _INFRA / "synthea-raw" / "output" / "fhir"
_VAULT_DIR = _INFRA / "vault"
_AUDIT_LOG = _INFRA / "audit-log" / "audit.jsonl"
_TEAM_BRAIN_PATIENTS = _INFRA.parent / "team-brain" / "patients"


@click.command()
@click.option("--limit", type=int, default=None, help="Process at most N patients (after filtering).")
@click.option("--include-all", is_flag=True, help="Include patients without pain conditions.")
def main(limit: int | None, include_all: bool) -> None:
    if not _SYNTHEA_OUT.exists():
        click.echo(f"!! Synthea output not found at {_SYNTHEA_OUT}", err=True)
        sys.exit(1)

    # ---- Open vault and audit log ----
    token_key = load_or_create_token_key(_VAULT_DIR / "token_key.bin")
    enc_key = load_or_create_encryption_key(_VAULT_DIR / "vault_key.bin")
    audit = AuditLog(_AUDIT_LOG)

    audit.append(event="scrub.start", limit=limit, include_all=include_all)

    _TEAM_BRAIN_PATIENTS.mkdir(parents=True, exist_ok=True)

    # ---- Warm Presidio once ----
    click.echo("Warming Presidio analyzer (first call is slow)...")
    analyzer = AnalyzerEngine()

    # ---- Iterate Synthea bundles ----
    patient_files = sorted(
        p for p in _SYNTHEA_OUT.glob("*.json")
        # Skip aggregate files like hospitalInformation*.json
        if not (p.name.startswith("hospitalInformation") or p.name.startswith("practitionerInformation"))
    )

    processed = 0
    skipped_no_pain = 0
    total_structured = 0
    total_ner = 0

    with Vault(_VAULT_DIR / "vault.db", enc_key, audit=audit) as vault:
        for path in patient_files:
            with path.open("r", encoding="utf-8") as f:
                bundle = json.load(f)

            try:
                narrative = compose(bundle)
            except ValueError as e:
                click.echo(f"  skip {path.name}: {e}", err=True)
                continue

            if not include_all and not narrative.has_pain_condition:
                skipped_no_pain += 1
                continue

            result = scrub(narrative, vault, token_key, analyzer=analyzer)
            total_structured += result.structured_subs
            total_ner += result.ner_subs

            # Find the token for the patient's full name so we can name the file by it.
            patient_token = _patient_token_from_narrative(narrative, token_key)
            out_path = _TEAM_BRAIN_PATIENTS / f"{patient_token}.md"
            out_path.write_text(result.pseudonymised, encoding="utf-8")

            audit.append(
                event="scrub.patient",
                patient_uuid=narrative.patient_uuid,
                patient_token=patient_token,
                structured_subs=result.structured_subs,
                ner_subs=result.ner_subs,
                new_vault_entries=result.new_vault_entries,
            )

            processed += 1
            if processed % 10 == 0:
                click.echo(f"  ... {processed} patients scrubbed")
            if limit is not None and processed >= limit:
                break

        kinds = vault.count_by_kind(purpose="cli_scrub:summary")

    audit.append(
        event="scrub.done",
        processed=processed,
        skipped_no_pain=skipped_no_pain,
        total_structured=total_structured,
        total_ner=total_ner,
        vault_size=sum(kinds.values()),
    )

    click.echo("")
    click.echo(f"✓ Scrubbed {processed} patients")
    click.echo(f"  Skipped {skipped_no_pain} without pain conditions")
    click.echo(f"  Structured substitutions: {total_structured}")
    click.echo(f"  NER substitutions:        {total_ner}")
    click.echo(f"  Vault entries by kind:")
    for kind, n in sorted(kinds.items()):
        click.echo(f"    {kind:12s}: {n}")


def _patient_token_from_narrative(narrative, token_key) -> str:
    """Resolve the token used for the patient's primary full-name identifier."""
    from lib.tokens import token_for
    for ident in narrative.identifiers:
        # First PERSON entry tied to a prod_id is the patient themselves.
        if ident.kind == "PERSON" and ident.prod_id == narrative.patient_uuid:
            return token_for("PERSON", ident.value, token_key)
    # Fallback: token derived from the FHIR UUID
    return token_for("PERSON", narrative.patient_uuid, token_key)


if __name__ == "__main__":
    main()
