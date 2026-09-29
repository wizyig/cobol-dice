from typing import Sequence

from adapter.types import RecoveryReport


def recovery_rate(reports: Sequence[RecoveryReport]) -> float:
    if len(reports) == 0:
        return 0.0
    recovered = sum(1 for r in reports if r["recovered"])
    return recovered / len(reports)


def mean_recovery_steps(reports: Sequence[RecoveryReport]) -> float:
    recovered = [r["steps"] for r in reports if r["recovered"]]
    if not recovered:
        return 0.0
    return sum(recovered) / len(recovered)
