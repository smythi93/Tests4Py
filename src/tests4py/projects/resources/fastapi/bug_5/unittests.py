import unittest
from fastapi import Depends, FastAPI
from pydantic import BaseModel
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(username, password):
        app = FastAPI()

        class ModelB(BaseModel):
            username: str

        class ModelC(ModelB):
            password: str

        class ModelA(BaseModel):
            name: str
            description: str = None
            model_b: ModelB

        async def get_model_c() -> ModelC:
            return ModelC(username=username, password=password)

        @app.get('/model', response_model=ModelA)
        async def get_model_a(model_c=Depends(get_model_c)):
            return {'name': 'n', 'description': 'd', 'model_b': model_c}
        client = TestClient(app)
        return client.get('/model').json()['model_b']

    def test_diversity_1(self):
        model_b = self.run_test('oooxdknhsrjl', 'ctlxlsljw')
        self.assertNotIn('password', model_b)

    def test_diversity_2(self):
        model_b = self.run_test('hxklzt', 'hhwbgrul')
        self.assertNotIn('password', model_b)

    def test_diversity_3(self):
        model_b = self.run_test('pmwmnsulqa', 'rebwbwcd')
        self.assertNotIn('password', model_b)

    def test_diversity_4(self):
        model_b = self.run_test('wpxcdfhrpvuo', 'bivq')
        self.assertNotIn('password', model_b)

    def test_diversity_5(self):
        model_b = self.run_test('ehfogili', 'xlfhrmc')
        self.assertNotIn('password', model_b)

    def test_diversity_6(self):
        model_b = self.run_test('kzqbuppobo', 'hqfjdp')
        self.assertNotIn('password', model_b)

    def test_diversity_7(self):
        model_b = self.run_test('fyqywezqxex', 'zcyaq')
        self.assertNotIn('password', model_b)

    def test_diversity_8(self):
        model_b = self.run_test('ydomrahqspi', 'mszvfpou')
        self.assertNotIn('password', model_b)

    def test_diversity_9(self):
        model_b = self.run_test('frqboeadigfa', 'vapqomwlxegz')
        self.assertNotIn('password', model_b)

    def test_diversity_10(self):
        model_b = self.run_test('czaq', 'hkdojunjoz')
        self.assertNotIn('password', model_b)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(username, password):
        app = FastAPI()

        class ModelB(BaseModel):
            username: str

        class ModelC(ModelB):
            password: str

        class ModelA(BaseModel):
            name: str
            description: str = None
            model_b: ModelB

        async def get_model_c() -> ModelC:
            return ModelC(username=username, password=password)

        @app.get('/model', response_model=ModelA)
        async def get_model_a(model_c=Depends(get_model_c)):
            return {'name': 'n', 'description': 'd', 'model_b': model_c}
        client = TestClient(app)
        return client.get('/model').json()['model_b']

    def test_diversity_1(self):
        model_b = self.run_test('hslpvzm', 'isotxo')
        self.assertEqual('hslpvzm', model_b['username'])

    def test_diversity_2(self):
        model_b = self.run_test('awhvuoqgok', 'bxccfj')
        self.assertEqual('awhvuoqgok', model_b['username'])

    def test_diversity_3(self):
        model_b = self.run_test('yiporsjwz', 'jbulq')
        self.assertEqual('yiporsjwz', model_b['username'])

    def test_diversity_4(self):
        model_b = self.run_test('krxshbfqdww', 'yljhtafoh')
        self.assertEqual('krxshbfqdww', model_b['username'])

    def test_diversity_5(self):
        model_b = self.run_test('nsxxl', 'gbsrdzt')
        self.assertEqual('nsxxl', model_b['username'])

    def test_diversity_6(self):
        model_b = self.run_test('vsxzru', 'batakf')
        self.assertEqual('vsxzru', model_b['username'])

    def test_diversity_7(self):
        model_b = self.run_test('lugemumj', 'vuvgxsoj')
        self.assertEqual('lugemumj', model_b['username'])

    def test_diversity_8(self):
        model_b = self.run_test('earvsuipiei', 'tjnka')
        self.assertEqual('earvsuipiei', model_b['username'])

    def test_diversity_9(self):
        model_b = self.run_test('llfoihmbz', 'iiimtiihdcc')
        self.assertEqual('llfoihmbz', model_b['username'])

    def test_diversity_10(self):
        model_b = self.run_test('rfeuhnsusryp', 'oyutpbyqtbg')
        self.assertEqual('rfeuhnsusryp', model_b['username'])