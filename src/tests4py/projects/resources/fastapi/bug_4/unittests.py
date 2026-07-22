import unittest
from fastapi import Depends, FastAPI
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(prefix, with_dependency):
        app = FastAPI()

        async def check(item_id: int):
            return True
        path = '/' + prefix + '/{item_id}'
        if with_dependency:

            @app.get(path, dependencies=[Depends(check)])
            async def read(item_id: int):
                return {'item_id': item_id}
        else:

            @app.get(path)
            async def read(item_id: int):
                return {'item_id': item_id}
        schema = TestClient(app).get('/openapi.json').json()
        params = schema['paths'][path]['get']['parameters']
        return [p['name'] for p in params]

    def test_diversity_1(self):
        names = self.run_test('itzyyx', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_2(self):
        names = self.run_test('vebpjstb', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_3(self):
        names = self.run_test('eljy', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_4(self):
        names = self.run_test('huadr', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_5(self):
        names = self.run_test('zivvf', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_6(self):
        names = self.run_test('mnujsk', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_7(self):
        names = self.run_test('ofd', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_8(self):
        names = self.run_test('bapg', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_9(self):
        names = self.run_test('ghaaw', True)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_10(self):
        names = self.run_test('ndl', True)
        self.assertEqual(len(names), len(set(names)))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(prefix, with_dependency):
        app = FastAPI()

        async def check(item_id: int):
            return True
        path = '/' + prefix + '/{item_id}'
        if with_dependency:

            @app.get(path, dependencies=[Depends(check)])
            async def read(item_id: int):
                return {'item_id': item_id}
        else:

            @app.get(path)
            async def read(item_id: int):
                return {'item_id': item_id}
        schema = TestClient(app).get('/openapi.json').json()
        params = schema['paths'][path]['get']['parameters']
        return [p['name'] for p in params]

    def test_diversity_1(self):
        names = self.run_test('agpwbzuf', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_2(self):
        names = self.run_test('ctxpmwh', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_3(self):
        names = self.run_test('guo', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_4(self):
        names = self.run_test('ipzrqekq', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_5(self):
        names = self.run_test('qhh', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_6(self):
        names = self.run_test('jnamx', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_7(self):
        names = self.run_test('rbhzajxl', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_8(self):
        names = self.run_test('gghyhmx', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_9(self):
        names = self.run_test('vefino', False)
        self.assertEqual(len(names), len(set(names)))

    def test_diversity_10(self):
        names = self.run_test('gjodez', False)
        self.assertEqual(len(names), len(set(names)))