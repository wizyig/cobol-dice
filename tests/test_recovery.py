import pytest

from adapter.recovery import analyze_recovery
from adapter.shrine_adapter import transform_sequence


def test_recovery_detected() -> None:
    result = transform_sequence(
        [
            {"request_id": "REQ-1", "status": "ERROR", "message": "invalid request"},
            {"request_id": "REQ-1", "status": "OK", "result": "heads"},
        ]
    )
    assert result["class_name"] == "RECOVERY"


@pytest.mark.parametrize(
    "events",
    [
        [
            {"request_id": "REQ-1", "status": "OK", "result": 1},
            {"request_id": "REQ-1", "status": "OK", "result": 2},
        ],
        [
            {"request_id": "REQ-1", "status": "ERROR", "message": "invalid request"},
            {"request_id": "REQ-2", "status": "OK", "result": 1},
        ],
        [
            {"request_id": "REQ-1", "status": "ERROR", "message": "invalid request"},
            {"request_id": "REQ-1", "status": "ERROR", "message": "invalid request"},
        ],
    ],
)
def test_not_recovery(events: list) -> None:
    result = transform_sequence(events)
    assert result["class_name"] != "RECOVERY"


def test_empty_sequence() -> None:
    with pytest.raises(ValueError):
        transform_sequence([])


def test_mixed_id_report() -> None:
    with pytest.raises(ValueError):
        analyze_recovery(
            [
                {"request_id": "REQ-1", "status": "ERROR", "message": "invalid request"},
                {"request_id": "REQ-2", "status": "OK", "result": 1},
            ]
        )
