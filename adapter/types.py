from typing import Literal
from typing import TypedDict
from typing import Union

ErrorMessage = Literal[
    "invalid sides",
    "invalid payload",
    "invalid request",
    "invalid tool",
]


class OkResponse(TypedDict):
    request_id: str
    status: Literal["OK"]
    result: object


class ErrorResponse(TypedDict):
    request_id: str
    status: Literal["ERROR"]
    message: ErrorMessage


Response = Union[OkResponse, ErrorResponse]

NarrativeClass = Literal["OBSERVATION", "ANOMALY", "RECOVERY"]


class Narrative(TypedDict):
    class_name: NarrativeClass
    request_id: str
    text: str


class RecoveryReport(TypedDict):
    request_id: str
    recovered: bool
    steps: int
    error_count: int
    ok_count: int
    recovery_count: int
    final_status: str
