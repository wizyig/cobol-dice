import pytest
from adapter.jsonschema_lite import validate

from tests.helpers import assert_schema_invalid


def test_narrative_schema_ok(narrative_schema: dict) -> None:
    validate(
        {
            "class_name": "OBSERVATION",
            "request_id": "REQ-1",
            "text": "観測点。result=4 を記録した。",
        },
        narrative_schema,
    )


@pytest.mark.parametrize(
    "payload,msg",
    [
        ({}, "class_name"),
        (
            {"class_name": "OBSERVE", "request_id": "REQ", "text": "test"},
            "enum",
        ),
        (
            {"class_name": "OBSERVATION", "request_id": "REQ", "text": ""},
            "minLength",
        ),
        (
            {
                "class_name": "OBSERVATION",
                "request_id": "REQ",
                "text": "ok",
                "extra": "forbidden",
            },
            "additionalProperties",
        ),
    ],
)
def test_narrative_schema_failure(
    payload: dict, msg: str, narrative_schema: dict
) -> None:
    assert_schema_invalid(payload, narrative_schema, msg)
