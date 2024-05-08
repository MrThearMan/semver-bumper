import re
from pathlib import Path

import pytest

from semver_bumper.git import (
    find_current_version,
    find_file_contents_in_ref,
    find_head,
    find_initial_commit_hash,
    find_previous_version,
)

GIT_PATH = Path(__file__).parent / "example_git"


def test_find_current_version():
    result = find_current_version(GIT_PATH)
    assert result == "v0.0.2"


def test_find_previous_version():
    result = find_previous_version(GIT_PATH)
    assert result == "v0.0.1"


def test_find_head():
    result = find_head(GIT_PATH)
    assert result == "4f4e1a43f0e81ccd73723adc4d23dda6a551b197"


def test_find_initial_commit_hash():
    result = find_initial_commit_hash(GIT_PATH)
    assert result == "c8aa3d587e4ec7fef5f4418cf6435e04134b0efa"


def test_find_file_contents_in_ref():
    result = find_file_contents_in_ref("v0.0.2", GIT_PATH / "empty", GIT_PATH)
    assert result == "foo bar baz"
    result = find_file_contents_in_ref("v0.0.1", GIT_PATH / "empty", GIT_PATH)
    assert result == "foo"


def test_find_file_contents_in_ref__file_not_found():
    msg = "File must be relative to the given directory"
    with pytest.raises(ValueError, match=re.escape(msg)):
        find_file_contents_in_ref("v0.0.2", GIT_PATH.parent / "empty", GIT_PATH)
