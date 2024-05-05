from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from datetime import date, datetime, time, timedelta
    from decimal import Decimal

    from tests.conftest import TestType


__all__ = [
    "Bar",
    "Barr",
    "Baz",
    "Bazz",
    "Buzz",
    "Class_1",
    "Fizz",
    "Foo",
    "function_01",
    "function_02",
    "function_03",
    "function_04",
    "function_05",
    "function_06",
    "function_07",
    "function_08",
    "function_09",
    "function_10",
    "function_11",
    "function_12",
    "function_13",
    "function_14",
    "function_15",
    "function_16",
    "function_17",
    "function_18",
    "function_19",
    "function_20",
    "function_21",
    "function_22",
    "function_23",
    "function_24",
    "function_25",
    "function_26",
    "function_27",
    "function_28",
    "function_29",
    "function_30",
    "function_31",
    "function_32",
    "function_33",
    "function_34",
    "function_35",
    "function_36",
    "function_37",
    "function_38",
    "function_39",
    "function_40",
    "function_41",
    "function_42",
    "function_43",
    "function_44",
    "function_45",
    "function_46",
    "function_47",
    "function_48",
    "function_49",
    "function_50",
    "function_51",
    "function_52",
    "function_53",
    "function_54",
    "function_55",
    "function_56",
    "function_57",
    "function_58",
    "function_59",
    "function_60",
    "function_61",
    "function_62",
    "function_63",
    "function_64",
    "function_65",
    "function_66",
    "function_67",
    "function_68",
    "function_69",
    "function_70",
    "function_71",
    "function_72",
    "function_73",
    "function_74",
    "function_75",
    "function_76",
    "function_77",
    "function_78",
    "function_79",
    "function_80",
    "function_81",
    "function_82",
    "function_83",
    "function_84",
    "function_85",
    "function_86",
    "function_87",
    "function_88",
    "function_89",
    "function_90",
    "function_91",
    "function_92",
    "function_93",
    "function_94",
    "function_95",
    "function_96",
    "function_97",
]


class Foo(TypedDict):
    name: str
    age: int


class Bar(TypedDict):
    item: Foo
    things: list[Foo]
    other: dict[str, Foo]


class Barr(TypedDict):
    item: Foo
    things: list[Foo]
    other: dict[str, Foo]


class Baz(TypedDict):
    weird: Bar
    nested: list[dict[str, Bar]]
    another: dict[str, list[Bar]]


class Bazz(TypedDict):
    weird: Barr
    nested: list[dict[str, Barr]]
    another: dict[str, list[Barr]]


class Fizz(TypedDict):
    union: int | float
    optional: str | None


class Buzz(TypedDict):
    not_available: TestType


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return {}

    return wrapper


def function_01(name, age) -> None:
    pass


def function_02(name: int, age) -> None:
    pass


def function_03(name, age: int) -> None:
    pass


def function_04(name: int, age: int) -> None:
    pass


def function_05(name, age=2.0) -> None:
    pass


def function_06(name: int, age=2.0) -> None:
    pass


def function_07(name, age: int = 2.0) -> None:
    pass


def function_08(name: int, age: int = 2.0) -> None:
    pass


def function_09(name=1.0, age=2.0) -> None:
    pass


def function_10(name: int = 1.0, age=2.0) -> None:
    pass


def function_11(name=1.0, age: int = 2.0) -> None:
    pass


def function_12(name: int = 1.0, age: int = 2.0) -> None:
    pass


def function_13(*, name, age) -> None:
    pass


def function_14(*, name: int, age) -> None:
    pass


def function_15(*, name, age: int) -> None:
    pass


def function_16(*, name: int, age: int) -> None:
    pass


def function_17(*, name, age=2.0) -> None:
    pass


def function_18(*, name: int, age=2.0) -> None:
    pass


def function_19(*, name, age: int = 2.0) -> None:
    pass


def function_20(*, name: int, age: int = 2.0) -> None:
    pass


def function_21(*, name=1.0, age=2.0) -> None:
    pass


def function_22(*, name: int = 1.0, age=2.0) -> None:
    pass


def function_23(*, name=1.0, age: int = 2.0) -> None:
    pass


def function_24(*, name: int = 1.0, age: int = 2.0) -> None:
    pass


def function_25(name, *args) -> None:
    pass


def function_26(name: int, *args) -> None:
    pass


def function_27(name, *args: int) -> None:
    pass


def function_28(name: int, *args: int) -> None:
    pass


def function_29(name, **kwargs) -> None:
    pass


