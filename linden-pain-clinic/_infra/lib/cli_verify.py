"""
CLI: verify the audit log's hash chain is intact.

Usage:
    uv run verify-audit
"""

from __future__ import annotations

import sys
from pathlib import Path

import click

from lib.audit import AuditLog


_INFRA = Path(__file__).resolve().parent.parent
_AUDIT_LOG = _INFRA / "audit-log" / "audit.jsonl"


@click.command()
def main() -> None:
    log = AuditLog(_AUDIT_LOG)
    ok, error, count = log.verify()
    if ok:
        click.echo(f"✓ audit log intact: {count} entries verified")
        sys.exit(0)
    else:
        click.echo(f"✗ audit log BROKEN after {count} entries: {error}", err=True)
        sys.exit(1)
