import pytest

from adapter.shrine_adapter import transform

FORBIDDEN = ["原因", "故障", "ユーザー", "設定ミス", "メモリ"]


@pytest.mark.parametrize(
    "message",
    ["invalid request", "invalid sides", "invalid payload"],
)
def test_no_inference(message: str) -> None:
    result = transform(
        {"request_id": "REQ-1", "status": "ERROR", "message": message}
    )
    for word in FORBIDDEN:
        assert word not in result["text"]
    assert message in result["text"]
