import pytest

from adapter.jsonschema_lite import ValidationError
from adapter.jsonschema_lite import validate
from adapter.schema import validate_request
from adapter.schema import validate_response


def test_request_not_dict() -> None:
    with pytest.raises(ValueError):
        validate_request("no")  # type: ignore[arg-type]


def test_request_empty_id() -> None:
    with pytest.raises(ValueError):
        validate_request({"request_id": "", "tool": "coin"})


def test_request_sides_bool() -> None:
    with pytest.raises(ValueError):
        validate_request({"request_id": "REQ", "tool": "dice", "sides": True})


def test_request_echo_not_str() -> None:
    with pytest.raises(ValueError):
        validate_request({"request_id": "REQ", "tool": "echo", "payload": 1})


def test_response_not_dict() -> None:
    with pytest.raises(ValueError):
        validate_response([])  # type: ignore[arg-type]


def test_lite_not_object() -> None:
    with pytest.raises(ValidationError):
        validate("x", {"type": "object", "properties": {}})


def test_lite_unsupported() -> None:
    with pytest.raises(ValidationError):
        validate(1, {"type": "array"})


def test_lite_string_type() -> None:
    with pytest.raises(ValidationError):
        validate({"a": 1}, {"type": "object", "properties": {"a": {"type": "string"}}})


def test_lite_string_maxlength() -> None:
    with pytest.raises(ValidationError):
        validate(
            {"a": "abcd"},
            {
                "type": "object",
                "properties": {"a": {"type": "string", "maxLength": 3}},
            },
        )


def test_lite_integer_type() -> None:
    with pytest.raises(ValidationError):
        validate({"n": "1"}, {"type": "object", "properties": {"n": {"type": "integer"}}})


def test_lite_integer_bool() -> None:
    with pytest.raises(ValidationError):
        validate({"n": True}, {"type": "object", "properties": {"n": {"type": "integer"}}})


def test_lite_const_fail() -> None:
    with pytest.raises(ValidationError):
        validate({"s": "X"}, {"type": "object", "properties": {"s": {"const": "OK"}}})


def test_lite_allof_if_false() -> None:
    schema = {
        "type": "object",
        "properties": {"tool": {"type": "string"}, "sides": {"type": "integer"}},
        "allOf": [
            {
                "if": {"properties": {"tool": {"const": "dice"}}},
                "then": {"required": ["sides"]},
            }
        ],
    }
    validate({"tool": "coin"}, schema)


def test_lite_oneof_ok_second() -> None:
    schema = {
        "oneOf": [
            {
                "type": "object",
                "required": ["a"],
                "properties": {"a": {"const": 1}},
            },
            {
                "type": "object",
                "required": ["b"],
                "properties": {"b": {"const": 2}},
            },
        ]
    }
    validate({"b": 2}, schema)
