from __future__ import annotations

from typing import TYPE_CHECKING

from .typing import Diff, DiffKind

if TYPE_CHECKING:
    from .typing import AssignmentData, ClassData, FunctionData, ModuleData


__all__ = [
    "get_diffs",
]


def get_diffs(old: ModuleData, new: ModuleData) -> list[Diff]:
    changes: list[Diff] = []

    changes += _diff_functions(old.functions, new.functions)
    changes += _diff_classes(old.classes, new.classes)
    changes += _diff_assignments(old.assignments, new.assignments)
    return changes


def _diff_functions(old: dict[str, FunctionData], new: dict[str, FunctionData]) -> list[Diff]:
    changes: list[Diff] = []
    function_names = set(old) | set(new)

    for function_name in function_names:
        if function_name in new and function_name not in old:
            changes.append(
                Diff(
                    kind=DiffKind.ADDITION,
                    old=None,
                    new=new[function_name],
                ),
            )
            continue

        if function_name in old and function_name not in new:
            changes.append(
                Diff(
                    kind=DiffKind.DELETION,
                    old=old[function_name],
                    new=None,
                ),
            )
            continue

        old_function = old[function_name]
        new_function = new[function_name]

        if old_function.return_type != new_function.return_type:
            changes.append(
                Diff(
                    kind=DiffKind.RETURN_TYPE_MODIFICATION,
                    old=old_function.return_type,
                    new=new_function.return_type,
                ),
            )

        if old_function.args != new_function.args:
            changes.append(
                Diff(
                    kind=DiffKind.ARGS_MODIFICATION,
                    old=old_function.args,
                    new=new_function.args,
                ),
            )

    return changes


def _diff_classes(old: dict[str, ClassData], new: dict[str, ClassData]) -> list[Diff]:
    changes: list[Diff] = []
    class_names = set(old) | set(new)

    for class_name in class_names:
        if class_name in new and class_name not in old:
            changes.append(
                Diff(
                    kind=DiffKind.ADDITION,
                    old=None,
                    new=new[class_name],
                ),
            )
            continue

        if class_name in old and class_name not in new:
            changes.append(
                Diff(
                    kind=DiffKind.DELETION,
                    old=old[class_name],
                    new=None,
                ),
            )
            continue

        old_class = old[class_name]
        new_class = new[class_name]

        changes += _diff_functions(old_class.body.functions, new_class.body.functions)
        changes += _diff_classes(old_class.body.classes, new_class.body.classes)
        changes += _diff_assignments(old_class.body.assignments, new_class.body.assignments)

    return changes


def _diff_assignments(old: dict[str, AssignmentData], new: dict[str, AssignmentData]) -> list[Diff]:
    changes: list[Diff] = []
    attribute_names = set(old) | set(new)

    for attribute_name in attribute_names:
        if attribute_name in new and attribute_name not in old:
            changes.append(
                Diff(
                    kind=DiffKind.ADDITION,
                    old=None,
                    new=new[attribute_name],
                ),
            )
            continue

        if attribute_name in old and attribute_name not in new:
            changes.append(
                Diff(
                    kind=DiffKind.DELETION,
                    old=old[attribute_name],
                    new=None,
                ),
            )
            continue

        old_assignment = old[attribute_name]
        new_assignment = new[attribute_name]

        if old_assignment.type != new_assignment.type:
            changes.append(
                Diff(
                    kind=DiffKind.TYPE_MODIFICATION,
                    old=old_assignment.type,
                    new=new_assignment.type,
                ),
            )

    return changes
