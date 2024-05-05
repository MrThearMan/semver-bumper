from dataclasses import asdict
from pathlib import Path

from semver_bumper.differ import get_diffs
from semver_bumper.parser import parse_module
from semver_bumper.typing import DiffKind


def test_compare_files():
    directory = Path(__file__).parent / "example"
    file_1 = directory / "utils.py"
    file_2 = directory / "utils_2.py"

    modle_1 = parse_module(file_1)
    modle_2 = parse_module(file_2)

    diffs = get_diffs(modle_1, modle_2)
    data = [asdict(diff) for diff in diffs]
    assert data == [
        {
            "kind": DiffKind.RETURN_TYPE_MODIFICATION,
            "new": "str",
            "old": "int",
        },
        {
            "kind": DiffKind.ARGS_MODIFICATION,
            "new": [
                {"name": "a", "type": "str"},
                {
                    "name": "b",
                    "type": "str",
                },
            ],
            "old": [
                {"name": "a", "type": "int"},
                {
                    "name": "b",
                    "type": "int",
                },
            ],
        },
    ]
