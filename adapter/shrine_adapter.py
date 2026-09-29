from typing import Any
from typing import Sequence

from adapter.schema import validate_response
from adapter.types import Narrative


def transform(event: dict[str, Any]) -> Narrative:
    validate_response(event)
    request_id = str(event["request_id"])
    if event["status"] == "OK":
        return {
            "class_name": "OBSERVATION",
            "request_id": request_id,
            "text": f"観測点。result={event['result']} を記録した。",
        }
    return {
        "class_name": "ANOMALY",
        "request_id": request_id,
        "text": f"異常観測点。{event['message']} を記録した。",
    }


def transform_sequence(events: Sequence[dict[str, Any]]) -> Narrative:
    if len(events) == 0:
        raise ValueError("empty sequence")
    for event in events:
        validate_response(event)
    first = events[0]
    last = events[-1]
    if (
        first["status"] == "ERROR"
        and last["status"] == "OK"
        and first["request_id"] == last["request_id"]
    ):
        return {
            "class_name": "RECOVERY",
            "request_id": str(first["request_id"]),
            "text": "再観測成功。復旧を確認した。",
        }
    return transform(last)
