import unittest
from fastapi import FastAPI
from pydantic import BaseModel, Field
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(alias, value, price):
        app = FastAPI()
        if alias:

            class Item(BaseModel):
                name: str = Field(..., alias=alias)
                price: float = None
            item = Item(**{alias: value, 'price': price})
        else:

            class Item(BaseModel):
                name: str = None
                price: float = None
            item = Item(name=value, price=price)

        @app.get('/item', response_model=Item)
        def get_item():
            return item
        client = TestClient(app)
        response = client.get('/item')
        return (response.status_code, response.json())

    def test_diversity_1(self):
        status, body = self.run_test('ykyjs', 'tpdxg', 44.6)
        self.assertEqual(200, status)
        self.assertEqual({'ykyjs': 'tpdxg', 'price': 44.6}, body)

    def test_diversity_2(self):
        status, body = self.run_test('scwyueh', 'ipaflliqx', 93.3)
        self.assertEqual(200, status)
        self.assertEqual({'scwyueh': 'ipaflliqx', 'price': 93.3}, body)

    def test_diversity_3(self):
        status, body = self.run_test('icyf', 'ljdi', 43.5)
        self.assertEqual(200, status)
        self.assertEqual({'icyf': 'ljdi', 'price': 43.5}, body)

    def test_diversity_4(self):
        status, body = self.run_test('iivrpn', 'rfvnqxfei', 57.2)
        self.assertEqual(200, status)
        self.assertEqual({'iivrpn': 'rfvnqxfei', 'price': 57.2}, body)

    def test_diversity_5(self):
        status, body = self.run_test('szsv', 'sdhdqthk', 97.4)
        self.assertEqual(200, status)
        self.assertEqual({'szsv': 'sdhdqthk', 'price': 97.4}, body)

    def test_diversity_6(self):
        status, body = self.run_test('vjuhqlcf', 'isv', 21.2)
        self.assertEqual(200, status)
        self.assertEqual({'vjuhqlcf': 'isv', 'price': 21.2}, body)

    def test_diversity_7(self):
        status, body = self.run_test('euvhdygjz', 'dqqwoq', 43.1)
        self.assertEqual(200, status)
        self.assertEqual({'euvhdygjz': 'dqqwoq', 'price': 43.1}, body)

    def test_diversity_8(self):
        status, body = self.run_test('ojetbtj', 'tplaevpds', 2.9)
        self.assertEqual(200, status)
        self.assertEqual({'ojetbtj': 'tplaevpds', 'price': 2.9}, body)

    def test_diversity_9(self):
        status, body = self.run_test('rqmr', 'awnij', 35.8)
        self.assertEqual(200, status)
        self.assertEqual({'rqmr': 'awnij', 'price': 35.8}, body)

    def test_diversity_10(self):
        status, body = self.run_test('oiy', 'cil', 55.4)
        self.assertEqual(200, status)
        self.assertEqual({'oiy': 'cil', 'price': 55.4}, body)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(alias, value, price):
        app = FastAPI()
        if alias:

            class Item(BaseModel):
                name: str = Field(..., alias=alias)
                price: float = None
            item = Item(**{alias: value, 'price': price})
        else:

            class Item(BaseModel):
                name: str = None
                price: float = None
            item = Item(name=value, price=price)

        @app.get('/item', response_model=Item)
        def get_item():
            return item
        client = TestClient(app)
        response = client.get('/item')
        return (response.status_code, response.json())

    def test_diversity_1(self):
        status, body = self.run_test(None, 'xjvnmwehq', 54.6)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'xjvnmwehq', 'price': 54.6}, body)

    def test_diversity_2(self):
        status, body = self.run_test(None, 'rpsbcmemh', 23.2)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'rpsbcmemh', 'price': 23.2}, body)

    def test_diversity_3(self):
        status, body = self.run_test(None, 'dtmaqfuitv', 17.4)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'dtmaqfuitv', 'price': 17.4}, body)

    def test_diversity_4(self):
        status, body = self.run_test(None, 'kcum', 85.8)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'kcum', 'price': 85.8}, body)

    def test_diversity_5(self):
        status, body = self.run_test(None, 'omf', 21.1)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'omf', 'price': 21.1}, body)

    def test_diversity_6(self):
        status, body = self.run_test(None, 'vjuhrno', 92.0)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'vjuhrno', 'price': 92.0}, body)

    def test_diversity_7(self):
        status, body = self.run_test(None, 'wfxy', 48.5)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'wfxy', 'price': 48.5}, body)

    def test_diversity_8(self):
        status, body = self.run_test(None, 'xjhqk', 34.6)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'xjhqk', 'price': 34.6}, body)

    def test_diversity_9(self):
        status, body = self.run_test(None, 'pzjtk', 12.8)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'pzjtk', 'price': 12.8}, body)

    def test_diversity_10(self):
        status, body = self.run_test(None, 'bjyvx', 80.0)
        self.assertEqual(200, status)
        self.assertEqual({'name': 'bjyvx', 'price': 80.0}, body)