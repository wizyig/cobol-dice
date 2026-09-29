import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def request_schema() -> dict:
    return json.loads((ROOT / "schemas/request.schema.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def response_schema() -> dict:
    return json.loads((ROOT / "schemas/response.schema.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def narrative_schema() -> dict:
    return json.loads((ROOT / "schemas/narrative.schema.json").read_text(encoding="utf-8"))
