import unittest
from typing import List

# noinspection PyUnresolvedReferences
from fastapi import FastAPI

try:
    # noinspection PyUnresolvedReferences
    from fastapi.testclient import TestClient
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.testclient import TestClient

# noinspection PyUnresolvedReferences
from pydantic import BaseModel, Field


class DefaultTest(unittest.TestCase):
    @staticmethod
    def run_test(
        mode="get", url="/", data=None, alias=False, items=(("valid", 1.0, None),)
    ):
        app = FastAPI()

        if alias:

            class Item(BaseModel):
                name: str = Field(..., alias="aliased_name")
                price: float = None
                owner_ids: List[int] = None

            name = "aliased_name"
        else:

            class Item(BaseModel):
                name: str
                price: float = None
                owner_ids: List[int] = None

            name = "name"

        if len(items) == 1:

            @app.get("/get", response_model=Item)
            def get_valid():
                return Item(
                    **{
                        name: items[0][0],
                        "price": items[0][1],
                        "owner_ids": items[0][2],
                    }
                )

            @app.post("/post", response_model=Item)
            def get_valid():
                return Item(
                    **{
                        name: items[0][0],
                        "price": items[0][1],
                        "owner_ids": items[0][2],
                    }
                )

        else:

            @app.get("/get", response_model=List[Item])
            def get_valid():
                return [
                    Item(**{name: item[0], "price": item[1], "owner_ids": item[2]})
                    for item in items
                ]

            @app.post("/post", response_model=List[Item])
            def get_valid():
                return [
                    Item(**{name: item[0], "price": item[1], "owner_ids": item[2]})
                    for item in items
                ]

        client = TestClient(app)

        if data is not None:
            response = getattr(client, mode)(url, json=data)
            return response.json(), response.status_code
        else:
            response = getattr(client, mode)(url)
            return response.json(), response.status_code


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        response, status = self.run_test("get", "/get", alias=True)
        self.assertEqual(
            {"aliased_name": "valid", "price": 1.0, "owner_ids": None}, response
        )
        self.assertEqual(200, status)

    def test_diversity_2(self):
        response, status = self.run_test("get", "/get", alias=True, data=[1, 2, 3])
        self.assertEqual(
            {"aliased_name": "valid", "price": 1.0, "owner_ids": None}, response
        )
        self.assertEqual(200, status)

    def test_diversity_3(self):
        response, status = self.run_test(
            "get", "/get", alias=True, items=[("valid", "1.0", None)]
        )
        self.assertEqual(
            {"aliased_name": "valid", "price": 1.0, "owner_ids": None}, response
        )
        self.assertEqual(200, status)

    def test_diversity_4(self):
        response, status = self.run_test(
            "get", "/get", alias=True, data=[1, 2, 3], items=[("valid", "1.0", None)]
        )
        self.assertEqual(
            {"aliased_name": "valid", "price": 1.0, "owner_ids": None}, response
        )
        self.assertEqual(200, status)

    def test_diversity_5(self):
        response, status = self.run_test(
            "get",
            "/get",
            alias=True,
            items=[("foo", None, None), ("bar", 1.0, None), ("baz", 2.0, [1, 2, 3])],
        )
        self.assertEqual(
            [
                {"aliased_name": "foo", "price": None, "owner_ids": None},
                {"aliased_name": "bar", "price": 1.0, "owner_ids": None},
                {"aliased_name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
            ],
            response,
        )
        self.assertEqual(200, status)

    def test_diversity_6(self):
        response, status = self.run_test(
            "get",
            "/get",
            alias=True,
            data=[1, 2, 3],
            items=[("foo", None, None), ("bar", 1.0, None), ("baz", 2.0, [1, 2, 3])],
        )
        self.assertEqual(
            [
                {"aliased_name": "foo", "price": None, "owner_ids": None},
                {"aliased_name": "bar", "price": 1.0, "owner_ids": None},
                {"aliased_name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
            ],
            response,
        )
        self.assertEqual(200, status)

    def test_diversity_7(self):
        response, status = self.run_test("post", "/post", alias=True)
        self.assertEqual(
            {"aliased_name": "valid", "price": 1.0, "owner_ids": None}, response
        )
        self.assertEqual(200, status)

    def test_diversity_8(self):
        response, status = self.run_test(
            "post", "/post", alias=True, items=[("valid", "1.0", None)]
        )
        self.assertEqual(
            {"aliased_name": "valid", "price": 1.0, "owner_ids": None}, response
        )
        self.assertEqual(200, status)

    def test_diversity_9(self):
        response, status = self.run_test(
            "post",
            "/post",
            alias=True,
            items=[("foo", None, None), ("bar", 1.0, None), ("baz", 2.0, [1, 2, 3])],
        )
        self.assertEqual(
            [
                {"aliased_name": "foo", "price": None, "owner_ids": None},
                {"aliased_name": "bar", "price": 1.0, "owner_ids": None},
                {"aliased_name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
            ],
            response,
        )
        self.assertEqual(200, status)

    def test_diversity_10(self):
        response, status = self.run_test("post", "/post", alias=True, data=[1, 2, 3])
        self.assertEqual(
            {"aliased_name": "valid", "price": 1.0, "owner_ids": None}, response
        )
        self.assertEqual(200, status)


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        response, status = self.run_test("get", "/get")
        self.assertEqual({"name": "valid", "price": 1.0, "owner_ids": None}, response)
        self.assertEqual(200, status)

    def test_diversity_2(self):
        response, status = self.run_test("get", "/get", data=[1, 2, 3])
        self.assertEqual({"name": "valid", "price": 1.0, "owner_ids": None}, response)
        self.assertEqual(200, status)

    def test_diversity_3(self):
        response, status = self.run_test("get", "/get", items=[("valid", "1.0", None)])
        self.assertEqual({"name": "valid", "price": 1.0, "owner_ids": None}, response)
        self.assertEqual(200, status)

    def test_diversity_4(self):
        response, status = self.run_test(
            "get", "/get", data=[1, 2, 3], items=[("valid", "1.0", None)]
        )
        self.assertEqual({"name": "valid", "price": 1.0, "owner_ids": None}, response)
        self.assertEqual(200, status)

    def test_diversity_5(self):
        response, status = self.run_test(
            "get",
            "/get",
            items=[("foo", None, None), ("bar", 1.0, None), ("baz", 2.0, [1, 2, 3])],
        )
        self.assertEqual(
            [
                {"name": "foo", "price": None, "owner_ids": None},
                {"name": "bar", "price": 1.0, "owner_ids": None},
                {"name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
            ],
            response,
        )
        self.assertEqual(200, status)

    def test_diversity_6(self):
        response, status = self.run_test(
            "get",
            "/get",
            data=[1, 2, 3],
            items=[("foo", None, None), ("bar", 1.0, None), ("baz", 2.0, [1, 2, 3])],
        )
        self.assertEqual(
            [
                {"name": "foo", "price": None, "owner_ids": None},
                {"name": "bar", "price": 1.0, "owner_ids": None},
                {"name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
            ],
            response,
        )
        self.assertEqual(200, status)

    def test_diversity_7(self):
        response, status = self.run_test("post", "/post")
        self.assertEqual({"name": "valid", "price": 1.0, "owner_ids": None}, response)
        self.assertEqual(200, status)

    def test_diversity_8(self):
        response, status = self.run_test(
            "post", "/post", items=[("valid", "1.0", None)]
        )
        self.assertEqual({"name": "valid", "price": 1.0, "owner_ids": None}, response)
        self.assertEqual(200, status)

    def test_diversity_9(self):
        response, status = self.run_test(
            "post",
            "/post",
            items=[("foo", None, None), ("bar", 1.0, None), ("baz", 2.0, [1, 2, 3])],
        )
        self.assertEqual(
            [
                {"name": "foo", "price": None, "owner_ids": None},
                {"name": "bar", "price": 1.0, "owner_ids": None},
                {"name": "baz", "price": 2.0, "owner_ids": [1, 2, 3]},
            ],
            response,
        )
        self.assertEqual(200, status)

    def test_diversity_10(self):
        response, status = self.run_test("post", "/post", data=[1, 2, 3])
        self.assertEqual({"name": "valid", "price": 1.0, "owner_ids": None}, response)
        self.assertEqual(200, status)
