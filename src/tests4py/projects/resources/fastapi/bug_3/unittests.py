import unittest

# noinspection PyUnresolvedReferences
from fastapi import APIRouter, Depends, FastAPI

try:
    # noinspection PyUnresolvedReferences
    from fastapi import WebSocket
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.websockets import WebSocket

try:
    # noinspection PyUnresolvedReferences
    from fastapi.testclient import TestClient
except ImportError:
    # noinspection PyUnresolvedReferences
    from starlette.testclient import TestClient


class DefaultTest(unittest.TestCase):
    @staticmethod
    def run_test(mode="get", url="/", data=None, depend=None, override=None):
        app = FastAPI()
        router = APIRouter()

        depend = depend or "Dependency"

        async def dependency():
            return depend

        @app.get("/get", response_model=str)
        def get_valid():
            return f"get_{depend}"

        @app.post("/post", response_model=str)
        def get_valid():
            return f"post_{depend}"

        @router.websocket("/")
        async def router_ws_decorator_depends(
            websocket_: WebSocket, data_=Depends(dependency)
        ):
            await websocket_.accept()
            await websocket_.send_text(data_)
            await websocket_.close()

        if override:
            app.dependency_overrides[dependency] = lambda: override

        app.include_router(router, prefix="/router")

        client = TestClient(app)

        if mode == "websocket":
            with client.websocket_connect(url) as websocket:
                return websocket.receive_text(), 200
        elif data is not None:
            response = getattr(client, mode)(url, json=data)
            return response.json(), response.status_code
        else:
            response = getattr(client, mode)(url)
            return response.json(), response.status_code


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        response, status = self.run_test("websocket", "/router/", override="Overridden")
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)

    def test_diversity_2(self):
        response, status = self.run_test(
            "websocket", "/router/", override="Overridden2"
        )
        self.assertEqual("Overridden2", response)
        self.assertEqual(200, status)

    def test_diversity_3(self):
        response, status = self.run_test(
            "websocket", "/router/", data=[1, 2, 3], override="Overridden"
        )
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)

    def test_diversity_4(self):
        response, status = self.run_test(
            "websocket", "/router/", data={"t": "test"}, override="Overridden"
        )
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)

    def test_diversity_5(self):
        response, status = self.run_test(
            "websocket", "/router/", data="test", override="Overridden"
        )
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)

    def test_diversity_6(self):
        response, status = self.run_test("websocket", "/router/", override="Overridden")
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)

    def test_diversity_7(self):
        response, status = self.run_test(
            "websocket", "/router/", override="Overridden2"
        )
        self.assertEqual("Overridden2", response)
        self.assertEqual(200, status)

    def test_diversity_8(self):
        response, status = self.run_test(
            "websocket", "/router/", data=[1, 2, 3], override="Overridden"
        )
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)

    def test_diversity_9(self):
        response, status = self.run_test(
            "websocket", "/router/", data={"t": "test"}, override="Overridden"
        )
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)

    def test_diversity_10(self):
        response, status = self.run_test(
            "websocket", "/router/", data="test", override="Overridden"
        )
        self.assertEqual("Overridden", response)
        self.assertEqual(200, status)


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        response, status = self.run_test("websocket", "/router/")
        self.assertEqual("Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_2(self):
        response, status = self.run_test("websocket", "/router/", depend="Dependency2")
        self.assertEqual("Dependency2", response)
        self.assertEqual(200, status)

    def test_diversity_3(self):
        response, status = self.run_test("websocket", "/router/", data=[1, 2, 3])
        self.assertEqual("Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_4(self):
        response, status = self.run_test("websocket", "/router/", data="test_1")
        self.assertEqual("Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_5(self):
        response, status = self.run_test("websocket", "/router/", data="test")
        self.assertEqual("Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_6(self):
        response, status = self.run_test("get", "/get", override="Overridden")
        self.assertEqual("get_Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_7(self):
        response, status = self.run_test("post", "/post", override="Overridden")
        self.assertEqual("post_Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_8(self):
        response, status = self.run_test(
            "get", "/get", data="test", override="Overridden"
        )
        self.assertEqual("get_Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_9(self):
        response, status = self.run_test(
            "post", "/post", data="test", override="Overridden"
        )
        self.assertEqual("post_Dependency", response)
        self.assertEqual(200, status)

    def test_diversity_10(self):
        response, status = self.run_test("post", "/get", override="Overridden")
        self.assertEqual({"detail": "Method Not Allowed"}, response)
        self.assertEqual(405, status)
