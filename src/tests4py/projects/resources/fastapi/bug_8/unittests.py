import unittest

# noinspection PyUnresolvedReferences
from fastapi import FastAPI, APIRouter

# noinspection PyUnresolvedReferences
from fastapi.routing import APIRoute

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
    def run_test(url="/", value="value"):
        app = FastAPI()

        class CustomAPIRoute(APIRoute):
            val = value

        router = APIRouter(route_class=CustomAPIRoute)

        @router.get("/")
        def get():
            return {"msg": value}

        app.include_router(router, prefix=url)

        return app

    @staticmethod
    def _get_routes(app: FastAPI):
        routes = {}
        for r in app.router.routes:
            routes[r.path] = r
        return routes

    @staticmethod
    def get_routes(url="/", value="value"):
        app = DefaultTest.run_test(url, value)
        return DefaultTest._get_routes(app)

    @staticmethod
    def run_get(url="/", value="value", mode="get", data=None):
        app = DefaultTest.run_test(url, value)
        client = TestClient(app)
        if data is not None:
            response = getattr(client, mode)(url, json=data)
            return response.json(), response.status_code, DefaultTest._get_routes(app)
        else:
            response = getattr(client, mode)(url)
            return response.json(), response.status_code, DefaultTest._get_routes(app)


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        routes = self.get_routes(url="/test", value="test")
        self.assertIn("/test/", routes)
        self.assertEqual("test", routes["/test/"].val)

    def test_diversity_2(self):
        routes = self.get_routes(url="/test", value="test2")
        self.assertIn("/test/", routes)
        self.assertEqual("test2", routes["/test/"].val)

    def test_diversity_3(self):
        routes = self.get_routes(url="/test1", value="test")
        self.assertIn("/test1/", routes)
        self.assertEqual("test", routes["/test1/"].val)

    def test_diversity_4(self):
        routes = self.get_routes(url="/test2", value="test2")
        self.assertIn("/test2/", routes)
        self.assertEqual("test2", routes["/test2/"].val)

    def test_diversity_5(self):
        _, _, routes = self.run_get(url="/test", value="test", mode="get")
        self.assertIn("/test/", routes)
        self.assertEqual("test", routes["/test/"].val)

    def test_diversity_6(self):
        _, _, routes = self.run_get(url="/test", value="test2", mode="get")
        self.assertIn("/test/", routes)
        self.assertEqual("test2", routes["/test/"].val)

    def test_diversity_7(self):
        _, _, routes = self.run_get(url="/test1", value="test", mode="get")
        self.assertIn("/test1/", routes)
        self.assertEqual("test", routes["/test1/"].val)

    def test_diversity_8(self):
        _, _, routes = self.run_get(url="/test2", value="test2", mode="get")
        self.assertIn("/test2/", routes)
        self.assertEqual("test2", routes["/test2/"].val)

    def test_diversity_9(self):
        _, _, routes = self.run_get(url="/test", value="test", mode="get", data="test")
        self.assertIn("/test/", routes)
        self.assertEqual("test", routes["/test/"].val)

    def test_diversity_10(self):
        _, _, routes = self.run_get(
            url="/test", value="test2", mode="get", data={"name": "test", "age": 5}
        )
        self.assertIn("/test/", routes)
        self.assertEqual("test2", routes["/test/"].val)


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        response, status_code, _ = self.run_get(url="/test", value="test", mode="get")
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test"}, response)

    def test_diversity_2(self):
        response, status_code, _ = self.run_get(url="/test", value="test2", mode="get")
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test2"}, response)

    def test_diversity_3(self):
        response, status_code, _ = self.run_get(url="/test2", value="test", mode="get")
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test"}, response)

    def test_diversity_4(self):
        response, status_code, _ = self.run_get(url="/test2", value="test2", mode="get")
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test2"}, response)

    def test_diversity_5(self):
        response, status_code, _ = self.run_get(
            url="/test", value="test", mode="get", data="test"
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test"}, response)

    def test_diversity_6(self):
        response, status_code, _ = self.run_get(
            url="/test", value="test2", mode="get", data={"name": "test", "age": 5}
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test2"}, response)

    def test_diversity_7(self):
        response, status_code, _ = self.run_get(
            url="/test2", value="test", mode="get", data="test"
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test"}, response)

    def test_diversity_8(self):
        response, status_code, _ = self.run_get(
            url="/test2", value="test2", mode="get", data={"name": "test", "age": 5}
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test2"}, response)

    def test_diversity_9(self):
        response, status_code, _ = self.run_get(
            url="/test", value="test", mode="get", data={"name": "test", "age": 5}
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test"}, response)

    def test_diversity_10(self):
        response, status_code, _ = self.run_get(
            url="/test", value="test123", mode="get", data={"name": "test", "age": 5}
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": "test123"}, response)
