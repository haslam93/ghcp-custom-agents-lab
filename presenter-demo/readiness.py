"""Small, deliberately incomplete release-readiness example for the presenter."""

from collections.abc import Sequence


VALID_STATUSES = frozenset({"passed", "failed", "pending"})


def release_state(checks: Sequence[str]) -> str:
    """Summarize supplied check results without running any release actions."""
    invalid = [status for status in checks if status not in VALID_STATUSES]
    if invalid:
        raise ValueError("Each check must be passed, failed, or pending.")
    return "ready" if all(status == "passed" for status in checks) else "not_ready"
