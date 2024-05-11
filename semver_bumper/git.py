from __future__ import annotations

import subprocess
from typing import TYPE_CHECKING

from semver_bumper.utils import logger

if TYPE_CHECKING:
    from pathlib import Path

__all__ = [
    "find_file_contents_in_ref",
    "find_initial_commit_hash",
    "find_previous_version",
    "has_new_commits_since_ref",
    "run_command",
]


def find_previous_version(directory: Path) -> str:
    """
    Find the ref for the previous version based on tags.
    If there are no tags in the history, use the initial commit hash.

    :param directory: The directory to run the command in.
    """
    command = "git describe --tags --abbrev=0"
    result = run_command(command, directory=directory)
    if result is None:
        return find_initial_commit_hash(directory)
    return result


def find_initial_commit_hash(directory: Path) -> str:
    """
    Find the initial commit hash for a git repository.

    :param directory: The directory to run the command in.
    :raises LookupError: No git respository, or no commits in the repository.
    """
    command = "git rev-list --max-parents=0 HEAD"
    result = run_command(command, directory=directory)
    if result is None:
        msg = "Could not find initial commit hash"
        raise LookupError(msg)
    return result


def find_file_contents_in_ref(ref: str, file: Path, directory: Path) -> str | None:
    """
    Get the file contents of the given file in the given ref.

    :param ref: The git reference to get the file contents from.
    :param file: The file to get the contents of. Should be relative to `directory`.
    :param directory: The directory to run the command in.
    :raises ValueError: The file is not relative to the given directory.
    """
    try:
        path = file.relative_to(directory).as_posix()
    except ValueError as error:
        msg = "File must be relative to the given directory"
        raise ValueError(msg) from error

    command = f"git show {ref}:{path!s}"
    return run_command(command, directory=directory)


def has_new_commits_since_ref(ref: str, directory: Path) -> bool:
    """
    Have been there any new commits since the given ref?

    :param ref: The git reference to check for new commits since.
    :param directory: The directory to run the command in.
    """
    ref = resolve_ref(ref, directory)
    head = resolve_ref("HEAD", directory)
    return ref != head


def resolve_ref(ref: str, directory: Path) -> str | None:
    """
    Resolves aliases for a git reference to their commit hash.
    E.g., tags, branches, short commit hashes, etc.

    :param ref: The git reference to resolve.
    :param directory: The directory to run the command in.
    """
    command = f"git rev-parse {ref}"
    return run_command(command, directory=directory)


def run_command(command: str, *, directory: Path | None = None) -> str | None:
    """
    Run a command in the given directory using subprocess.
    Return the stdout of the command if it succeeds, otherwise return None and log the error.

    :param command: The command string to run.
    :param directory: The directory to run the command in.
    """
    process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory)
    stdout, stderr = process.communicate()

    error = stderr.decode()
    if error:
        logger.error(error)
        return None

    return stdout.decode().strip()
