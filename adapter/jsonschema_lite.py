"""Minimal JSON Schema checks for the three frozen schemas. No jsonschema dep."""

from typing import Any


class ValidationError(ValueError):
    pass


def validate(instance: Any, schema: dict[str, Any]) -> None:
    if "oneOf" in schema:
        errors: list[str] = []
        for option in schema["oneOf"]:
            try:
                validate(instance, option)
                return
            except ValidationError as exc:
                errors.append(str(exc))
        raise ValidationError("oneOf failed: " + "; ".join(errors))
    if schema.get("type") == "object":
        if not isinstance(instance, dict):
            raise ValidationError("not object")
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                raise ValidationError(key)
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(instance) - set(props)
            if extra:
                raise ValidationError("additionalProperties")
        for key, value in instance.items():
            if key in props:
                _validate_prop(value, props[key], key)
        for clause in schema.get("allOf", []):
            if_clause = clause.get("if")
            then_clause = clause.get("then")
            if if_clause and then_clause and _matches_if(instance, if_clause):
                for key in then_clause.get("required", []):
                    if key not in instance:
                        raise ValidationError(key)
        return
    raise ValidationError("unsupported schema")


def _matches_if(instance: dict[str, Any], if_clause: dict[str, Any]) -> bool:
    props = if_clause.get("properties", {})
    for key, spec in props.items():
        if "const" in spec and instance.get(key) != spec["const"]:
            return False
    return True


def _validate_prop(value: Any, spec: dict[str, Any], key: str) -> None:
    if "const" in spec and value != spec["const"]:
        raise ValidationError(key)
    if "enum" in spec and value not in spec["enum"]:
        raise ValidationError("enum")
    if spec.get("type") == "string":
        if not isinstance(value, str):
            raise ValidationError(key)
        if "minLength" in spec and len(value) < spec["minLength"]:
            raise ValidationError("minLength")
        if "maxLength" in spec and len(value) > spec["maxLength"]:
            raise ValidationError("maxLength")
    if spec.get("type") == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValidationError(key)
        if "minimum" in spec and value < spec["minimum"]:
            raise ValidationError("minimum")
        if "maximum" in spec and value > spec["maximum"]:
            raise ValidationError("maximum")
