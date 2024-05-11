from dataclasses import asdict
from itertools import count
from pathlib import Path

from semver_bumper.parser import parse_module_body
from semver_bumper.typing import ArgKind

TESTS_DIR = Path(__file__).parent


def func_name():
    counter = count(2)
    while True:
        yield f"function_{str(next(counter) // 2).zfill(2)}"


def test_parse_file() -> None:
    path = TESTS_DIR / "example" / "arg_spec_functions.py"

    module_body = parse_module_body(path.read_text())
    results = asdict(module_body)

    assert results["assignments"] == {}

    assert results["classes"]["Foo"] == {
        "name": "Foo",
        "body": {
            "assignments": {
                "name": {
                    "name": "name",
                    "type": "str",
                },
                "age": {
                    "name": "age",
                    "type": "int",
                },
            },
            "classes": {},
            "functions": {},
        },
        "attributes": {},
    }
    assert results["classes"]["Bar"] == {
        "name": "Bar",
        "body": {
            "assignments": {
                "item": {
                    "name": "item",
                    "type": "Foo",
                },
                "things": {
                    "name": "things",
                    "type": "list[Foo]",
                },
                "other": {
                    "name": "other",
                    "type": "dict[str, Foo]",
                },
            },
            "classes": {},
            "functions": {},
        },
        "attributes": {},
    }
    assert results["classes"]["Barr"] == {
        "name": "Barr",
        "body": {
            "assignments": {
                "item": {
                    "name": "item",
                    "type": "Foo",
                },
                "things": {
                    "name": "things",
                    "type": "list[Foo]",
                },
                "other": {
                    "name": "other",
                    "type": "dict[str, Foo]",
                },
            },
            "classes": {},
            "functions": {},
        },
        "attributes": {},
    }
    assert results["classes"]["Baz"] == {
        "name": "Baz",
        "body": {
            "assignments": {
                "weird": {
                    "name": "weird",
                    "type": "Bar",
                },
                "nested": {
                    "name": "nested",
                    "type": "list[dict[str, Bar]]",
                },
                "another": {
                    "name": "another",
                    "type": "dict[str, list[Bar]]",
                },
            },
            "classes": {},
            "functions": {},
        },
        "attributes": {},
    }
    assert results["classes"]["Bazz"] == {
        "name": "Bazz",
        "body": {
            "assignments": {
                "weird": {
                    "name": "weird",
                    "type": "Barr",
                },
                "nested": {
                    "name": "nested",
                    "type": "list[dict[str, Barr]]",
                },
                "another": {
                    "name": "another",
                    "type": "dict[str, list[Barr]]",
                },
            },
            "classes": {},
            "functions": {},
        },
        "attributes": {},
    }
    assert results["classes"]["Fizz"] == {
        "name": "Fizz",
        "body": {
            "assignments": {
                "union": {
                    "name": "union",
                    "type": "int | float",
                },
                "optional": {
                    "name": "optional",
                    "type": "str | None",
                },
            },
            "classes": {},
            "functions": {},
        },
        "attributes": {},
    }
    assert results["classes"]["Buzz"] == {
        "name": "Buzz",
        "body": {
            "assignments": {
                "not_available": {
                    "name": "not_available",
                    "type": "TestType",
                },
            },
            "classes": {},
            "functions": {},
        },
        "attributes": {},
    }
    assert results["classes"]["Class_1"] == {
        "name": "Class_1",
        "body": {
            "assignments": {
                "foo": {
                    "name": "foo",
                    "type": "int",
                },
            },
            "classes": {
                "Class_2": {
                    "name": "Class_2",
                    "body": {
                        "assignments": {
                            "foo": {
                                "name": "foo",
                                "type": "dict[int | str, str | list[int]]",
                            }
                        },
                        "classes": {},
                        "functions": {},
                    },
                    "attributes": {},
                }
            },
            "functions": {
                "__init__": {
                    "name": "__init__",
                    "args": [
                        {
                            "name": "self",
                            "type": None,
                            "kind": ArgKind.REGULAR,
                        },
                        {
                            "name": "bar",
                            "type": "Bar",
                            "kind": ArgKind.REGULAR,
                        },
                    ],
                    "return_type": "None",
                },
                "method": {
                    "name": "method",
                    "args": [
                        {
                            "name": "self",
                            "type": None,
                            "kind": ArgKind.REGULAR,
                        },
                        {
                            "name": "foo",
                            "type": "int",
                            "kind": ArgKind.REGULAR,
                        },
                    ],
                    "return_type": "None",
                },
                "classmethod": {
                    "name": "classmethod",
                    "args": [
                        {
                            "name": "cls",
                            "type": None,
                            "kind": ArgKind.REGULAR,
                        },
                        {
                            "name": "foo",
                            "type": "int",
                            "kind": ArgKind.REGULAR,
                        },
                    ],
                    "return_type": "None",
                },
                "staticmethod": {
                    "name": "staticmethod",
                    "args": [
                        {
                            "name": "foo",
                            "type": "int",
                            "kind": ArgKind.REGULAR,
                        },
                    ],
                    "return_type": "None",
                },
                "property": {
                    "name": "property",
                    "args": [
                        {
                            "name": "self",
                            "type": None,
                            "kind": ArgKind.REGULAR,
                        },
                    ],
                    "return_type": "None",
                },
            },
        },
        "attributes": {
            "bar": {
                "name": "bar",
                "type": "Bar",
            },
        },
    }

    name = func_name()

    # 1 - 10
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }

    # 11 - 20
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }

    # 21 - 30
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }

    # 31 - 40
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }

    # 41 - 50
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": None,
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": None,
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }

    # 51 - 60
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "args",
                "type": "int",
                "kind": ArgKind.ARGS,
            },
            {
                "name": "kwargs",
                "type": "int",
                "kind": ArgKind.KWARGS,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }

    # 61 - 70
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.KEYWORD_ONLY,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": None,
                "kind": ArgKind.POSITIONAL_ONLY,
            },
            {
                "name": "age",
                "type": None,
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.POSITIONAL_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "float",
                "kind": ArgKind.POSITIONAL_ONLY,
            },
            {
                "name": "age",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "name",
                "type": "int",
                "kind": ArgKind.POSITIONAL_ONLY,
            },
            {
                "name": "age",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "str",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }

    # 71 - 80
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "float",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "bool",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "dict",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "list",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "date",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "datetime",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "time",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "timedelta",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "Decimal",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "type",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }

    # 81 - 90
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "x",
                "type": "Exception",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Foo",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Fizz",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Bar",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Barr",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Baz",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Bazz",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Foo",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Fizz",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Bar",
    }

    # 91 - 100
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Barr",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Baz",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Bazz",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Foo",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Foo",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "list[Foo]",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "dict[str, Foo]",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "Buzz",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Buzz",
    }
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [
            {
                "name": "foo",
                "type": "str | int",
                "kind": ArgKind.REGULAR,
            },
        ],
        "return_type": "None",
    }

    # 101 - 110
    assert results["functions"][next(name)] == {
        "name": next(name),
        "args": [],
        "return_type": "Foo | Bar",
    }
