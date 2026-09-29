from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_dice_examples() -> None:
    req = load("request/request.example.json")
    res = load("response/response.example.json")
    assert req["tool"] == "dice"
    assert res["status"] == "OK"
    assert 1 <= res["result"] <= req["sides"]


def test_coin_examples() -> None:
    req = load("request/coin.example.json")
    res = load("response/coin.example.json")
    assert req["tool"] == "coin"
    assert res["result"] in {"heads", "tails"}


def test_timestamp_examples() -> None:
    res = load("response/timestamp.example.json")
    assert "T" in res["result"]


def test_echo_examples() -> None:
    req = load("request/echo.example.json")
    res = load("response/echo.example.json")
    assert req["payload"] == res["result"]
