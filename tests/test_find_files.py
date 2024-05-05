from pathlib import Path

from semver_bumper.utils import find_python_files


def test_find_python_files():
    directory = Path(__file__).parent / "example"

    expected = [
        directory / "arg_spec_functions.py",
        directory / "utils.py",
        directory / "utils_2.py",
        directory / "__init__.py",
        directory / "package" / "main.py",
        directory / "package" / "module.py",
        directory / "package" / "__init__.py",
    ]

    actual = find_python_files(directory)

    for file in actual:
        assert file in expected
