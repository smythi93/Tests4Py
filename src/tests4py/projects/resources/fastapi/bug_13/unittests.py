import unittest
from fastapi import APIRouter, FastAPI
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(routes):
        app = FastAPI()
        router = APIRouter()
        for name, code in routes:

            @router.get('/' + name, responses={code: {'description': 'd_' + name}})
            async def handler():
                return 'ok'
        app.include_router(router)
        schema = TestClient(app).get('/openapi.json').json()
        return {p: sorted(m['get']['responses'].keys()) for p, m in schema['paths'].items()}

    def test_diversity_1(self):
        result = self.run_test([('lgy', 501), ('ooaf', 502), ('zlkmztco', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_2(self):
        result = self.run_test([('eyhspzr', 501), ('qjxyw', 502), ('xowzsyfw', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_3(self):
        result = self.run_test([('hkkehq', 501), ('ueuj', 502), ('zon', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_4(self):
        result = self.run_test([('cplew', 501), ('trozn', 502), ('wbad', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_5(self):
        result = self.run_test([('amkmjje', 501), ('fyyywlh', 502), ('ysc', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_6(self):
        result = self.run_test([('aqjb', 501), ('eqer', 502), ('vxx', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_7(self):
        result = self.run_test([('ggpgvw', 501), ('uzn', 502), ('vzzbnxs', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_8(self):
        result = self.run_test([('jocguoo', 501), ('kzjjkme', 502), ('lftqqw', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_9(self):
        result = self.run_test([('dyk', 501), ('mvstzsdd', 502), ('wmuztwt', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_10(self):
        result = self.run_test([('ksqrkyub', 501), ('sikgmeez', 502), ('yub', 503)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(routes):
        app = FastAPI()
        router = APIRouter()
        for name, code in routes:

            @router.get('/' + name, responses={code: {'description': 'd_' + name}})
            async def handler():
                return 'ok'
        app.include_router(router)
        schema = TestClient(app).get('/openapi.json').json()
        return {p: sorted(m['get']['responses'].keys()) for p, m in schema['paths'].items()}

    def test_diversity_1(self):
        result = self.run_test([('axp', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_2(self):
        result = self.run_test([('kdnawht', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_3(self):
        result = self.run_test([('ahkuf', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_4(self):
        result = self.run_test([('tmyczb', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_5(self):
        result = self.run_test([('vozhmxcx', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_6(self):
        result = self.run_test([('uiqc', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_7(self):
        result = self.run_test([('fotvt', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_8(self):
        result = self.run_test([('gpe', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_9(self):
        result = self.run_test([('sngm', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))

    def test_diversity_10(self):
        result = self.run_test([('jkm', 501)])
        for codes in result.values():
            self.assertEqual(2, len(codes))
