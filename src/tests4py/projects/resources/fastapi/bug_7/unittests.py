import unittest
from decimal import Decimal

# noinspection PyUnresolvedReferences
from fastapi import FastAPI

try:
    # noinspection PyUnresolvedReferences
    from fastapi.testclient import TestClient
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.testclient import TestClient

# noinspection PyUnresolvedReferences
from pydantic import BaseModel, condecimal, conint, confloat


class DefaultTest(unittest.TestCase):
    @staticmethod
    def run_test(
        model: BaseModel,
        mode="post",
        url="/",
        data=None,
    ):
        app = FastAPI()

        @app.post("/item")
        def save_item(item: model):
            return {"name": item.name, "age": item.age}

        client = TestClient(app)

        if data is not None:
            response = getattr(client, mode)(url, json=data)
            return response.json(), response.status_code
        else:
            response = getattr(client, mode)(url)
            return response.json(), response.status_code

    @staticmethod
    def run_gt(mode="post", url="/", data=None, limit=0.0):
        class Item(BaseModel):
            name: str
            age: condecimal(gt=Decimal(limit))

        return DefaultTest.run_test(Item, mode, url, data)

    @staticmethod
    def run_lt(mode="post", url="/", data=None, limit=100.0):
        class Item(BaseModel):
            name: str
            age: condecimal(lt=Decimal(limit))

        return DefaultTest.run_test(Item, mode, url, data)

    @staticmethod
    def run_multiple_of(mode="post", url="/", data=None, limit=2.0):
        class Item(BaseModel):
            name: str
            age: condecimal(multiple_of=Decimal(limit))

        return DefaultTest.run_test(Item, mode, url, data)

    @staticmethod
    def run_conint(mode="post", url="/", data=None, limit=0):
        class Item(BaseModel):
            name: str
            age: conint(gt=limit)

        return DefaultTest.run_test(Item, mode, url, data)

    @staticmethod
    def run_confloat(mode="post", url="/", data=None, limit=0.0):
        class Item(BaseModel):
            name: str
            age: confloat(gt=limit)

        return DefaultTest.run_test(Item, mode, url, data)


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_gt(
            "post", "/item", limit=0.0, data={"name": "test", "age": -1}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_2(self):
        response, status_code = self.run_gt(
            "post", "/item", limit=10.0, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_3(self):
        response, status_code = self.run_lt(
            "post", "/item", limit=10.0, data={"name": "test", "age": 15}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_4(self):
        response, status_code = self.run_multiple_of(
            "post", "/item", limit=2, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_5(self):
        response, status_code = self.run_lt(
            "post", "/item", limit=0.0, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_6(self):
        response, status_code = self.run_multiple_of(
            "post", "/item", limit=3, data={"name": "test", "age": 2}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_7(self):
        response, status_code = self.run_gt(
            "post", "/item", limit=0.0, data={"name": "test", "age": -10}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_8(self):
        response, status_code = self.run_gt(
            "post", "/item", limit=20.0, data={"name": "test", "age": 19}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_9(self):
        response, status_code = self.run_lt(
            "post", "/item", limit=10.0, data={"name": "test", "age": 11}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_10(self):
        response, status_code = self.run_multiple_of(
            "post",
            "/item",
            limit=-2,
            data={"name": "test", "age": -31},
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_gt(
            "get", "/item", limit=0.0, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 405)
        self.assertEqual({"detail": "Method Not Allowed"}, response)

    def test_diversity_2(self):
        response, status_code = self.run_gt(
            "post", "/item", limit=0.0, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"name": "test", "age": 5}, response)

    def test_diversity_3(self):
        response, status_code = self.run_lt(
            "post", "/item", limit=10.0, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"name": "test", "age": 5}, response)

    def test_diversity_4(self):
        response, status_code = self.run_multiple_of(
            "post", "/item", limit=2, data={"name": "test", "age": 8}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"name": "test", "age": 8}, response)

    def test_diversity_5(self):
        response, status_code = self.run_conint(
            "post", "/item", limit=0, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"name": "test", "age": 5}, response)

    def test_diversity_6(self):
        response, status_code = self.run_confloat(
            "post", "/item", limit=0.0, data={"name": "test", "age": 5}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"name": "test", "age": 5}, response)

    def test_diversity_7(self):
        response, status_code = self.run_conint(
            "post", "/item", limit=0, data={"name": "test", "age": -1}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_8(self):
        response, status_code = self.run_confloat(
            "post", "/item", limit=0.0, data={"name": "test", "age": -1}
        )
        self.assertEqual(status_code, 422)
        self.assertIn("detail", response)

    def test_diversity_9(self):
        response, status_code = self.run_gt(
            "post",
            "/item",
            limit=50.0,
            data={"name": "test", "age": 100},
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"name": "test", "age": 100}, response)

    def test_diversity_10(self):
        response, status_code = self.run_lt(
            "post", "/item", limit=50.0, data={"name": "test", "age": 49}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"name": "test", "age": 49}, response)
