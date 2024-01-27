import unittest
from typing import List

# noinspection PyUnresolvedReferences
from fastapi import Depends, FastAPI

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
    def run_test(gets=(), posts=(), params=()):
        app = FastAPI()

        class Item(BaseModel):
            name: str

        for url in gets:

            @app.get(url, response_model=Item)
            def get_valid():
                return {"name": "valid"}

        for url in posts:

            @app.post(url, response_model=Item)
            def post_valid():
                return {"name": "valid"}

        async def exists(value: int):
            return True

        for url, parameter in params:

            @app.get(f"{url}/{parameter}", dependencies=[Depends(exists)])
            def get_valid(value: int):
                pass

        client = TestClient(app)

        response = client.get("/openapi.json")
        return response.json(), response.status_code

    def assert_test(self, gets=(), posts=(), params=()):
        response, status = self.run_test(
            gets=gets, posts=posts, params=(("/user", "{user_id}"),)
        )
        self.assertIn("openapi", response)
        self.assertIn("info", response)
        for url in gets:
            self.assertIn(url, response["paths"])
            self.assertIn("get", response["paths"][url])
        for url in posts:
            self.assertIn(url, response["paths"])
            self.assertIn("post", response["paths"][url])
        for url, parameter in params:
            if parameter.startswith("{") and parameter.endswith("}"):
                u = f"{url}/{parameter}"
                self.assertIn(u, response["paths"])
                self.assertIn("get", response["paths"][u])
                self.assertIn("parameters", response["paths"][u]["get"])
                self.assertIsInstance(response["paths"][u]["get"]["parameters"], List)
                self.assertEqual(1, len(response["paths"][u]["get"]["parameters"]))

        self.assertEqual(200, status)


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        self.assert_test(params=[("/user", "{user_id}")])

    def test_diversity_2(self):
        self.assert_test(gets=["/g1"], params=[("/user", "{user_id}")])

    def test_diversity_3(self):
        self.assert_test(posts=["/p1"], params=[("/user", "{user_id}")])

    def test_diversity_4(self):
        self.assert_test(gets=["/g1"], posts=["/p1"], params=[("/user", "{user_id}")])

    def test_diversity_5(self):
        self.assert_test(
            gets=["/g1", "/g2"], posts=["/p1", "/p2"], params=[("/user", "{user_id}")]
        )

    def test_diversity_6(self):
        self.assert_test(params=[("/user", "{user_id}"), ("/item", "{item_id}")])

    def test_diversity_7(self):
        self.assert_test(
            gets=["/g1"], params=[("/user", "{user_id}"), ("/item", "{item_id}")]
        )

    def test_diversity_8(self):
        self.assert_test(
            posts=["/p1"], params=[("/user", "{user_id}"), ("/item", "{item_id}")]
        )

    def test_diversity_9(self):
        self.assert_test(
            gets=["/g1"],
            posts=["/p1"],
            params=[("/user", "{user_id}"), ("/item", "{item_id}")],
        )

    def test_diversity_10(self):
        self.assert_test(
            gets=["/g1", "/g2"],
            posts=["/p1", "/p2"],
            params=[("/user", "{user_id}"), ("/item", "{item_id}")],
        )


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        self.assert_test()

    def test_diversity_2(self):
        self.assert_test(gets=["/g1"])

    def test_diversity_3(self):
        self.assert_test(posts=["/p1"])

    def test_diversity_4(self):
        self.assert_test(gets=["/g1"], posts=["/p1"])

    def test_diversity_5(self):
        self.assert_test(gets=["/g1", "/g2"], posts=["/p1", "/p2"])

    def test_diversity_6(self):
        self.assert_test(params=[("/user", "user_id")])

    def test_diversity_7(self):
        self.assert_test(gets=["/g1"], params=[("/user", "user_id")])

    def test_diversity_8(self):
        self.assert_test(posts=["/p1"], params=[("/user", "user_id")])

    def test_diversity_9(self):
        self.assert_test(gets=["/g1"], posts=["/p1"], params=[("/user", "user_id")])

    def test_diversity_10(self):
        self.assert_test(
            gets=["/g1", "/g2"], posts=["/p1", "/p2"], params=[("/user", "user_id")]
        )
