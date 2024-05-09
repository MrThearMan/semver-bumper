from __future__ import annotations

import ast
import json

from .typing import ArgKind, ArgumentData, AssignmentData, BodyData, ClassData, FunctionArguments, FunctionData
from .utils import is_dunder_method, is_internal_method

__all__ = [
    "parse_module_body",
]


def parse_module_body(contents: str) -> BodyData:
    """
    Parse the given python file contents into the required data for version diffing.

    :param contents: The contents of the python file.
    """
    module: ast.Module = ast.parse(contents)
    return _parse_body(module.body, dunder_all=_get_dunder_all(module))


def _get_dunder_all(module: ast.Module) -> list[str] | None:
    """Find the __all__ attribute in the given module, if it exists."""
    for node in module.body:
        if isinstance(node, ast.Assign):
            name = _node_to_string(node.targets[0])
            if name == "__all__":
                return json.loads(_node_to_string(node.value).replace("'", '"'))
    return None


def _parse_body(nodes: list[ast.stmt], *, dunder_all: list[str] | None = None) -> BodyData:
    """Parse the list of ast statements in an object body (e.g., module/class) into diffing data."""
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
    """Get the argument data for a function definition."""
    data: list[ArgumentData] = []
    arguments = FunctionArguments.from_ast(node)

    for arg, default in arguments.args_with_defaults:
        data.append(
            ArgumentData(
                name=arg.arg,
                type=_node_to_string(arg.annotation) if arg.annotation is not None else _infer_type_for_node(default),
                kind=ArgKind.POSITIONAL_ONLY if arg in arguments.posonlyargs else ArgKind.REGULAR,
            )
        )

    if arguments.vararg is not None:
        data.append(
            ArgumentData(
                name=arguments.vararg.arg,
                type=_node_to_string(arguments.vararg.annotation),
                kind=ArgKind.ARGS,
            )
        )

    for arg, default in arguments.kwargs_with_defaults:
        data.append(
            ArgumentData(
                name=arg.arg,
                type=_node_to_string(arg.annotation) if arg.annotation is not None else _infer_type_for_node(default),
                kind=ArgKind.KEYWORD_ONLY,
            )
        )

    if arguments.kwarg is not None:
        data.append(
            ArgumentData(
                name=arguments.kwarg.arg,
                type=_node_to_string(arguments.kwarg.annotation),
                kind=ArgKind.KWARGS,
            )
        )

    return data


def _should_include_function(node: ast.FunctionDef, dunder_all: list[str] | None) -> bool:
    """Should the given function definition be included in the diffing data?"""
    name = node.name
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _should_include_class(node: ast.ClassDef, dunder_all: list[str] | None) -> bool:
    """Should the given class definition be included in the diffing data?"""
    name = node.name
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _should_include_assignment(node: ast.Assign, dunder_all: list[str] | None) -> bool:
    """Should the given assignment be included in the diffing data?"""
    name = _node_to_string(node.targets[0])
    if name == "__all__":
        return False
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _should_include_ann_assignment(node: ast.AnnAssign, dunder_all: list[str] | None) -> bool:
    """Should the given annotated assignment be included in the diffing data?"""
    name = _node_to_string(node.target)
    if dunder_all is not None:
        return name in dunder_all
    return not is_internal_method(name) or is_dunder_method(name)


def _node_to_string(node: ast.expr | None) -> str | None:
    """Convert the given ast node to a string."""
    if node is None:
        return None
    return ast.unparse(node)


def _infer_type_for_node(node: ast.expr | None) -> str | None:  # noqa: PLR0911
    """Infer the type for the given ast node."""
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
    """Infer the types for the given list of ast nodes."""
    subtypes: list[str] = []
    for node in nodes:
        subtype = _infer_type_for_node(node)
        if subtype not in subtypes:
            subtypes.append(subtype)
    if not subtypes:
        return "Any"
    return " | ".join(subtypes)
