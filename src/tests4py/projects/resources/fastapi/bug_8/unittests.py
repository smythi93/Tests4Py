import unittest
from fastapi import APIRouter, FastAPI
from fastapi.routing import APIRoute
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(prefix, msg, check_x_type):
        app = FastAPI()

        class RouteA(APIRoute):
            x_type = 'A'

        class RouteB(APIRoute):
            x_type = 'B'
        router_a = APIRouter(route_class=RouteA)
        router_b = APIRouter(route_class=RouteB)

        @router_b.get('/item')
        def get_b():
            return {'msg': msg}
        router_a.include_router(router=router_b, prefix='/' + prefix)
        app.include_router(router=router_a, prefix='/root')

        @app.get('/routes/')
        def routes():
            return [r.x_type for r in app.routes if isinstance(r, APIRoute) and r.path.startswith('/root')]
        client = TestClient(app)
        return client.get('/routes/' if check_x_type else '/root/' + prefix + '/item')

    def test_diversity_1(self):
        response = self.run_test('fgybp', 'enitzji', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_2(self):
        response = self.run_test('rgezsi', 'xxip', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_3(self):
        response = self.run_test('pcrec', 'uot', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_4(self):
        response = self.run_test('odafoh', 'uhf', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_5(self):
        response = self.run_test('kab', 'arfeesew', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_6(self):
        response = self.run_test('erdb', 'rpoh', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_7(self):
        response = self.run_test('quhba', 'dnqbmrk', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_8(self):
        response = self.run_test('mgksqi', 'xdhjo', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_9(self):
        response = self.run_test('uch', 'wszuaxsc', True)
        self.assertEqual(200, response.status_code)

    def test_diversity_10(self):
        response = self.run_test('nhxfetpo', 'gzzs', True)
        self.assertEqual(200, response.status_code)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(prefix, msg, check_x_type):
        app = FastAPI()

        class RouteA(APIRoute):
            x_type = 'A'

        class RouteB(APIRoute):
            x_type = 'B'
        router_a = APIRouter(route_class=RouteA)
        router_b = APIRouter(route_class=RouteB)

        @router_b.get('/item')
        def get_b():
            return {'msg': msg}
        router_a.include_router(router=router_b, prefix='/' + prefix)
        app.include_router(router=router_a, prefix='/root')

        @app.get('/routes/')
        def routes():
            return [r.x_type for r in app.routes if isinstance(r, APIRoute) and r.path.startswith('/root')]
        client = TestClient(app)
        return client.get('/routes/' if check_x_type else '/root/' + prefix + '/item')

    def test_diversity_1(self):
        response = self.run_test('fks', 'sgikovlo', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_2(self):
        response = self.run_test('mmtxknsn', 'xsfmch', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_3(self):
        response = self.run_test('iips', 'ymk', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_4(self):
        response = self.run_test('bxjlgryb', 'dktj', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_5(self):
        response = self.run_test('bdv', 'ddrmqir', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_6(self):
        response = self.run_test('eun', 'mpp', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_7(self):
        response = self.run_test('marote', 'kvci', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_8(self):
        response = self.run_test('lkjc', 'hyywvfzm', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_9(self):
        response = self.run_test('qtrl', 'byq', False)
        self.assertEqual(200, response.status_code)

    def test_diversity_10(self):
        response = self.run_test('tjzkiwp', 'zedxuo', False)
        self.assertEqual(200, response.status_code)