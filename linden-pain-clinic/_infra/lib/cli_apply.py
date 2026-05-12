"""
CLI: apply a plan against the prod system, with full audit trail.

Usage:
    uv run apply-plan path/to/plan.yaml
    uv run apply-plan path/to/plan.yaml --actor "claude-code:rhys"
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import click
import yaml

from lib.audit import AuditLog
from lib.executor import execute_plan
from lib.prod import prod_store_from_url
from lib.tokens import load_or_create_token_key  # noqa: F401  (kept symmetric)
from lib.vault import Vault, load_or_create_encryption_key


_INFRA = Path(__file__).resolve().parent.parent
_VAULT_DIR = _INFRA / "vault"
_DEFAULT_PROD_URL = f"sqlite:///{_INFRA / 'prod-target' / 'prod.db'}"
_AUDIT_LOG = _INFRA / "audit-log" / "audit.jsonl"
_CONNECTION_ENV = _INFRA / "prod-target" / "connection.env"


def _load_prod_url() -> str:
    """Resolve the prod URL from (in order): PROD_DB_URL env var, connection.env, default."""
    if env := os.environ.get("PROD_DB_URL"):
        return env
    if _CONNECTION_ENV.exists():
        for raw in _CONNECTION_ENV.read_text().splitlines():
            line = raw.strip()
            if line.startswith("PROD_DB_URL="):
                return line.removeprefix("PROD_DB_URL=").strip().strip('"').strip("'")
    return _DEFAULT_PROD_URL


@click.command()
@click.argument("plan_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--actor", default="claude-code-session", help="Who/what produced this plan.")
def main(plan_path: Path, actor: str) -> None:
    plan = yaml.safe_load(plan_path.read_text(encoding="utf-8"))
    if not isinstance(plan, dict):
        click.echo("!! plan file must be a YAML mapping at top level", err=True)
        sys.exit(2)

    prod_url = _load_prod_url()
    # Display only the scheme + host; never log credentials.
    from urllib.parse import urlparse
    parsed = urlparse(prod_url)
    click.echo(f"Prod backend: {parsed.scheme}://{parsed.hostname or 'local'}")

    enc_key = load_or_create_encryption_key(_VAULT_DIR / "vault_key.bin")
    audit = AuditLog(_AUDIT_LOG)

    with Vault(_VAULT_DIR / "vault.db", enc_key, audit=audit) as vault, prod_store_from_url(prod_url) as prod:
        result = execute_plan(plan, vault=vault, prod=prod, audit=audit, actor=actor)

    click.echo("")
    click.echo(f"Plan {result.plan_id}")
    click.echo(f"  Validated: {result.ops_validated}")
    click.echo(f"  Applied:   {result.ops_applied}")
    if result.errors:
        click.echo(f"  Errors ({len(result.errors)}):")
        for e in result.errors:
            click.echo(f"    - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
