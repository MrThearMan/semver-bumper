from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING

from semver_bumper.utils import logger

if TYPE_CHECKING:
    from pathlib import Path

__all__ = [
    "find_current_version",
    "find_file_contents_in_ref",
    "find_head",
    "find_initial_commit_hash",
    "find_previous_version",
    "run_command",
]


def find_current_version(directory: Path) -> str | None:
    """Find the current tag version from the main branch in the given directory."""
    command = "git describe --tags --abbrev=0"
    return run_command(command, directory=directory)


def find_previous_version(directory: Path) -> str | None:
    """Find the previous tag (=before current) from the main branch in the given directory."""
    cur = find_current_version(directory)
    if cur is None:
        return None
    command = f"git describe --tags --abbrev=0 {cur}~"
    return run_command(command, directory=directory)


def find_head(directory: Path) -> str | None:
    """Find the current HEAD commit hash from the main branch in the given directory."""
    command = "git rev-parse HEAD"
    return run_command(command, directory=directory)


def find_initial_commit_hash(directory: Path) -> str | None:
    """Find the initial commit hash of the main branch in the given git directory."""
    command = "git rev-list --max-parents=0 HEAD"
    return run_command(command, directory=directory)


def find_file_contents_in_ref(ref: str, file: Path, directory: Path) -> str | None:
    """Find the initial commit hash of the main branch in the given git directory."""
    try:
        path = file.relative_to(directory)
    except ValueError as error:
        msg = "File must be relative to the given directory"
        raise ValueError(msg) from error

    command = f"git show {ref}:{path!s}"
    return run_command(command, directory=directory)


def run_command(command: str, *, directory: Path | None = None) -> str | None:
    """Run a command in the given directory using subprocess."""
    process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory)
    stdout, stderr = process.communicate()

    error = stderr.decode()
    if error:
        logger.error(error)
        return None

    return stdout.decode().strip()
