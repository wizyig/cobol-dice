from typing import Any

ALLOWED_TOOLS: set[str] = {"dice", "coin", "timestamp", "echo"}

ERROR_MESSAGES: set[str] = {
    "invalid sides",
    "invalid payload",
    "invalid tool",
    "invalid request",
}


def validate_request(req: dict[str, Any]) -> None:
    if not isinstance(req, dict):
        raise ValueError("invalid request")
    request_id = req.get("request_id")
    if not isinstance(request_id, str) or request_id == "":
        raise ValueError("invalid request")
    if "tool" not in req:
        raise ValueError("invalid tool")
    tool = req["tool"]
    if tool not in ALLOWED_TOOLS:
        raise ValueError("invalid tool")
    if tool == "dice":
        sides = req.get("sides")
        if not isinstance(sides, int) or isinstance(sides, bool):
            raise ValueError("invalid sides")
        if sides < 2 or sides > 1000:
            raise ValueError("invalid sides")
    if tool == "echo":
        payload = req.get("payload")
        if not isinstance(payload, str):
            raise ValueError("invalid payload")
        if len(payload) < 1 or len(payload) > 80:
            raise ValueError("invalid payload")


def validate_response(resp: dict[str, Any]) -> None:
    if not isinstance(resp, dict):
        raise ValueError("invalid response")
    request_id = resp.get("request_id")
    if not isinstance(request_id, str) or request_id == "":
        raise ValueError("invalid response")
    status = resp.get("status")
    if status == "OK":
        if "result" not in resp:
            raise ValueError("missing result")
        if "message" in resp:
            raise ValueError("unexpected message")
        return
    if status == "ERROR":
        message = resp.get("message")
        if not isinstance(message, str):
            raise ValueError("missing message")
        if message not in ERROR_MESSAGES:
            raise ValueError("invalid message")
        if "result" in resp:
            raise ValueError("unexpected result")
        return
    raise ValueError("invalid status")
