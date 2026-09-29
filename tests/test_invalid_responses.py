import pytest

from adapter.shrine_adapter import transform

INVALID_CASES = [
    {},
    {"status": "OK", "result": 1},
    {"request_id": "", "status": "OK", "result": 1},
    {"request_id": "REQ", "status": "BROKEN"},
    {"request_id": "REQ", "status": "OK"},
    {"request_id": "REQ", "status": "ERROR"},
    {
        "request_id": "REQ",
        "status": "OK",
        "result": 1,
        "message": "invalid request",
    },
    {
        "request_id": "REQ",
        "status": "ERROR",
        "message": "invalid request",
        "result": 1,
    },
    {"request_id": "REQ", "status": "ERROR", "message": "segfault"},
]


@pytest.mark.parametrize("payload", INVALID_CASES)
def test_invalid_response(payload: dict) -> None:
    with pytest.raises(ValueError):
        transform(payload)
