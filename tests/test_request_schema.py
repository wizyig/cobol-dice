import pytest
from adapter.jsonschema_lite import validate

from adapter.schema import validate_request
from tests.helpers import assert_schema_invalid


def test_valid_dice() -> None:
    validate_request({"request_id": "REQ-1", "tool": "dice", "sides": 6})


def test_valid_coin() -> None:
    validate_request({"request_id": "REQ-1", "tool": "coin"})


def test_missing_request_id() -> None:
    with pytest.raises(ValueError):
        validate_request({"tool": "coin"})


def test_invalid_tool() -> None:
    with pytest.raises(ValueError):
        validate_request({"request_id": "REQ-1", "tool": "roulette"})


def test_request_schema_ok(request_schema: dict) -> None:
    validate(
        {"request_id": "REQ", "tool": "dice", "sides": 6},
        request_schema,
    )


@pytest.mark.parametrize(
    "payload,msg",
    [
        ({}, "request_id"),
        ({"tool": "dice"}, "request_id"),
        ({"request_id": "REQ"}, "tool"),
        ({"request_id": "REQ", "tool": "roulette"}, "enum"),
        ({"request_id": "REQ", "tool": "dice", "sides": 1}, "minimum"),
        ({"request_id": "REQ", "tool": "dice", "sides": 1001}, "maximum"),
    ],
)
def test_request_schema_failure(payload: dict, msg: str, request_schema: dict) -> None:
    assert_schema_invalid(payload, request_schema, msg)
