# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TraceIdTypeEvent(str, enum.Enum):
    LANGFUSE = "LANGFUSE"
    EXTERNAL = "EXTERNAL"

    def visit(self, langfuse: typing.Callable[[], T_Result], external: typing.Callable[[], T_Result]) -> T_Result:
        if self is TraceIdTypeEvent.LANGFUSE:
            return langfuse()
        if self is TraceIdTypeEvent.EXTERNAL:
            return external()
