import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter.jsonschema_lite import validate


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        sys.exit(result.returncode)


def run_optional(cmd: list[str]) -> None:
    try:
        run(cmd)
    except FileNotFoundError:
        print("skip:", " ".join(cmd), file=sys.stderr)


def verify_schemas() -> None:
    schema_root = ROOT / "schemas"
    response_schema = json.loads(
        (schema_root / "response.schema.json").read_text(encoding="utf-8")
    )
    narrative_schema = json.loads(
        (schema_root / "narrative.schema.json").read_text(encoding="utf-8")
    )
    validate(
        {"request_id": "REQ", "status": "OK", "result": 1},
        response_schema,
    )
    validate(
        {
            "class_name": "OBSERVATION",
            "request_id": "REQ",
            "text": "観測点",
        },
        narrative_schema,
    )


def main() -> None:
    verify_schemas()
    run_optional(["mypy", "adapter"])
    run([sys.executable, "-m", "pytest", "-q", "-o", "addopts="])


if __name__ == "__main__":
    main()
