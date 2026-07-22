import unittest
from fastapi import FastAPI
from pydantic import BaseModel
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(path, marker, fill):
        app = FastAPI()

        class SubModel(BaseModel):
            marker: str = 'defaultmarker'

        class Model(BaseModel):
            x: int = None
            sub: SubModel
        if fill:

            @app.get('/' + path, response_model=Model, response_model_skip_defaults=True)
            def get():
                return Model(x=5, sub={'marker': marker})
        else:

            @app.get('/' + path, response_model=Model, response_model_skip_defaults=True)
            def get():
                return Model(sub={})
        return TestClient(app).get('/' + path).json()

    def test_diversity_1(self):
        body = self.run_test('zilgjul', 'ziw', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_2(self):
        body = self.run_test('hgktea', 'gdngnhz', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_3(self):
        body = self.run_test('vdgdpvq', 'yhjz', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_4(self):
        body = self.run_test('ynmkgjf', 'simia', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_5(self):
        body = self.run_test('thipur', 'pgeek', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_6(self):
        body = self.run_test('klkyk', 'rbnr', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_7(self):
        body = self.run_test('vnshaeqx', 'ijrhw', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_8(self):
        body = self.run_test('dszqv', 'fnm', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_9(self):
        body = self.run_test('yskwv', 'ecgpfu', False)
        self.assertEqual({'sub': {}}, body)

    def test_diversity_10(self):
        body = self.run_test('auzs', 'vue', False)
        self.assertEqual({'sub': {}}, body)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(path, marker, fill):
        app = FastAPI()

        class SubModel(BaseModel):
            marker: str = 'defaultmarker'

        class Model(BaseModel):
            x: int = None
            sub: SubModel
        if fill:

            @app.get('/' + path, response_model=Model, response_model_skip_defaults=True)
            def get():
                return Model(x=5, sub={'marker': marker})
        else:

            @app.get('/' + path, response_model=Model, response_model_skip_defaults=True)
            def get():
                return Model(sub={})
        return TestClient(app).get('/' + path).json()

    def test_diversity_1(self):
        body = self.run_test('srkyk', 'kuziihgm', True)
        self.assertEqual('kuziihgm', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_2(self):
        body = self.run_test('mmwxirl', 'lyz', True)
        self.assertEqual('lyz', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_3(self):
        body = self.run_test('riws', 'ugflz', True)
        self.assertEqual('ugflz', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_4(self):
        body = self.run_test('qdwip', 'arhnr', True)
        self.assertEqual('arhnr', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_5(self):
        body = self.run_test('bqzzwwgj', 'zdo', True)
        self.assertEqual('zdo', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_6(self):
        body = self.run_test('fdrsdvlb', 'tdznwpfd', True)
        self.assertEqual('tdznwpfd', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_7(self):
        body = self.run_test('ascqqh', 'yiulqf', True)
        self.assertEqual('yiulqf', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_8(self):
        body = self.run_test('ypjt', 'xiq', True)
        self.assertEqual('xiq', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_9(self):
        body = self.run_test('zainnkqa', 'qdcjgp', True)
        self.assertEqual('qdcjgp', body['sub']['marker'])
        self.assertEqual(5, body['x'])

    def test_diversity_10(self):
        body = self.run_test('enip', 'ygybj', True)
        self.assertEqual('ygybj', body['sub']['marker'])
        self.assertEqual(5, body['x'])
