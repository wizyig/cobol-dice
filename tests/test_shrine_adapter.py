from adapter.jsonschema_lite import validate

from adapter.shrine_adapter import transform


def test_observation(narrative_schema: dict) -> None:
    result = transform({"request_id": "REQ-1", "status": "OK", "result": 6})
    assert result["class_name"] == "OBSERVATION"
    assert result["request_id"] == "REQ-1"
    assert "6" in result["text"]
    validate(result, narrative_schema)


def test_anomaly() -> None:
    result = transform(
        {"request_id": "REQ-1", "status": "ERROR", "message": "invalid payload"}
    )
    assert result["class_name"] == "ANOMALY"
    assert "invalid payload" in result["text"]


def test_narrative_keys() -> None:
    result = transform({"request_id": "REQ-1", "status": "OK", "result": 6})
    assert set(result.keys()) == {"class_name", "request_id", "text"}
    assert result["text"] != ""
