from __future__ import annotations

from typing import TYPE_CHECKING

from semver_bumper.differ import get_diffs
from semver_bumper.git import find_file_contents_in_ref, find_previous_version, has_new_commits_since_ref
from semver_bumper.parser import parse_module_body
from semver_bumper.utils import find_python_files, get_module_path

if TYPE_CHECKING:
    from pathlib import Path

    from semver_bumper.typing import Diff


__all__ = [
    "find_diffs_from_previous_version",
]


def find_diffs_from_previous_version(directory: Path) -> dict[str, list[Diff]]:
    module_diffs: dict[str, list[Diff]] = {}

    version = find_previous_version(directory)
    if not has_new_commits_since_ref(version, directory):
        return module_diffs

    for file in find_python_files(directory):
        new_contents = find_file_contents_in_ref("HEAD", file, directory)
        old_contents = find_file_contents_in_ref(version, file, directory)

        old_data = parse_module_body(old_contents)
        new_data = parse_module_body(new_contents)

        name = get_module_path(file)
        module_diffs[name] = get_diffs(old_data, new_data)

    return module_diffs
