from __future__ import annotations

import dataclasses
from enum import Enum
from typing import Any, Generator

__all__ = [
    "ArgumentData",
    "AssignmentData",
    "ClassData",
    "Diff",
    "FunctionData",
    "Generator",
]


@dataclasses.dataclass
class ArgumentData:
    name: str
    type: str | None


@dataclasses.dataclass
class FunctionData:
    name: str
    args: list[ArgumentData]
    return_type: str


@dataclasses.dataclass
class ClassData:
    name: str
    body: BodyData


@dataclasses.dataclass
class AssignmentData:
    name: str
    type: str | None


@dataclasses.dataclass
class BodyData:
    functions: dict[str, FunctionData] = dataclasses.field(default_factory=dict)
    classes: dict[str, ClassData] = dataclasses.field(default_factory=dict)
    assignments: dict[str, AssignmentData] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class ModuleData:
    name: str
    body: BodyData

    @property
    def functions(self) -> dict[str, FunctionData]:
        return self.body.functions

    @property
    def classes(self) -> dict[str, ClassData]:
        return self.body.classes

    @property
    def assignments(self) -> dict[str, AssignmentData]:
        return self.body.assignments


class DiffKind(str, Enum):
    ADDITION = "ADDITION"
    DELETION = "DELETION"
    RETURN_TYPE_MODIFICATION = "RETURN_TYPE_MODIFICATION"
    ARGS_MODIFICATION = "ARGS_MODIFICATION"
    TYPE_MODIFICATION = "TYPE_MODIFICATION"


@dataclasses.dataclass
class Diff:
    kind: DiffKind
    old: Any
    new: Any
