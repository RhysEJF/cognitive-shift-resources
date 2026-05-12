"""
Whitelist of operations the executor will apply to the prod system.

CRITICAL PROPERTY: this list is the ONLY way state ever changes in prod. If
the LLM's plan contains an op not in this list, the executor refuses the
entire plan. This is the boundary that contains LLM behaviour: even with
prompt injection, the worst the agent can do is fail to act.

Each operation declares:
    - name             : the op string in the plan
    - required_fields  : fields the plan must provide (validated by type)
    - allowed_values   : optional set of allowed values per field
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class OperationSpec:
    name: str
    required_fields: dict[str, type]
    allowed_values: dict[str, frozenset[str]]


REVIEW_STATUSES = frozenset(
    {
        "needs_review",
        "needs_followup",
        "stable",
        "escalate_to_consultant",
        "discharge_to_gp",
    }
)


OPERATIONS: dict[str, OperationSpec] = {
    "set_review_status": OperationSpec(
        name="set_review_status",
        required_fields={"patient": str, "status": str},
        allowed_values={"status": REVIEW_STATUSES},
    ),
    "flag_for_review": OperationSpec(
        name="flag_for_review",
        required_fields={"patient": str, "reason": str},
        allowed_values={},
    ),
    "schedule_followup": OperationSpec(
        name="schedule_followup",
        required_fields={"patient": str, "weeks_out": int, "reason": str},
        allowed_values={},
    ),
    "append_note": OperationSpec(
        name="append_note",
        required_fields={"patient": str, "note": str},
        allowed_values={},
    ),
}


class PlanValidationError(Exception):
    """Raised when a plan contains an operation the executor refuses to apply."""


def validate_op(op: dict[str, Any]) -> OperationSpec:
    """
    Validate a single operation dict from the plan.

    Returns the OperationSpec on success; raises PlanValidationError otherwise.
    """
    op_name = op.get("op")
    if not op_name:
        raise PlanValidationError("operation missing 'op' field")
    spec = OPERATIONS.get(op_name)
    if not spec:
        raise PlanValidationError(
            f"unknown operation {op_name!r}; allowed: {sorted(OPERATIONS)}"
        )
    for field, expected_type in spec.required_fields.items():
        if field not in op:
            raise PlanValidationError(f"{op_name}: missing field {field!r}")
        if not isinstance(op[field], expected_type):
            raise PlanValidationError(
                f"{op_name}: field {field!r} must be {expected_type.__name__}, got {type(op[field]).__name__}"
            )
    for field, allowed in spec.allowed_values.items():
        if op[field] not in allowed:
            raise PlanValidationError(
                f"{op_name}: {field}={op[field]!r} not in allowed values {sorted(allowed)}"
            )
    # The 'patient' field must look like a PERSON token; not enforcing the
    # exact format here so we can catch it later in the executor with a clearer
    # vault-miss error, but we reject the obvious case of a raw name.
    patient = op.get("patient", "")
    if not patient.startswith("PERSON_"):
        raise PlanValidationError(
            f"{op_name}: 'patient' must be a PERSON token (got {patient!r}). "
            f"The LLM should never reference patients by raw name or ID."
        )
    return spec
