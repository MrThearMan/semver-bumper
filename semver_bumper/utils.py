from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from .typing import Generator

__all__ = [
    "get_module_path",
    "is_dunder_method",
    "is_internal_method",
    "logger",
]

logger = logging.getLogger(__name__)


def get_module_path(path: Path) -> str:
    """
    Get the module path for the given python file.
    Recurses up the directory tree until a path without a `__init__.py` file is found.

    :param path: The path to the python module file.
    """
    module = path.stem if path.stem != "__init__" else ""

    parent = path.parent
    while parent.name:
        if not (parent / "__init__.py").exists():
            break
        module = f"{parent.name}.{module}"
        parent = parent.parent

    return module.strip(".")


def is_internal_method(name: str) -> bool:
    """Is the given name an internal method?"""
    return name.startswith("_")


def is_dunder_method(name: str) -> bool:
    """Is the given name a dunder method?"""
    return name.startswith("__") and name.endswith("__")


def is_class_internal_method(name: str) -> bool:
    """Is the given name an internal method?"""
    parts = name.split(".")
    if len(parts) != 2:  # noqa: PLR2004
        return False
    return parts[0] == "self" and is_internal_method(parts[1])


def is_class_dunder_method(name: str) -> bool:
    """Is the given name an internal method?"""
    parts = name.split(".")
    if len(parts) != 2:  # noqa: PLR2004
        return False
    return parts[0] == "self" and is_dunder_method(parts[1])


def find_python_files(path: Path) -> Generator[Path, None, None]:
    """
    Find all python files in the given directory and its subdirectories.

    :param path: The base directory to start searching python files from.
    """
    for path_object in path.rglob("*.py"):
        if not path_object.is_file():
            continue

        yield path_object
