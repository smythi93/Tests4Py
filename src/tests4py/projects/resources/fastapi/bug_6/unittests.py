import unittest

# noinspection PyUnresolvedReferences
from fastapi import FastAPI, Form

try:
    # noinspection PyUnresolvedReferences
    from fastapi.testclient import TestClient
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.testclient import TestClient


class DefaultTest(unittest.TestCase):
    @staticmethod
    def run_test(
        mode="post",
        url="/",
        data=None,
    ):
        app = FastAPI()

        @app.post("/form/python-list")
        def post_form_param_list(items: list = Form(...)):
            return items

        @app.post("/form/python-set")
        def post_form_param_set(items: set = Form(...)):
            return items

        @app.post("/form/python-tuple")
        def post_form_param_tuple(items: tuple = Form(...)):
            return items

        @app.post("/form/python-int-1")
        def post_form_param_int(items: int = Form(1)):
            return items

        @app.post("/form/python-int-2")
        def post_form_param_int(items: int = Form(2)):
            return items

        @app.post("/form/python-str-1")
        def post_form_param_str(items: str = Form("test")):
            return items

        @app.post("/form/python-str-2")
        def post_form_param_str(items: str = Form("post")):
            return items

        client = TestClient(app)

        if data is not None:
            response = getattr(client, mode)(url, json=data)
            return response.json(), response.status_code
        else:
            response = getattr(client, mode)(url)
            return response.json(), response.status_code


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_test(
            "post", "/form/python-list", {"items": [1, 2, 3]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual([1, 2, 3], response)

    def test_diversity_2(self):
        response, status_code = self.run_test(
            "post", "/form/python-set", {"items": [1, 2, 3]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({1, 2, 3}, response)

    def test_diversity_3(self):
        response, status_code = self.run_test(
            "post", "/form/python-tuple", {"items": [1, 2, 3]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual([1, 2, 3], response)

    def test_diversity_4(self):
        response, status_code = self.run_test(
            "post", "/form/python-list", {"items": ["1", "2", "3"]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual(["1", "2", "3"], response)

    def test_diversity_5(self):
        response, status_code = self.run_test(
            "post", "/form/python-set", {"items": ["1", "2", "3"]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({"1", "2", "3"}, response)

    def test_diversity_6(self):
        response, status_code = self.run_test(
            "post", "/form/python-tuple", {"items": ["1", "2", "3"]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual(["1", "2", "3"], response)

    def test_diversity_7(self):
        response, status_code = self.run_test(
            "post", "/form/python-list", {"items": [1, "2", "3"]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual([1, "2", "3"], response)

    def test_diversity_8(self):
        response, status_code = self.run_test(
            "post", "/form/python-set", {"items": [1, "2", "3"]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual({1, "2", "3"}, response)

    def test_diversity_9(self):
        response, status_code = self.run_test(
            "post", "/form/python-tuple", {"items": [1, "2", "3"]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual([1, "2", "3"], response)

    def test_diversity_10(self):
        response, status_code = self.run_test(
            "post", "/form/python-list", {"items": [1, 2, 3, "1", "2", "3"]}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual([1, 2, 3, "1", "2", "3"], response)


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        response, status_code = self.run_test(
            "get", "/form/python-list", {"items": [1, 2, 3]}
        )
        self.assertEqual({"detail": "Method Not Allowed"}, response)
        self.assertEqual(status_code, 405)

    def test_diversity_2(self):
        response, status_code = self.run_test(
            "post", "/form/python-int-1", {"items": 1}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual(1, response)

    def test_diversity_3(self):
        response, status_code = self.run_test(
            "post", "/form/python-int-2", {"items": 2}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual(2, response)

    def test_diversity_4(self):
        response, status_code = self.run_test("post", "/form/python-int-1")
        self.assertEqual(status_code, 200)
        self.assertEqual(1, response)

    def test_diversity_5(self):
        response, status_code = self.run_test("post", "/form/python-int-2")
        self.assertEqual(status_code, 200)
        self.assertEqual(2, response)

    def test_diversity_6(self):
        response, status_code = self.run_test(
            "post", "/form/python-str-1", {"items": "test"}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual("test", response)

    def test_diversity_7(self):
        response, status_code = self.run_test(
            "post", "/form/python-str-2", {"items": "post"}
        )
        self.assertEqual(status_code, 200)
        self.assertEqual("post", response)

    def test_diversity_8(self):
        response, status_code = self.run_test("post", "/form/python-str-1")
        self.assertEqual(status_code, 200)
        self.assertEqual("test", response)

    def test_diversity_9(self):
        response, status_code = self.run_test("post", "/form/python-str-2")
        self.assertEqual(status_code, 200)
        self.assertEqual("post", response)

    def test_diversity_10(self):
        response, status_code = self.run_test("get", "/form/python-int-1", {"items": 1})
        self.assertEqual({"detail": "Method Not Allowed"}, response)
        self.assertEqual(status_code, 405)
