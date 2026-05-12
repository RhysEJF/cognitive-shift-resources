"""
Executor: turns a token-only plan into prod state changes.

Steps for each operation in the plan:
    1. Validate against the operation whitelist (lib.operations)
    2. Resolve the patient token to a real patient_id via the vault (audited)
    3. Dispatch to the matching ProdStore method
    4. Audit-log the prod write

If ANY operation fails validation or vault lookup, the entire plan is aborted
before any prod writes happen. (Atomic-or-nothing is overkill for SQLite but
sets the right expectation for a real deployment with transactional prod.)
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from lib.audit import AuditLog
from lib.operations import OPERATIONS, PlanValidationError, validate_op
from lib.prod import ProdStore
from lib.vault import Vault


@dataclass
class ExecutionResult:
    plan_id: str
    ops_validated: int
    ops_applied: int
    errors: list[str]


def execute_plan(
    plan: dict,
    *,
    vault: Vault,
    prod: ProdStore,
    audit: AuditLog,
    actor: str = "claude-code-session",
) -> ExecutionResult:
    """
    Validate and apply a plan. Audit every step.

    `actor` identifies who/what produced the plan; lands in the audit log.
    """
    plan_id = plan.get("plan_id") or str(uuid.uuid4())
    ops = plan.get("operations") or []

    audit.append(event="executor.plan.start", plan_id=plan_id, actor=actor, op_count=len(ops))

    # ---- Pass 1: validate everything ----
    errors: list[str] = []
    for i, op in enumerate(ops):
        try:
            validate_op(op)
        except PlanValidationError as e:
            errors.append(f"op[{i}] ({op.get('op','?')}): {e}")

    if errors:
        audit.append(
            event="executor.plan.rejected",
            plan_id=plan_id,
            reason="validation",
            errors=errors,
        )
        return ExecutionResult(plan_id=plan_id, ops_validated=0, ops_applied=0, errors=errors)

    # ---- Pass 2: apply ----
    applied = 0
    for i, op in enumerate(ops):
        op_name = op["op"]
        token = op["patient"]
        purpose = f"executor:{op_name}:{plan_id}"
        try:
            patient_id = vault.prod_id_for(token, purpose=purpose)
        except KeyError as e:
            err = f"op[{i}] ({op_name}): vault miss for {token}"
            errors.append(err)
            audit.append(event="executor.op.failed", plan_id=plan_id, op_index=i, op=op_name, error=err)
            continue

        if patient_id is None:
            err = f"op[{i}] ({op_name}): token {token} has no prod_id; cannot apply"
            errors.append(err)
            audit.append(event="executor.op.failed", plan_id=plan_id, op_index=i, op=op_name, error=err)
            continue

        try:
            _dispatch(op, patient_id=patient_id, prod=prod)
        except Exception as e:
            err = f"op[{i}] ({op_name}): {type(e).__name__}: {e}"
            errors.append(err)
            audit.append(event="executor.op.failed", plan_id=plan_id, op_index=i, op=op_name, error=err)
            continue

        applied += 1
        audit.append(
            event="executor.op.applied",
            plan_id=plan_id,
            op_index=i,
            op=op_name,
            patient_token=token,
            patient_prod_id=patient_id,
        )

    audit.append(
        event="executor.plan.done",
        plan_id=plan_id,
        ops_applied=applied,
        ops_failed=len(ops) - applied,
    )
    return ExecutionResult(
        plan_id=plan_id, ops_validated=len(ops), ops_applied=applied, errors=errors
    )


def _dispatch(op: dict, *, patient_id: str, prod: ProdStore) -> None:
    name = op["op"]
    if name == "set_review_status":
        prod.set_review_status(patient_id, op["status"])
    elif name == "flag_for_review":
        prod.flag_for_review(patient_id, op["reason"])
    elif name == "schedule_followup":
        prod.schedule_followup(patient_id, op["weeks_out"], op["reason"])
    elif name == "append_note":
        prod.append_note(patient_id, op["note"])
    else:
        # Defensive: validate_op should have caught this.
        raise PlanValidationError(f"unhandled op in dispatch: {name}")
