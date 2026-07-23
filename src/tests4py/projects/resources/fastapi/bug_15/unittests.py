import unittest
from fastapi import APIRouter, FastAPI
try:
    from fastapi import WebSocket
except ImportError:
    from starlette.websockets import WebSocket
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(path, message, via_include):
        app = FastAPI()
        if via_include:
            router = APIRouter()

            @router.websocket_route(path)
            async def idx(websocket: WebSocket):
                await websocket.accept()
                await websocket.send_text(message)
                await websocket.close()
            app.include_router(router)
        else:

            @app.websocket_route(path)
            async def idx2(websocket: WebSocket):
                await websocket.accept()
                await websocket.send_text(message)
                await websocket.close()
        client = TestClient(app)
        try:
            with client.websocket_connect(path) as ws:
                return ws.receive_text()
        except Exception as e:
            return 'ERROR:' + type(e).__name__

    def test_diversity_1(self):
        received = self.run_test('/sspmkvct', 'hzwg', True)
        self.assertEqual('hzwg', received)

    def test_diversity_2(self):
        received = self.run_test('/zpivsu', 'maamfx', True)
        self.assertEqual('maamfx', received)

    def test_diversity_3(self):
        received = self.run_test('/gtxnichh', 'ilousj', True)
        self.assertEqual('ilousj', received)

    def test_diversity_4(self):
        received = self.run_test('/hxddaixw', 'cnz', True)
        self.assertEqual('cnz', received)

    def test_diversity_5(self):
        received = self.run_test('/hrdrpejk', 'ykcalutd', True)
        self.assertEqual('ykcalutd', received)

    def test_diversity_6(self):
        received = self.run_test('/cmjusr', 'zos', True)
        self.assertEqual('zos', received)

    def test_diversity_7(self):
        received = self.run_test('/stqoqwwl', 'xglcfgqa', True)
        self.assertEqual('xglcfgqa', received)

    def test_diversity_8(self):
        received = self.run_test('/vxzkw', 'vsxbfsq', True)
        self.assertEqual('vsxbfsq', received)

    def test_diversity_9(self):
        received = self.run_test('/xhzam', 'yhhil', True)
        self.assertEqual('yhhil', received)

    def test_diversity_10(self):
        received = self.run_test('/pvigp', 'ocwvx', True)
        self.assertEqual('ocwvx', received)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(path, message, via_include):
        app = FastAPI()
        if via_include:
            router = APIRouter()

            @router.websocket_route(path)
            async def idx(websocket: WebSocket):
                await websocket.accept()
                await websocket.send_text(message)
                await websocket.close()
            app.include_router(router)
        else:

            @app.websocket_route(path)
            async def idx2(websocket: WebSocket):
                await websocket.accept()
                await websocket.send_text(message)
                await websocket.close()
        client = TestClient(app)
        try:
            with client.websocket_connect(path) as ws:
                return ws.receive_text()
        except Exception as e:
            return 'ERROR:' + type(e).__name__

    def test_diversity_1(self):
        received = self.run_test('/jrjetmph', 'maqkgwz', False)
        self.assertEqual('maqkgwz', received)

    def test_diversity_2(self):
        received = self.run_test('/rjddsgbj', 'jmumdfpf', False)
        self.assertEqual('jmumdfpf', received)

    def test_diversity_3(self):
        received = self.run_test('/bcfryqk', 'tylcfzei', False)
        self.assertEqual('tylcfzei', received)

    def test_diversity_4(self):
        received = self.run_test('/wlrvnzx', 'xiq', False)
        self.assertEqual('xiq', received)

    def test_diversity_5(self):
        received = self.run_test('/ijdd', 'ujunoh', False)
        self.assertEqual('ujunoh', received)

    def test_diversity_6(self):
        received = self.run_test('/fue', 'qcuqt', False)
        self.assertEqual('qcuqt', received)

    def test_diversity_7(self):
        received = self.run_test('/kgkfxlld', 'hkypqps', False)
        self.assertEqual('hkypqps', received)

    def test_diversity_8(self):
        received = self.run_test('/ekl', 'xbawxbh', False)
        self.assertEqual('xbawxbh', received)

    def test_diversity_9(self):
        received = self.run_test('/vmgif', 'uvj', False)
        self.assertEqual('uvj', received)

    def test_diversity_10(self):
        received = self.run_test('/ydll', 'vqfcqj', False)
        self.assertEqual('vqfcqj', received)
