import re
from inspect import cleandoc
from pathlib import Path

import pytest

from semver_bumper.git import (
    find_file_contents_in_ref,
    find_initial_commit_hash,
    find_previous_version,
    has_new_commits_since_ref,
    resolve_ref,
)

GIT_PATH = Path(__file__).parent / "example_git"


def test_find_previous_version():
    result = find_previous_version(GIT_PATH)
    assert result == "v0.0.2"


def test_resolve_ref():
    result = resolve_ref("v0.0.2", GIT_PATH)
    assert result == "642a9d5fe4500decf7e3f27039494d378b8d5926"

    result = resolve_ref("642a9d5", GIT_PATH)
    assert result == "642a9d5fe4500decf7e3f27039494d378b8d5926"

    result = resolve_ref("642a9d5fe4500decf7e3f27039494d378b8d5926", GIT_PATH)
    assert result == "642a9d5fe4500decf7e3f27039494d378b8d5926"

    result = resolve_ref("HEAD", GIT_PATH)
    assert result == "acac2b50ea3556c236506f673ee99d246f4cf30e"

    result = resolve_ref("main", GIT_PATH)
    assert result == "acac2b50ea3556c236506f673ee99d246f4cf30e"


def test_has_new_commits_since_ref():
    assert has_new_commits_since_ref("v0.0.2", GIT_PATH) is True


def test_find_initial_commit_hash():
    result = find_initial_commit_hash(GIT_PATH)
    assert result == "5f59bd49778515bb0e62d8243fcf176468a8bc2a"


def test_find_file_contents_in_ref():
    result = find_file_contents_in_ref("v0.0.2", GIT_PATH / "example" / "main.py", GIT_PATH)
    assert result == cleandoc(
        """
        def main(*, name: str, title: str) -> None:
            print(f"Hello {title} {name}")
        """
    )
    result = find_file_contents_in_ref("v0.0.1", GIT_PATH / "example" / "main.py", GIT_PATH)
    assert result == cleandoc(
        """
        def main(name: str) -> None:
            print(f"Hello {name}")
        """
    )


def test_find_file_contents_in_ref__not_relative():
    msg = "File must be relative to the given directory"
    with pytest.raises(ValueError, match=re.escape(msg)):
        find_file_contents_in_ref("v0.0.2", GIT_PATH.parent / "nonexistent.py", GIT_PATH)
