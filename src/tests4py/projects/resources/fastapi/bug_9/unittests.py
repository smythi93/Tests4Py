import unittest

# noinspection PyUnresolvedReferences
from fastapi import FastAPI, Body

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
        url="/", target="/", mode="post", media_type=None, embed=False, data=None
    ):
        app = FastAPI()

        class Item(BaseModel):
            name: str
            value: int

        if media_type is None and not embed:

            @app.post(url)
            async def create_item(item: Item):
                return {"msg": item.value}

        elif media_type is None and embed:

            @app.post(url)
            async def create_item(item: Item = Body(..., embed=embed)):
                return {"msg": item.value}

        elif media_type is not None and not embed:

            @app.post(url)
            async def create_item(item: Item = Body(..., media_type=media_type)):
                return {"msg": item.value}

        else:

            @app.post(url)
            async def create_item(
                item: Item = Body(..., media_type=media_type, embed=embed)
            ):
                return {"msg": item.value}

        client = TestClient(app)
        if data is not None:
            response = getattr(client, mode)(target, json=data)
            return response.json(), response.status_code
        else:
            response = getattr(client, mode)(target)
            return response.json(), response.status_code


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_test(
            url="/test",
            target="/openapi.json",
            mode="get",
            media_type="application/vnd.api+json",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/vnd.api+json",
            response["paths"]["/test"]["post"]["requestBody"]["content"],
        )

    def test_diversity_2(self):
        response, status_code = self.run_test(
            url="/test",
            target="/openapi.json",
            mode="get",
            media_type="abc",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "abc",
            response["paths"]["/test"]["post"]["requestBody"]["content"],
        )

    def test_diversity_3(self):
        response, status_code = self.run_test(
            url="/test2",
            target="/openapi.json",
            mode="get",
            media_type="application/vnd.api+json",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/vnd.api+json",
            response["paths"]["/test2"]["post"]["requestBody"]["content"],
        )

    def test_diversity_4(self):
        response, status_code = self.run_test(
            url="/test2",
            target="/openapi.json",
            mode="get",
            media_type="abc",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "abc",
            response["paths"]["/test2"]["post"]["requestBody"]["content"],
        )

    def test_diversity_5(self):
        response, status_code = self.run_test(
            url="/test",
            target="/openapi.json",
            mode="get",
            media_type="test",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "test",
            response["paths"]["/test"]["post"]["requestBody"]["content"],
        )

    def test_diversity_6(self):
        response, status_code = self.run_test(
            url="/abc",
            target="/openapi.json",
            mode="get",
            media_type="abc",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "abc",
            response["paths"]["/abc"]["post"]["requestBody"]["content"],
        )

    def test_diversity_7(self):
        response, status_code = self.run_test(
            url="/test2",
            target="/openapi.json",
            mode="get",
            media_type="test",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "test",
            response["paths"]["/test2"]["post"]["requestBody"]["content"],
        )

    def test_diversity_8(self):
        response, status_code = self.run_test(
            url="/test2",
            target="/openapi.json",
            mode="get",
            media_type="test2",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "test2",
            response["paths"]["/test2"]["post"]["requestBody"]["content"],
        )

    def test_diversity_9(self):
        response, status_code = self.run_test(
            url="/test/a",
            target="/openapi.json",
            mode="get",
            media_type="application/vnd.json",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/vnd.json",
            response["paths"]["/test/a"]["post"]["requestBody"]["content"],
        )

    def test_diversity_10(self):
        response, status_code = self.run_test(
            url="/test/b",
            target="/openapi.json",
            mode="get",
            media_type="application/vnd.json",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/vnd.json",
            response["paths"]["/test/b"]["post"]["requestBody"]["content"],
        )


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_test(
            url="/test",
            target="/openapi.json",
            mode="post",
            media_type="application/.api+vnd.json",
        )
        self.assertEqual(405, status_code)
        self.assertEqual({"detail": "Method Not Allowed"}, response)

    def test_diversity_2(self):
        response, status_code = self.run_test(
            url="/test",
            target="/test",
            mode="get",
            media_type="application/.api+vnd.json",
        )
        self.assertEqual(405, status_code)
        self.assertEqual({"detail": "Method Not Allowed"}, response)

    def test_diversity_3(self):
        response, status_code = self.run_test(
            url="/test",
            target="/openapi.json",
            mode="get",
            media_type="application/json",
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/json",
            response["paths"]["/test"]["post"]["requestBody"]["content"],
        )

    def test_diversity_4(self):
        response, status_code = self.run_test(
            url="/test",
            target="/test",
            mode="post",
            media_type="application/.api+vnd.json",
            data={"name": "test", "value": 5},
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": 5}, response)

    def test_diversity_5(self):
        response, status_code = self.run_test(
            url="/test2",
            target="/openapi.json",
            mode="get",
            media_type="application/json",
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/json",
            response["paths"]["/test2"]["post"]["requestBody"]["content"],
        )

    def test_diversity_6(self):
        response, status_code = self.run_test(
            url="/test",
            target="/test",
            mode="post",
            media_type="application/.api+vnd.json",
            data={"name": "test2", "value": 90},
        )
        self.assertEqual(200, status_code)
        self.assertEqual({"msg": 90}, response)

    def test_diversity_7(self):
        response, status_code = self.run_test(
            url="/test",
            target="/openapi.json",
            mode="get",
            media_type="application/vnd.api+json",
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/vnd.api+json",
            response["paths"]["/test"]["post"]["requestBody"]["content"],
        )

    def test_diversity_8(self):
        response, status_code = self.run_test(
            url="/test/b",
            target="/openapi.json",
            mode="get",
            media_type="application/vnd.json",
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/vnd.json",
            response["paths"]["/test/b"]["post"]["requestBody"]["content"],
        )

    def test_diversity_9(self):
        response, status_code = self.run_test(
            url="/test/b",
            target="/openapi.json",
            mode="get",
            media_type="application/json",
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/json",
            response["paths"]["/test/b"]["post"]["requestBody"]["content"],
        )

    def test_diversity_10(self):
        response, status_code = self.run_test(
            url="/test/b",
            target="/openapi.json",
            mode="get",
            embed=True,
        )
        self.assertEqual(200, status_code)
        self.assertIn(
            "application/json",
            response["paths"]["/test/b"]["post"]["requestBody"]["content"],
        )
