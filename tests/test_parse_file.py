from dataclasses import asdict
from pathlib import Path

from semver_bumper.parser import parse_module


def test_parse_file() -> None:
    directory = Path(__file__).parent / "example"
    path = directory / "arg_spec_functions.py"

    module_data = parse_module(path)

    assert asdict(module_data) == {
        "name": "tests.example.arg_spec_functions",
        "body": {
            "assignments": {},
            "classes": {
                "Foo": {
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
                },
                "Bar": {
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
                },
                "Barr": {
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
                },
                "Baz": {
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
                },
                "Bazz": {
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
                },
                "Fizz": {
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
                },
                "Buzz": {
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
                },
                "Class_1": {
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
                            }
                        },
                        "functions": {
                            "__init__": {
                                "name": "__init__",
                                "args": [
                                    {
                                        "name": "self",
                                        "type": None,
                                    },
                                    {
                                        "name": "foo",
                                        "type": "Foo",
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
                                    },
                                    {
                                        "name": "foo",
                                        "type": "int",
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
                                    },
                                    {
                                        "name": "foo",
                                        "type": "int",
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
                                    },
                                ],
                                "return_type": "None",
                            },
                        },
                    },
                },
            },
            "functions": {
                "function_01": {
                    "name": "function_01",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                        {
                            "name": "age",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_02": {
                    "name": "function_02",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                        {
                            "name": "age",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_03": {
                    "name": "function_03",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                        {
                            "name": "age",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_04": {
                    "name": "function_04",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                        {
                            "name": "age",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_05": {
                    "name": "function_05",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                        {
                            "name": "age",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_06": {
                    "name": "function_06",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                        {
                            "name": "age",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_07": {
                    "name": "function_07",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                        {
                            "name": "age",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_08": {
                    "name": "function_08",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                        {
                            "name": "age",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_09": {
                    "name": "function_09",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                        {
                            "name": "age",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_10": {
                    "name": "function_10",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                        {
                            "name": "age",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_11": {
                    "name": "function_11",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                        {
                            "name": "age",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_12": {
                    "name": "function_12",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                        {
                            "name": "age",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_13": {
                    "name": "function_13",
                    "args": [],
                    "return_type": "None",
                },
                "function_14": {
                    "name": "function_14",
                    "args": [],
                    "return_type": "None",
                },
                "function_15": {
                    "name": "function_15",
                    "args": [],
                    "return_type": "None",
                },
                "function_16": {
                    "name": "function_16",
                    "args": [],
                    "return_type": "None",
                },
                "function_17": {
                    "name": "function_17",
                    "args": [],
                    "return_type": "None",
                },
                "function_18": {
                    "name": "function_18",
                    "args": [],
                    "return_type": "None",
                },
                "function_19": {
                    "name": "function_19",
                    "args": [],
                    "return_type": "None",
                },
                "function_20": {
                    "name": "function_20",
                    "args": [],
                    "return_type": "None",
                },
                "function_21": {
                    "name": "function_21",
                    "args": [],
                    "return_type": "None",
                },
                "function_22": {
                    "name": "function_22",
                    "args": [],
                    "return_type": "None",
                },
                "function_23": {
                    "name": "function_23",
                    "args": [],
                    "return_type": "None",
                },
                "function_24": {
                    "name": "function_24",
                    "args": [],
                    "return_type": "None",
                },
                "function_25": {
                    "name": "function_25",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_26": {
                    "name": "function_26",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_27": {
                    "name": "function_27",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_28": {
                    "name": "function_28",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_29": {
                    "name": "function_29",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_30": {
                    "name": "function_30",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_31": {
                    "name": "function_31",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_32": {
                    "name": "function_32",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_33": {
                    "name": "function_33",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_34": {
                    "name": "function_34",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_35": {
                    "name": "function_35",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_36": {
                    "name": "function_36",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_37": {
                    "name": "function_37",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_38": {
                    "name": "function_38",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_39": {
                    "name": "function_39",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_40": {
                    "name": "function_40",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_41": {
                    "name": "function_41",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_42": {
                    "name": "function_42",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_43": {
                    "name": "function_43",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_44": {
                    "name": "function_44",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_45": {
                    "name": "function_45",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_46": {
                    "name": "function_46",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_47": {
                    "name": "function_47",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_48": {
                    "name": "function_48",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_49": {
                    "name": "function_49",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_50": {
                    "name": "function_50",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_51": {
                    "name": "function_51",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_52": {
                    "name": "function_52",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_53": {
                    "name": "function_53",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_54": {
                    "name": "function_54",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_55": {
                    "name": "function_55",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_56": {
                    "name": "function_56",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_57": {
                    "name": "function_57",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_58": {
                    "name": "function_58",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_59": {
                    "name": "function_59",
                    "args": [
                        {
                            "name": "name",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_60": {
                    "name": "function_60",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_61": {
                    "name": "function_61",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_62": {
                    "name": "function_62",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_63": {
                    "name": "function_63",
                    "args": [
                        {
                            "name": "name",
                            "type": None,
                        },
                    ],
                    "return_type": "None",
                },
                "function_64": {
                    "name": "function_64",
                    "args": [
                        {
                            "name": "name",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_65": {
                    "name": "function_65",
                    "args": [
                        {
                            "name": "x",
                            "type": "str",
                        },
                    ],
                    "return_type": "None",
                },
                "function_66": {
                    "name": "function_66",
                    "args": [
                        {
                            "name": "x",
                            "type": "int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_67": {
                    "name": "function_67",
                    "args": [
                        {
                            "name": "x",
                            "type": "float",
                        },
                    ],
                    "return_type": "None",
                },
                "function_68": {
                    "name": "function_68",
                    "args": [
                        {
                            "name": "x",
                            "type": "bool",
                        },
                    ],
                    "return_type": "None",
                },
                "function_69": {
                    "name": "function_69",
                    "args": [
                        {
                            "name": "x",
                            "type": "dict",
                        },
                    ],
                    "return_type": "None",
                },
                "function_70": {
                    "name": "function_70",
                    "args": [
                        {
                            "name": "x",
                            "type": "list",
                        },
                    ],
                    "return_type": "None",
                },
                "function_71": {
                    "name": "function_71",
                    "args": [
                        {
                            "name": "x",
                            "type": "date",
                        },
                    ],
                    "return_type": "None",
                },
                "function_72": {
                    "name": "function_72",
                    "args": [
                        {
                            "name": "x",
                            "type": "datetime",
                        },
                    ],
                    "return_type": "None",
                },
                "function_73": {
                    "name": "function_73",
                    "args": [
                        {
                            "name": "x",
                            "type": "time",
                        },
                    ],
                    "return_type": "None",
                },
                "function_74": {
                    "name": "function_74",
                    "args": [
                        {
                            "name": "x",
                            "type": "timedelta",
                        },
                    ],
                    "return_type": "None",
                },
                "function_75": {
                    "name": "function_75",
                    "args": [
                        {
                            "name": "x",
                            "type": "Decimal",
                        },
                    ],
                    "return_type": "None",
                },
                "function_76": {
                    "name": "function_76",
                    "args": [
                        {
                            "name": "x",
                            "type": "type",
                        },
                    ],
                    "return_type": "None",
                },
                "function_77": {
                    "name": "function_77",
                    "args": [
                        {
                            "name": "x",
                            "type": "Exception",
                        },
                    ],
                    "return_type": "None",
                },
                "function_78": {
                    "name": "function_78",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Foo",
                        },
                    ],
                    "return_type": "None",
                },
                "function_79": {
                    "name": "function_79",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Fizz",
                        },
                    ],
                    "return_type": "None",
                },
                "function_80": {
                    "name": "function_80",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Bar",
                        },
                    ],
                    "return_type": "None",
                },
                "function_81": {
                    "name": "function_81",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Barr",
                        },
                    ],
                    "return_type": "None",
                },
                "function_82": {
                    "name": "function_82",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Baz",
                        },
                    ],
                    "return_type": "None",
                },
                "function_83": {
                    "name": "function_83",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Bazz",
                        },
                    ],
                    "return_type": "None",
                },
                "function_84": {
                    "name": "function_84",
                    "args": [],
                    "return_type": "Foo",
                },
                "function_85": {
                    "name": "function_85",
                    "args": [],
                    "return_type": "Fizz",
                },
                "function_86": {
                    "name": "function_86",
                    "args": [],
                    "return_type": "Bar",
                },
                "function_87": {
                    "name": "function_87",
                    "args": [],
                    "return_type": "Barr",
                },
                "function_88": {
                    "name": "function_88",
                    "args": [],
                    "return_type": "Baz",
                },
                "function_89": {
                    "name": "function_89",
                    "args": [],
                    "return_type": "Bazz",
                },
                "function_90": {
                    "name": "function_90",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Foo",
                        },
                    ],
                    "return_type": "None",
                },
                "function_91": {
                    "name": "function_91",
                    "args": [],
                    "return_type": "Foo",
                },
                "function_92": {
                    "name": "function_92",
                    "args": [],
                    "return_type": "list[Foo]",
                },
                "function_93": {
                    "name": "function_93",
                    "args": [],
                    "return_type": "dict[str, Foo]",
                },
                "function_94": {
                    "name": "function_94",
                    "args": [
                        {
                            "name": "foo",
                            "type": "Buzz",
                        },
                    ],
                    "return_type": "None",
                },
                "function_95": {
                    "name": "function_95",
                    "args": [],
                    "return_type": "Buzz",
                },
                "function_96": {
                    "name": "function_96",
                    "args": [
                        {
                            "name": "foo",
                            "type": "str | int",
                        },
                    ],
                    "return_type": "None",
                },
                "function_97": {
                    "name": "function_97",
                    "args": [],
                    "return_type": "Foo | Bar",
                },
            },
        },
    }
