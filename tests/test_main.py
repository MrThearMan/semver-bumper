from pathlib import Path

from semver_bumper.main import find_diffs_from_previous_version
from semver_bumper.typing import ArgKind, ArgumentData, Diff, DiffKind

GIT_PATH = Path(__file__).parent / "example_git"


def test_find_diffs_from_previous_version():
    diffs = find_diffs_from_previous_version(GIT_PATH)
    assert diffs == {
        "example": [],
        "example.main": [
            Diff(
                kind=DiffKind.ARGS_MODIFICATION,
                old=[
                    ArgumentData(
                        name="name",
                        type="str",
                        kind=ArgKind.KEYWORD_ONLY,
                    ),
                    ArgumentData(
                        name="title",
                        type="str",
                        kind=ArgKind.KEYWORD_ONLY,
                    ),
                ],
                new=[
                    ArgumentData(
                        name="name",
                        type="str",
                        kind=ArgKind.KEYWORD_ONLY,
                    ),
                ],
            )
        ],
    }
