import pytest

from adapter.schema import validate_request


def test_dice_min() -> None:
    validate_request({"request_id": "REQ", "tool": "dice", "sides": 2})


def test_dice_max() -> None:
    validate_request({"request_id": "REQ", "tool": "dice", "sides": 1000})


@pytest.mark.parametrize("value", [1, 0, -1, 1001])
def test_invalid_sides(value: int) -> None:
    with pytest.raises(ValueError):
        validate_request({"request_id": "REQ", "tool": "dice", "sides": value})


def test_echo_min() -> None:
    validate_request({"request_id": "REQ", "tool": "echo", "payload": "A"})


def test_echo_max() -> None:
    validate_request({"request_id": "REQ", "tool": "echo", "payload": "A" * 80})


@pytest.mark.parametrize("payload", ["", "A" * 81])
def test_echo_invalid(payload: str) -> None:
    with pytest.raises(ValueError):
        validate_request({"request_id": "REQ", "tool": "echo", "payload": payload})
