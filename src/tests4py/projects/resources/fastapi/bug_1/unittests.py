import unittest

# noinspection PyUnresolvedReferences
from fastapi.encoders import jsonable_encoder

# noinspection PyUnresolvedReferences
from pydantic import BaseModel

try:
    # noinspection PyUnresolvedReferences
    from pydantic import Field
except ImportError:
    # noinspection PyUnresolvedReferences
    from pydantic import Schema as Field


class DefaultTest(unittest.TestCase):
    @staticmethod
    def run_test(
        obj=None,
        include=None,
        exclude=None,
        by_alias=None,
        skip_defaults=None,
        exclude_unset=None,
        exclude_defaults=None,
        include_none=None,
        exclude_none=None,
        custom_encoder=None,
        sqlalchemy_safe=None,
    ):
        parameters = dict()
        if obj is not None:
            parameters["obj"] = obj
        if include is not None:
            parameters["include"] = include
        if exclude is not None:
            parameters["exclude"] = exclude
        if by_alias is not None:
            parameters["by_alias"] = False
        if skip_defaults is not None:
            parameters["skip_defaults"] = True
        if exclude_unset is not None:
            parameters["exclude_unset"] = True
        if exclude_defaults is not None:
            parameters["exclude_defaults"] = True
        if include_none is not None:
            parameters["include_none"] = False
        if exclude_none is not None:
            parameters["exclude_none"] = True
        if custom_encoder is not None:
            parameters["custom_encoder"] = custom_encoder
        if sqlalchemy_safe is not None:
            parameters["sqlalchemy_safe"] = False
        jsonable_encoder(**parameters)

    class Model(BaseModel):
        foo: str = Field(..., alias="foo")
        bar: str = "bar"
        bla: str = "bla"

        class Config:
            use_enum_values = True


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        self.run_test(obj={"foo": "test"}, exclude_defaults=True)

    def test_diversity_2(self):
        self.run_test(obj=self.Model(foo="test"), exclude_defaults=True)

    def test_diversity_3(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo"),
            exclude_defaults=True,
            exclude_none=True,
            by_alias=True,
        )

    def test_diversity_4(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            exclude_unset=True,
            skip_defaults=True,
            exclude_defaults=True,
        )

    def test_diversity_5(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            sqlalchemy_safe=True,
            exclude_defaults=True,
        )

    def test_diversity_6(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            exclude_defaults=True,
            custom_encoder={str: repr},
        )

    def test_diversity_7(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            exclude_none=True,
            include=["foo"],
            exclude_defaults=True,
            custom_encoder={str: repr},
        )

    def test_diversity_8(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo"),
            sqlalchemy_safe=True,
            exclude_defaults=True,
        )

    def test_diversity_9(self):
        self.run_test(
            obj={"foo": "1", "bar": "2", "bla": "3", "da": "4"},
            exclude=["bla"],
            exclude_defaults=True,
        )

    def test_diversity_10(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo"),
            include=["foo"],
            exclude=["bla"],
            exclude_defaults=True,
            custom_encoder={str: repr},
        )


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        self.run_test(obj={"foo": "test"})

    def test_diversity_2(self):
        self.run_test(obj=self.Model(foo="test"))

    def test_diversity_3(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo"),
            by_alias=True,
        )

    def test_diversity_4(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            skip_defaults=True,
            exclude_unset=True,
        )

    def test_diversity_5(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            sqlalchemy_safe=True,
        )

    def test_diversity_6(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            custom_encoder={str: repr},
        )

    def test_diversity_7(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo", bla="da"),
            custom_encoder={str: repr},
            include=["foo"],
            by_alias=True,
        )

    def test_diversity_8(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo"),
            sqlalchemy_safe=True,
        )

    def test_diversity_9(self):
        self.run_test(
            obj={"foo": "1", "bar": "2", "bla": "3", "da": "4"},
            exclude=["bla"],
        )

    def test_diversity_10(self):
        self.run_test(
            obj=self.Model(foo="bar", bar="foo"),
            include=["foo"],
            exclude=["bla"],
            custom_encoder={str: repr},
        )
