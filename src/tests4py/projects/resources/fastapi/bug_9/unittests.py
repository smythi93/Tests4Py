import unittest
from fastapi import Body, FastAPI
from pydantic import BaseModel
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(path, custom):
        app = FastAPI()

        class Product(BaseModel):
            name: str
            price: float
        if custom:

            @app.post('/' + path)
            async def create(data: Product=Body(..., media_type='application/vnd.api+json', embed=True)):
                return data
        else:

            @app.post('/' + path)
            async def create(data: Product):
                return data
        schema = TestClient(app).get('/openapi.json').json()
        content = schema['paths']['/' + path]['post']['requestBody']['content']
        return list(content.keys())

    def test_diversity_1(self):
        media = self.run_test('axlffd', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_2(self):
        media = self.run_test('ehm', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_3(self):
        media = self.run_test('muoxda', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_4(self):
        media = self.run_test('agwsxdod', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_5(self):
        media = self.run_test('vkx', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_6(self):
        media = self.run_test('pakgk', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_7(self):
        media = self.run_test('fdtpzvx', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_8(self):
        media = self.run_test('zia', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_9(self):
        media = self.run_test('autspbn', True)
        self.assertIn('application/vnd.api+json', media)

    def test_diversity_10(self):
        media = self.run_test('zzfz', True)
        self.assertIn('application/vnd.api+json', media)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(path, custom):
        app = FastAPI()

        class Product(BaseModel):
            name: str
            price: float
        if custom:

            @app.post('/' + path)
            async def create(data: Product=Body(..., media_type='application/vnd.api+json', embed=True)):
                return data
        else:

            @app.post('/' + path)
            async def create(data: Product):
                return data
        schema = TestClient(app).get('/openapi.json').json()
        content = schema['paths']['/' + path]['post']['requestBody']['content']
        return list(content.keys())

    def test_diversity_1(self):
        media = self.run_test('kfdn', False)
        self.assertIn('application/json', media)

    def test_diversity_2(self):
        media = self.run_test('xlxddcyb', False)
        self.assertIn('application/json', media)

    def test_diversity_3(self):
        media = self.run_test('wuit', False)
        self.assertIn('application/json', media)

    def test_diversity_4(self):
        media = self.run_test('nej', False)
        self.assertIn('application/json', media)

    def test_diversity_5(self):
        media = self.run_test('ytbqyccq', False)
        self.assertIn('application/json', media)

    def test_diversity_6(self):
        media = self.run_test('fffv', False)
        self.assertIn('application/json', media)

    def test_diversity_7(self):
        media = self.run_test('joabvj', False)
        self.assertIn('application/json', media)

    def test_diversity_8(self):
        media = self.run_test('oxi', False)
        self.assertIn('application/json', media)

    def test_diversity_9(self):
        media = self.run_test('koixdhk', False)
        self.assertIn('application/json', media)

    def test_diversity_10(self):
        media = self.run_test('kmd', False)
        self.assertIn('application/json', media)