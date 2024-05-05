from __future__ import annotations

import ast
import json
from itertools import zip_longest
from typing import TYPE_CHECKING

from .typing import ArgumentData, AssignmentData, BodyData, ClassData, FunctionData, ModuleData
from .utils import get_module_path, is_dunder_method, is_internal_method

if TYPE_CHECKING:
    from pathlib import Path

__all__ = [
    "parse_module",
]


def parse_module(path: Path) -> ModuleData:
    module: ast.Module = ast.parse(path.read_text())
    return ModuleData(
        name=get_module_path(path),
        body=_parse_body(module.body, dunder_all=_get_dunder_all(module)),
    )


def _get_dunder_all(module: ast.Module) -> list[str] | None:
    for node in module.body:
        if isinstance(node, ast.Assign):
            name = _node_to_string(node.targets[0])
            if name == "__all__":
                return json.loads(_node_to_string(node.value).replace("'", '"'))
    return None


def _parse_body(nodes: list[ast.stmt], *, dunder_all: list[str] | None = None) -> BodyData:
    body = BodyData()

    for node in nodes:
        if isinstance(node, ast.FunctionDef) and _should_include_function(node, dunder_all):
            name = node.name
            body.functions[name] = FunctionData(
                name=name,
                args=_get_argument_data(node),
                return_type=_node_to_string(node.returns),
            )

        elif isinstance(node, ast.ClassDef) and _should_include_class(node, dunder_all):
            name = node.name
            body.classes[name] = ClassData(
                name=name,
                body=_parse_body(node.body),
            )

        elif isinstance(node, ast.Assign) and _should_include_assignment(node, dunder_all):
            name = _node_to_string(node.targets[0])
            body.assignments[name] = AssignmentData(
                name=name,
                type=_infer_type_for_node(node.value),
            )

        elif isinstance(node, ast.AnnAssign) and _should_include_ann_assignment(node, dunder_all):
            name = _node_to_string(node.target)
            body.assignments[name] = AssignmentData(
                name=name,
                type=_node_to_string(node.annotation),
            )

    return body


def _get_argument_data(node: ast.FunctionDef) -> list[ArgumentData]:
    args = [
        ArgumentData(
            name=arg.arg,
            type=_node_to_string(arg.annotation) if arg.annotation is not None else _infer_type_for_node(default),
        )
        for arg, default in zip_longest(reversed(node.args.args), reversed(node.args.defaults))
    ]
    args.reverse()
    return args


def _should_include_function(node: ast.FunctionDef, dunder_all: list[str] | None) -> bool:
    name = node.name
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _should_include_class(node: ast.ClassDef, dunder_all: list[str] | None) -> bool:
    name = node.name
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _should_include_assignment(node: ast.Assign, dunder_all: list[str] | None) -> bool:
    name = _node_to_string(node.targets[0])
    if name == "__all__":
        return False
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _should_include_ann_assignment(node: ast.AnnAssign, dunder_all: list[str] | None) -> bool:
    name = _node_to_string(node.target)
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _node_to_string(node: ast.expr | None) -> str | None:
    if node is None:
        return None
    return ast.unparse(node)


def _infer_type_for_node(node: ast.expr | None) -> str | None:  # noqa: PLR0911
    if node is None:
        return None

    if isinstance(node, ast.Constant):
        return type(node.value).__name__

    if isinstance(node, ast.List):
        subtypes = _infer_types_for_nodes(node.elts)
        return f"list[{subtypes}]"

    if isinstance(node, ast.Tuple):
        subtypes = _infer_types_for_nodes(node.elts)
        return f"tuple[{subtypes}]"

    if isinstance(node, ast.Set):
        subtypes = _infer_types_for_nodes(node.elts)
        return f"set[{subtypes}]"

    if isinstance(node, ast.Dict):
        keys = _infer_types_for_nodes(node.keys)
        values = _infer_types_for_nodes(node.values)
        return f"dict[{keys}, {values}]"

    return _node_to_string(node)


def _infer_types_for_nodes(nodes: list[ast.expr]) -> str:
    subtypes: list[str] = []
    for node in nodes:
        subtype = _infer_type_for_node(node)
        if subtype not in subtypes:
            subtypes.append(subtype)
    if not subtypes:
        return "Any"
    return " | ".join(subtypes)
