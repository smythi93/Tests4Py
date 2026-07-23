import unittest
from decimal import Decimal
from fastapi import FastAPI
from pydantic import BaseModel, condecimal
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(name, price, age):
        app = FastAPI()

        class Item(BaseModel):
            name: str
            price: float = None
            age: condecimal(gt=Decimal(0.0))

        @app.post('/item')
        def post_item(item: Item):
            return {'item': item}
        client = TestClient(app)
        return client.post('/item', json={'name': name, 'price': price, 'age': age})

    def test_diversity_1(self):
        response = self.run_test('bskkh', 95.7, -11)
        self.assertEqual(422, response.status_code)

    def test_diversity_2(self):
        response = self.run_test('youaeq', 69.9, -32)
        self.assertEqual(422, response.status_code)

    def test_diversity_3(self):
        response = self.run_test('mpmqarb', 30.9, -51)
        self.assertEqual(422, response.status_code)

    def test_diversity_4(self):
        response = self.run_test('wjz', 94.2, -5)
        self.assertEqual(422, response.status_code)

    def test_diversity_5(self):
        response = self.run_test('kitmlp', 89.3, -33)
        self.assertEqual(422, response.status_code)

    def test_diversity_6(self):
        response = self.run_test('zde', 60.8, -87)
        self.assertEqual(422, response.status_code)

    def test_diversity_7(self):
        response = self.run_test('rbw', 57.4, -50)
        self.assertEqual(422, response.status_code)

    def test_diversity_8(self):
        response = self.run_test('dkbz', 90.2, -86)
        self.assertEqual(422, response.status_code)

    def test_diversity_9(self):
        response = self.run_test('sidb', 92.2, -90)
        self.assertEqual(422, response.status_code)

    def test_diversity_10(self):
        response = self.run_test('enx', 61.7, -9)
        self.assertEqual(422, response.status_code)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(name, price, age):
        app = FastAPI()

        class Item(BaseModel):
            name: str
            price: float = None
            age: condecimal(gt=Decimal(0.0))

        @app.post('/item')
        def post_item(item: Item):
            return {'item': item}
        client = TestClient(app)
        return client.post('/item', json={'name': name, 'price': price, 'age': age})

    def test_diversity_1(self):
        response = self.run_test('nwnwafez', 47.2, 21)
        self.assertEqual(200, response.status_code)

    def test_diversity_2(self):
        response = self.run_test('zujuksx', 65.9, 16)
        self.assertEqual(200, response.status_code)

    def test_diversity_3(self):
        response = self.run_test('rvacbzpr', 72.7, 47)
        self.assertEqual(200, response.status_code)

    def test_diversity_4(self):
        response = self.run_test('qpl', 6.3, 39)
        self.assertEqual(200, response.status_code)

    def test_diversity_5(self):
        response = self.run_test('ddsohl', 55.2, 99)
        self.assertEqual(200, response.status_code)

    def test_diversity_6(self):
        response = self.run_test('jwylgbrbb', 71.5, 45)
        self.assertEqual(200, response.status_code)

    def test_diversity_7(self):
        response = self.run_test('gwm', 63.3, 58)
        self.assertEqual(200, response.status_code)

    def test_diversity_8(self):
        response = self.run_test('jnvz', 32.7, 36)
        self.assertEqual(200, response.status_code)

    def test_diversity_9(self):
        response = self.run_test('inql', 21.9, 33)
        self.assertEqual(200, response.status_code)

    def test_diversity_10(self):
        response = self.run_test('sad', 37.9, 63)
        self.assertEqual(200, response.status_code)