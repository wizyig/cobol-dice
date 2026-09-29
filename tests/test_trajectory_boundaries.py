import pytest

from adapter.recovery import analyze_recovery
from adapter.recovery_metrics import mean_recovery_steps
from adapter.recovery_metrics import recovery_rate


def _err() -> dict:
    return {"request_id": "REQ", "status": "ERROR", "message": "invalid request"}


def _ok() -> dict:
    return {"request_id": "REQ", "status": "OK", "result": 1}


CASES = [
    ([_err(), _ok()], 1, True),
    ([_err(), _ok(), _err(), _ok()], 2, True),
    ([_err(), _ok(), _err()], 1, False),
    ([_ok(), _err(), _ok()], 1, True),
    ([_ok()], 0, False),
]


@pytest.mark.parametrize("events,recovery_count,recovered", CASES)
def test_trajectory_boundary_cases(
    events: list, recovery_count: int, recovered: bool
) -> None:
    report = analyze_recovery(events)
    assert report["recovery_count"] == recovery_count
    assert report["recovered"] is recovered


def test_recovery_rate() -> None:
    reports = [
        analyze_recovery([_err(), _ok()]),
        analyze_recovery([_err(), _err()]),
    ]
    assert recovery_rate(reports) == 0.5
    assert mean_recovery_steps(reports) == 2.0


def test_metrics_empty() -> None:
    assert recovery_rate([]) == 0.0
    assert mean_recovery_steps([]) == 0.0
