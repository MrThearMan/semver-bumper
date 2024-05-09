from pathlib import Path

import pytest

from semver_bumper.utils import get_module_path, is_dunder_method, is_internal_method

BASE_DIR = Path(__file__).parent.parent


@pytest.mark.parametrize(
    ("path", "result"),
    [
        (BASE_DIR / "tests" / "example" / "arg_spec_functions.py", "tests.example.arg_spec_functions"),
        (BASE_DIR / "semver_bumper" / "main.py", "semver_bumper.main"),
        (BASE_DIR / "semver_bumper" / "__init__.py", "semver_bumper"),
    ],
)
def test_get_module_path(path: Path, result: bool):
    assert get_module_path(path) == result


@pytest.mark.parametrize(
    ("name", "result"),
    [
        ("a", False),
        ("_a", True),
        ("__a", True),
        ("a_", False),
        ("a__", False),
        ("__a_", True),
        ("_a__", True),
        ("__a__", True),
        ("__a__b", True),
        ("b__a__", False),
        ("__a_b__", True),
        ("__a___", True),
        ("___a__", True),
    ],
)
def test_is_internal_method(name: str, result: bool):
    assert is_internal_method(name) is result


@pytest.mark.parametrize(
    ("name", "result"),
    [
        ("a", False),
        ("_a", False),
        ("__a", False),
        ("a_", False),
        ("a__", False),
        ("__a_", False),
        ("_a__", False),
        ("__a__", True),
        ("__a__b", False),
        ("b__a__", False),
        ("__a_b__", True),
        ("__a___", True),
        ("___a__", True),
    ],
)
def test_is_dunder_method(name: str, result: bool):
    assert is_dunder_method(name) is result