def function_30(name: int, **kwargs) -> None:
    pass


def function_31(name, **kwargs: int) -> None:
    pass


def function_32(name: int, **kwargs: int) -> None:
    pass


def function_33(name=1.0, **kwargs) -> None:
    pass


def function_34(name: int = 1.0, **kwargs) -> None:
    pass


def function_35(name=1.0, **kwargs: int) -> None:
    pass


def function_36(name: int = 1.0, **kwargs: int) -> None:
    pass


def function_37(name, *args, **kwargs) -> None:
    pass


def function_38(name: int, *args, **kwargs) -> None:
    pass


def function_39(name, *args: int, **kwargs) -> None:
    pass


def function_40(name: int, *args: int, **kwargs) -> None:
    pass


def function_41(name, *args, **kwargs: int) -> None:
    pass


def function_42(name: int, *args, **kwargs: int) -> None:
    pass


def function_43(name, *args: int, **kwargs: int) -> None:
    pass


def function_44(name: int, *args: int, **kwargs: int) -> None:
    pass


def function_45(name=1.0, *args, **kwargs) -> None:
    pass


def function_46(name: int = 1.0, *args, **kwargs) -> None:
    pass


def function_47(name=1.0, *args: int, **kwargs) -> None:
    pass


def function_48(name: int = 1.0, *args: int, **kwargs) -> None:
    pass


def function_49(name=1.0, *args, **kwargs: int) -> None:
    pass


def function_50(name: int = 1.0, *args, **kwargs: int) -> None:
    pass


def function_51(name=1.0, *args: int, **kwargs: int) -> None:
    pass


def function_52(name: int = 1.0, *args: int, **kwargs: int) -> None:
    pass


def function_53(name, *, age) -> None:
    pass


def function_54(name: int, *, age) -> None:
    pass


def function_55(name, *, age: int) -> None:
    pass


def function_56(name: int, *, age: int) -> None:
    pass


def function_57(name=1.0, *, age) -> None:
    pass


def function_58(name: int = 1.0, *, age) -> None:
    pass


def function_59(name=1.0, *, age: int) -> None:
    pass


def function_60(name: int = 1.0, *, age: int) -> None:
    pass


def function_61(name, *, age=2.0) -> None:
    pass


def function_62(name: int, *, age=2.0) -> None:
    pass


def function_63(name, *, age: int = 2.0) -> None:
    pass


def function_64(name: int, *, age: int = 2.0) -> None:
    pass


def function_65(x: str) -> None:
    pass


def function_66(x: int) -> None:
    pass


def function_67(x: float) -> None:
    pass


def function_68(x: bool) -> None:
    pass


def function_69(x: dict) -> None:
    pass


def function_70(x: list) -> None:
    pass


def function_71(x: date) -> None:
    pass


def function_72(x: datetime) -> None:
    pass


def function_73(x: time) -> None:
    pass


def function_74(x: timedelta) -> None:
    pass


def function_75(x: Decimal) -> None:
    pass


def function_76(x: type) -> None:
    pass


def function_77(x: Exception) -> None:
    pass


def function_78(foo: Foo) -> None:
    pass


def function_79(foo: Fizz) -> None:
    pass


def function_80(foo: Bar) -> None:
    pass


def function_81(foo: Barr) -> None:
    pass


def function_82(foo: Baz) -> None:
    pass


def function_83(foo: Bazz) -> None:
    pass


def function_84() -> Foo:
    pass


def function_85() -> Fizz:
    pass


def function_86() -> Bar:
    pass


def function_87() -> Barr:
    pass


def function_88() -> Baz:
    pass


def function_89() -> Bazz:
    pass


@decorator
def function_90(foo: Foo) -> None:
    pass


@decorator
def function_91() -> Foo:
    pass


def function_92() -> list[Foo]:
    pass


def function_93() -> dict[str, Foo]:
    pass


def function_94(foo: Buzz) -> None:
    pass


def function_95() -> Buzz:
    pass


def function_96(foo: str | int) -> None:
    pass


def function_97() -> Foo | Bar:
    pass


class Class_1:
    foo = 1

    class Class_2:
        foo = {1: "foo", "z": [1, 2, 3]}

    def __init__(self, foo: Foo) -> None:
        pass

    def method(self, foo: int) -> None:
        pass

    @classmethod
    def classmethod(cls, foo: int) -> None:
        pass

    @staticmethod
    def staticmethod(foo: int) -> None:
        pass

    @property
    def property(self) -> None:
        pass
