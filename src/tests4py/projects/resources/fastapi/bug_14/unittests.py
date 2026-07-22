import unittest
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(path, kind):
        app = FastAPI()
        if kind == 'dict':

            class M(BaseModel):
                items: Dict[str, int]
        else:

            class M(BaseModel):
                name: str

        @app.post('/' + path)
        def foo(m: M):
            return m
        schema = TestClient(app).get('/openapi.json').json()
        return schema['components']['schemas']['M']['properties']

    def test_diversity_1(self):
        props = self.run_test('ozfxr', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_2(self):
        props = self.run_test('lvlagtrq', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_3(self):
        props = self.run_test('effe', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_4(self):
        props = self.run_test('pfnosvw', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_5(self):
        props = self.run_test('tyce', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_6(self):
        props = self.run_test('ubtkwed', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_7(self):
        props = self.run_test('sxuxoqh', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_8(self):
        props = self.run_test('xpkoozy', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_9(self):
        props = self.run_test('wstsgm', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

    def test_diversity_10(self):
        props = self.run_test('hkb', 'dict')
        self.assertIsInstance(props['items']['additionalProperties'], dict)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(path, kind):
        app = FastAPI()
        if kind == 'dict':

            class M(BaseModel):
                items: Dict[str, int]
        else:

            class M(BaseModel):
                name: str

        @app.post('/' + path)
        def foo(m: M):
            return m
        schema = TestClient(app).get('/openapi.json').json()
        return schema['components']['schemas']['M']['properties']

    def test_diversity_1(self):
        props = self.run_test('tvds', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_2(self):
        props = self.run_test('npw', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_3(self):
        props = self.run_test('ido', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_4(self):
        props = self.run_test('nitcvg', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_5(self):
        props = self.run_test('tjdrkx', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_6(self):
        props = self.run_test('lwjxvoru', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_7(self):
        props = self.run_test('cdkn', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_8(self):
        props = self.run_test('coziyck', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_9(self):
        props = self.run_test('tyzjy', 'plain')
        self.assertEqual('string', props['name']['type'])

    def test_diversity_10(self):
        props = self.run_test('pbf', 'plain')
        self.assertEqual('string', props['name']['type'])
