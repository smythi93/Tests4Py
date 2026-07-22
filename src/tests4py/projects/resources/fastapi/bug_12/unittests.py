import unittest
from typing import Optional
from fastapi import FastAPI, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_test(path, scheme, cred):
        app = FastAPI()
        security = HTTPBearer(auto_error=False)

        @app.get('/' + path)
        def read_current_user(credentials: Optional[HTTPAuthorizationCredentials]=Security(security)):
            if credentials is None:
                return {'msg': 'Create an account first'}
            return {'scheme': credentials.scheme, 'credentials': credentials.credentials}
        headers = {}
        if scheme is not None:
            headers['Authorization'] = scheme + ' ' + cred
        resp = TestClient(app).get('/' + path, headers=headers)
        return (resp.status_code, resp.json())

    def test_diversity_1(self):
        status, body = self.run_test('cmstxux', 'Bear', 'ctmbx')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_2(self):
        status, body = self.run_test('isdarud', 'Bear', 'rtzi')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_3(self):
        status, body = self.run_test('utnatvy', 'Bear', 'muiwimmn')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_4(self):
        status, body = self.run_test('mbso', 'Basic', 'gfetvj')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_5(self):
        status, body = self.run_test('unwr', 'OAuth', 'leyd')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_6(self):
        status, body = self.run_test('rxo', 'Negotiate', 'gqlbdyq')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_7(self):
        status, body = self.run_test('nfhm', 'Basic', 'umvy')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_8(self):
        status, body = self.run_test('nuhkv', 'OAuth', 'ntv')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_9(self):
        status, body = self.run_test('cooguie', 'OAuth', 'wdtw')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

    def test_diversity_10(self):
        status, body = self.run_test('whidl', 'Bear', 'oqvhsc')
        self.assertEqual(200, status)
        self.assertEqual({'msg': 'Create an account first'}, body)

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_test(path, scheme, cred):
        app = FastAPI()
        security = HTTPBearer(auto_error=False)

        @app.get('/' + path)
        def read_current_user(credentials: Optional[HTTPAuthorizationCredentials]=Security(security)):
            if credentials is None:
                return {'msg': 'Create an account first'}
            return {'scheme': credentials.scheme, 'credentials': credentials.credentials}
        headers = {}
        if scheme is not None:
            headers['Authorization'] = scheme + ' ' + cred
        resp = TestClient(app).get('/' + path, headers=headers)
        return (resp.status_code, resp.json())

    def test_diversity_1(self):
        status, body = self.run_test('rvzx', 'Bearer', 'gpsd')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'gpsd'}, body)

    def test_diversity_2(self):
        status, body = self.run_test('flg', 'Bearer', 'vyoupmmg')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'vyoupmmg'}, body)

    def test_diversity_3(self):
        status, body = self.run_test('lyla', 'Bearer', 'dftwdpe')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'dftwdpe'}, body)

    def test_diversity_4(self):
        status, body = self.run_test('xhgqf', 'Bearer', 'ksqxbogj')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'ksqxbogj'}, body)

    def test_diversity_5(self):
        status, body = self.run_test('ydvgtboe', 'Bearer', 'ehhxxq')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'ehhxxq'}, body)

    def test_diversity_6(self):
        status, body = self.run_test('acoayzr', 'Bearer', 'glicqsro')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'glicqsro'}, body)

    def test_diversity_7(self):
        status, body = self.run_test('tbdvzho', 'Bearer', 'dmnxl')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'dmnxl'}, body)

    def test_diversity_8(self):
        status, body = self.run_test('gsd', 'Bearer', 'kitypbxx')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'kitypbxx'}, body)

    def test_diversity_9(self):
        status, body = self.run_test('tapemrrr', 'Bearer', 'lbk')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'lbk'}, body)

    def test_diversity_10(self):
        status, body = self.run_test('kjhi', 'Bearer', 'uxigrm')
        self.assertEqual(200, status)
        self.assertEqual({'scheme': 'Bearer', 'credentials': 'uxigrm'}, body)
