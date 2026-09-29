import pytest
from adapter.jsonschema_lite import validate

from adapter.schema import validate_response
from tests.helpers import assert_schema_invalid


@pytest.mark.parametrize(
    "payload",
    [
        {"request_id": "REQ-1", "status": "OK", "result": 1},
        {"request_id": "REQ-2", "status": "OK", "result": "heads"},
        {"request_id": "REQ-3", "status": "OK", "result": "HELLO"},
    ],
)
def test_valid_responses(payload: dict) -> None:
    validate_response(payload)


def test_error_response() -> None:
    validate_response(
        {"request_id": "REQ-1", "status": "ERROR", "message": "invalid sides"}
    )


def test_ok_must_not_have_message() -> None:
    with pytest.raises(ValueError):
        validate_response(
            {
                "request_id": "REQ-1",
                "status": "OK",
                "result": 4,
                "message": "invalid sides",
            }
        )


def test_error_must_not_have_result() -> None:
    with pytest.raises(ValueError):
        validate_response(
            {
                "request_id": "REQ-1",
                "status": "ERROR",
                "message": "invalid sides",
                "result": 4,
            }
        )


def test_response_schema_ok(response_schema: dict) -> None:
    validate(
        {"request_id": "REQ", "status": "OK", "result": 1},
        response_schema,
    )


@pytest.mark.parametrize(
    "payload,msg",
    [
        ({}, "request_id"),
        ({"request_id": "REQ", "status": "OK"}, "result"),
        ({"request_id": "REQ", "status": "ERROR"}, "message"),
    ],
)
def test_response_schema_error_message(
    payload: dict, msg: str, response_schema: dict
) -> None:
    assert_schema_invalid(payload, response_schema, msg)
