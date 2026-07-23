import unittest
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(path, body, union):
        app = FastAPI()

        class ItemA(BaseModel):
            name: str = None

        class ItemB(BaseModel):
            price: int
        if union:

            @app.post('/' + path)
            def save(item: Union[ItemB, ItemA]):
                return {'item': item}
        else:

            @app.post('/' + path)
            def save(item: ItemB):
                return {'item': item}
        resp = TestClient(app).post('/' + path, json=body)
        return (resp.status_code, resp.json())

    def test_diversity_1(self):
        status, body = self.run_test('nfz', {'price': 212}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 212}}, body)

    def test_diversity_2(self):
        status, body = self.run_test('uifuyob', {'price': 946}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 946}}, body)

    def test_diversity_3(self):
        status, body = self.run_test('abi', {'price': 486}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 486}}, body)

    def test_diversity_4(self):
        status, body = self.run_test('ytmfvcd', {'price': 416}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 416}}, body)

    def test_diversity_5(self):
        status, body = self.run_test('ikwlapm', {'price': 484}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 484}}, body)

    def test_diversity_6(self):
        status, body = self.run_test('kgogo', {'price': 578}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 578}}, body)

    def test_diversity_7(self):
        status, body = self.run_test('uum', {'price': 726}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 726}}, body)

    def test_diversity_8(self):
        status, body = self.run_test('qtymmds', {'price': 488}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 488}}, body)

    def test_diversity_9(self):
        status, body = self.run_test('qqhz', {'price': 539}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 539}}, body)

    def test_diversity_10(self):
        status, body = self.run_test('yobw', {'price': 697}, True)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 697}}, body)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(path, body, union):
        app = FastAPI()

        class ItemA(BaseModel):
            name: str = None

        class ItemB(BaseModel):
            price: int
        if union:

            @app.post('/' + path)
            def save(item: Union[ItemB, ItemA]):
                return {'item': item}
        else:

            @app.post('/' + path)
            def save(item: ItemB):
                return {'item': item}
        resp = TestClient(app).post('/' + path, json=body)
        return (resp.status_code, resp.json())

    def test_diversity_1(self):
        status, body = self.run_test('lday', {'price': 482}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 482}}, body)

    def test_diversity_2(self):
        status, body = self.run_test('wlxtdcwp', {'price': 227}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 227}}, body)

    def test_diversity_3(self):
        status, body = self.run_test('kpd', {'price': 430}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 430}}, body)

    def test_diversity_4(self):
        status, body = self.run_test('ktbvqwkn', {'price': 208}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 208}}, body)

    def test_diversity_5(self):
        status, body = self.run_test('xcspqir', {'price': 645}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 645}}, body)

    def test_diversity_6(self):
        status, body = self.run_test('ipjcw', {'price': 456}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 456}}, body)

    def test_diversity_7(self):
        status, body = self.run_test('hkrny', {'price': 698}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 698}}, body)

    def test_diversity_8(self):
        status, body = self.run_test('xmp', {'price': 209}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 209}}, body)

    def test_diversity_9(self):
        status, body = self.run_test('ciesemkf', {'price': 770}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 770}}, body)

    def test_diversity_10(self):
        status, body = self.run_test('lpn', {'price': 207}, False)
        self.assertEqual(200, status)
        self.assertEqual({'item': {'price': 207}}, body)
