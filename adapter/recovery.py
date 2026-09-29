from typing import Any
from typing import Sequence

from adapter.schema import validate_response
from adapter.types import RecoveryReport


def analyze_recovery(events: Sequence[dict[str, Any]]) -> RecoveryReport:
    if len(events) == 0:
        raise ValueError("empty sequence")
    for event in events:
        validate_response(event)
    request_id = str(events[0]["request_id"])
    for event in events:
        if event["request_id"] != request_id:
            raise ValueError("mixed request_id")
    error_count = sum(1 for e in events if e["status"] == "ERROR")
    ok_count = sum(1 for e in events if e["status"] == "OK")
    recovery_count = 0
    previous: str | None = None
    for event in events:
        current = str(event["status"])
        if previous == "ERROR" and current == "OK":
            recovery_count += 1
        previous = current
    final_status = str(events[-1]["status"])
    return {
        "request_id": request_id,
        "recovered": error_count > 0 and final_status == "OK",
        "steps": len(events),
        "error_count": error_count,
        "ok_count": ok_count,
        "recovery_count": recovery_count,
        "final_status": final_status,
    }
