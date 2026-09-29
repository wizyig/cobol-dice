"""MCP Adapter — dispatch by tool name. No business logic."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
COBOL_DIR = ROOT / "cobol"

TOOL_BIN = {
    "dice": COBOL_DIR / "DICE",
    "coin": COBOL_DIR / "COIN",
    "timestamp": COBOL_DIR / "TIMESTAMP",
    "echo": COBOL_DIR / "ECHO",
}

ALLOWED_MESSAGES = {
    "invalid sides",
    "invalid tool",
    "invalid request",
    "invalid payload",
}


class AdapterError(Exception):
    pass


def validate_surface(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise AdapterError("invalid request")
    if "request_id" not in payload or "tool" not in payload:
        raise AdapterError("invalid request")
    tool = str(payload["tool"])
    if tool not in TOOL_BIN:
        raise AdapterError("invalid tool")
    out: dict[str, Any] = {
        "request_id": str(payload["request_id"]),
        "tool": tool,
    }
    if tool == "dice":
        if "sides" not in payload:
            raise AdapterError("invalid request")
        out["sides"] = int(payload["sides"])
    if tool == "echo":
        if "payload" not in payload:
            raise AdapterError("invalid payload")
        out["payload"] = str(payload["payload"])
    return out


def call_cobol(request: dict[str, Any]) -> dict[str, Any]:
    binary = TOOL_BIN[request["tool"]]
    if not binary.exists():
        raise AdapterError("invalid request")
    proc = subprocess.run(
        [str(binary)],
        input=json.dumps(request),
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise AdapterError("invalid request")
    loaded: object = json.loads(proc.stdout)
    if not isinstance(loaded, dict):
        raise AdapterError("invalid request")
    return loaded


def handle(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        request = validate_surface(payload)
        return call_cobol(request)
    except AdapterError as exc:
        msg = str(exc) if str(exc) in ALLOWED_MESSAGES else "invalid request"
        rid = ""
        if isinstance(payload, dict):
            rid = str(payload.get("request_id", ""))
        return {"request_id": rid, "status": "ERROR", "message": msg}


if __name__ == "__main__":
    raw = json.load(sys.stdin)
    json.dump(handle(raw), sys.stdout, indent=2)
    sys.stdout.write("\n")
