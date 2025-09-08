from __future__ import annotations

import dataclasses
from collections.abc import Generator, Iterator
from enum import StrEnum
from itertools import zip_longest
from typing import TYPE_CHECKING, Any, NamedTuple

if TYPE_CHECKING:
    import ast

__all__ = [
    "ArgKind",
    "ArgumentData",
    "AssignmentData",
    "BodyData",
    "ClassData",
    "Diff",
    "DiffKind",
    "FunctionArguments",
    "FunctionData",
    "Generator",
]


class ArgKind(StrEnum):
    POSITIONAL_ONLY = "POSITIONAL_ONLY"
    REGULAR = "REGULAR"
    KEYWORD_ONLY = "KEYWORD_ONLY"
    ARGS = "ARGS"
    KWARGS = "KWARGS"


@dataclasses.dataclass
class ArgumentData:
    name: str
    type: str | None
    kind: ArgKind


@dataclasses.dataclass
class ClassAttributeData:
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
    attributes: dict[str, ClassAttributeData] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class AssignmentData:
    name: str
    type: str | None


@dataclasses.dataclass
class BodyData:
    functions: dict[str, FunctionData] = dataclasses.field(default_factory=dict)
    classes: dict[str, ClassData] = dataclasses.field(default_factory=dict)
    assignments: dict[str, AssignmentData] = dataclasses.field(default_factory=dict)


class DiffKind(StrEnum):
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


class FunctionArguments(NamedTuple):
    posonlyargs: list[ast.arg]
    args: list[ast.arg]
    vararg: ast.arg | None
    kwonlyargs: list[ast.arg]
    kw_defaults: list[ast.expr | None]
    kwarg: ast.arg | None
    defaults: list[ast.expr]

    @classmethod
    def from_ast(cls, node: ast.FunctionDef) -> FunctionArguments:
        return cls(
            posonlyargs=node.args.posonlyargs,
            args=node.args.args,
            vararg=node.args.vararg,
            kwonlyargs=node.args.kwonlyargs,
            kw_defaults=node.args.kw_defaults,
            kwarg=node.args.kwarg,
            defaults=node.args.defaults,
        )

    @property
    def args_with_defaults(self) -> Iterator[tuple[ast.arg, ast.expr | None]]:
        return reversed(
            list(
                zip_longest(
                    reversed(self.posonlyargs + self.args),
                    reversed(self.defaults),
                )
            )
        )

    @property
    def kwargs_with_defaults(self) -> Iterator[tuple[ast.arg, ast.expr | None]]:
        return zip(self.kwonlyargs, self.kw_defaults, strict=False)
