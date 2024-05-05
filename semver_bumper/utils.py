from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from .typing import Generator

__all__ = [
    "get_module_path",
    "is_dunder_method",
    "is_internal_method",
]


def get_module_path(path: Path) -> str:
    module = path.stem

    parent = path.parent
    while parent.name:
        if not (parent / "__init__.py").exists():
            break
        module = f"{parent.name}.{module}"
        parent = parent.parent

    return module


def is_internal_method(name: str) -> bool:
    return name.startswith("_")


def is_dunder_method(name: str) -> bool:
    return name.startswith("__") and name.endswith("__")


def find_python_files(base_path: Path) -> Generator[Path, None, None]:
    for path_object in base_path.rglob("*.py"):
        if not path_object.is_file():
            continue

        yield path_object
