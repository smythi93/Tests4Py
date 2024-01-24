import unittest

# noinspection PyUnresolvedReferences
from fastapi import APIRouter, Depends, FastAPI

try:
    # noinspection PyUnresolvedReferences
    from fastapi.testclient import TestClient
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.testclient import TestClient

# noinspection PyUnresolvedReferences
from pydantic import BaseModel


class DefaultTest(unittest.TestCase):
    @staticmethod
    def run_test(
        mode="get",
        url="/",
        data=None,
        b_username="b",
        a_username="a",
        a_password="password",
    ):
        app = FastAPI()

        class ModelB(BaseModel):
            username: str

        @app.get("/b", response_model=ModelB)
        async def get_model_b() -> ModelB:
            return ModelB(username=b_username)

        class ModelA(ModelB):
            password: str

        @app.get("/a", response_model=ModelA)
        async def get_model_a() -> ModelA:
            return ModelA(username=a_username, password=a_password)

        class ModelC(BaseModel):
            id_: int
            model_b: ModelB

        @app.get("/c/a", response_model=ModelC)
        async def get_model_c_a(model_a=Depends(get_model_a)):
            return {"id_": 0, "model_b": model_a}

        @app.get("/c/b", response_model=ModelC)
        async def get_model_c_b(model_b=Depends(get_model_b)):
            return {"id_": 0, "model_b": model_b}

        client = TestClient(app)

        if data is not None:
            response = getattr(client, mode)(url, json=data)
            return response.json(), response.status_code
        else:
            response = getattr(client, mode)(url)
            return response.json(), response.status_code


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_test("get", "/c/a", None, "b", "a", "password")
        self.assertEqual({"id_": 0, "model_b": {"username": "a"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_2(self):
        response, status_code = self.run_test(
            "get", "/c/a", [1, 2, 3], "b", "a", "password"
        )
        self.assertEqual({"id_": 0, "model_b": {"username": "a"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_3(self):
        response, status_code = self.run_test("get", "/c/a", 123, "b", "a", "password")
        self.assertEqual({"id_": 0, "model_b": {"username": "a"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_4(self):
        response, status_code = self.run_test(
            "get", "/c/a", "test", "b", "a", "password"
        )
        self.assertEqual({"id_": 0, "model_b": {"username": "a"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_5(self):
        response, status_code = self.run_test("get", "/c/a", None, "b_u", "a_u", "pwd")
        self.assertEqual({"id_": 0, "model_b": {"username": "a_u"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_6(self):
        response, status_code = self.run_test(
            "get", "/c/a", [1, 2, 3], "b_u", "a_u", "pwd"
        )
        self.assertEqual({"id_": 0, "model_b": {"username": "a_u"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_7(self):
        response, status_code = self.run_test("get", "/c/a", 123, "b_u", "a_u", "pwd")
        self.assertEqual({"id_": 0, "model_b": {"username": "a_u"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_8(self):
        response, status_code = self.run_test(
            "get", "/c/a", "test", "b_u", "a_u", "pwd"
        )
        self.assertEqual({"id_": 0, "model_b": {"username": "a_u"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_9(self):
        response, status_code = self.run_test(
            "get", "/c/a", None, "b_user", "a_user", "a_password"
        )
        self.assertEqual({"id_": 0, "model_b": {"username": "a"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_10(self):
        response, status_code = self.run_test(
            "get", "/c/a", [1, 2, 3], "b_user", "a_user", "a_password"
        )
        self.assertEqual({"id_": 0, "model_b": {"username": "a_user"}}, response)
        self.assertEqual(status_code, 200)


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_test("get", "/c/b", None, "b", "a", "password")
        self.assertEqual({"id_": 0, "model_b": {"username": "b"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_2(self):
        response, status_code = self.run_test(
            "get", "/c/b", [1, 2, 3], "b", "a", "password"
        )
        self.assertEqual({"id_": 0, "model_b": {"username": "b"}}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_3(self):
        response, status_code = self.run_test(
            "post", "/c/b", None, "b", "a", "password"
        )
        self.assertEqual({"detail": "Method Not Allowed"}, response)
        self.assertEqual(status_code, 405)

    def test_diversity_4(self):
        response, status_code = self.run_test(
            "post", "/c/b", [1, 2, 3], "b", "a", "password"
        )
        self.assertEqual({"detail": "Method Not Allowed"}, response)
        self.assertEqual(status_code, 405)

    def test_diversity_5(self):
        response, status_code = self.run_test("get", "/a", None, "b", "a", "password")
        self.assertEqual({"username": "a", "password": "password"}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_6(self):
        response, status_code = self.run_test("get", "/b", None, "b", "a", "password")
        self.assertEqual({"username": "b"}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_7(self):
        response, status_code = self.run_test("get", "/a", None, "b", "b", "password")
        self.assertEqual({"username": "b", "password": "password"}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_8(self):
        response, status_code = self.run_test("get", "/b", None, "a", "a", "password")
        self.assertEqual({"username": "a"}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_9(self):
        response, status_code = self.run_test(
            "get", "/a", [1, 2, 3], "b", "a", "password"
        )
        self.assertEqual({"username": "a", "password": "password"}, response)
        self.assertEqual(status_code, 200)

    def test_diversity_10(self):
        response, status_code = self.run_test(
            "get", "/b", [1, 2, 3], "b", "a", "password"
        )
        self.assertEqual({"username": "b"}, response)
        self.assertEqual(status_code, 200)
