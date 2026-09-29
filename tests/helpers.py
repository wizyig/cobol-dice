from typing import Any

import pytest

from adapter.jsonschema_lite import ValidationError
from adapter.jsonschema_lite import validate


def assert_schema_invalid(
    payload: dict[str, Any],
    schema: dict[str, Any],
    contains: str | None = None,
) -> None:
    with pytest.raises(ValidationError) as exc:
        validate(instance=payload, schema=schema)
    if contains is not None:
        assert contains in str(exc.value)
