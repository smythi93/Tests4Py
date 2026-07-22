import unittest
from fastapi import FastAPI, Form
try:
    from fastapi.testclient import TestClient
except ImportError:
    from starlette.testclient import TestClient

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_list_form(items):
        app = FastAPI()

        @app.post('/form')
        def post_form(items: list=Form(...)):
            return items
        return TestClient(app).post('/form', data={'items': items})

    @staticmethod
    def run_str_form(value):
        app = FastAPI()

        @app.post('/form')
        def post_form(value: str=Form(...)):
            return value
        return TestClient(app).post('/form', data={'value': value})

    def test_diversity_1(self):
        response = self.run_list_form(['fduwaty', 'kcb'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['fduwaty', 'kcb'], response.json())

    def test_diversity_2(self):
        response = self.run_list_form(['bpfxwcgo', 'fmzflsz', 'jzjcyx'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['bpfxwcgo', 'fmzflsz', 'jzjcyx'], response.json())

    def test_diversity_3(self):
        response = self.run_list_form(['vmlgm', 'ytnzr', 'xrynyaghp', 'iuvik'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['vmlgm', 'ytnzr', 'xrynyaghp', 'iuvik'], response.json())

    def test_diversity_4(self):
        response = self.run_list_form(['cqqkla', 'ojila', 'azagaev', 'lzzggcqt'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['cqqkla', 'ojila', 'azagaev', 'lzzggcqt'], response.json())

    def test_diversity_5(self):
        response = self.run_list_form(['prga', 'nfov'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['prga', 'nfov'], response.json())

    def test_diversity_6(self):
        response = self.run_list_form(['fgtwrr', 'gsymf', 'zrz', 'baowjq'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['fgtwrr', 'gsymf', 'zrz', 'baowjq'], response.json())

    def test_diversity_7(self):
        response = self.run_list_form(['tfdynnqk', 'ajm', 'oxzygnnk', 'oxcmzndxh'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['tfdynnqk', 'ajm', 'oxzygnnk', 'oxcmzndxh'], response.json())

    def test_diversity_8(self):
        response = self.run_list_form(['hujhyej', 'ucnskbsrq', 'zkftt', 'wuj'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['hujhyej', 'ucnskbsrq', 'zkftt', 'wuj'], response.json())

    def test_diversity_9(self):
        response = self.run_list_form(['pmlny', 'qhiehzgst', 'fira'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['pmlny', 'qhiehzgst', 'fira'], response.json())

    def test_diversity_10(self):
        response = self.run_list_form(['qzfrfdt', 'vssmj', 'nwa'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(['qzfrfdt', 'vssmj', 'nwa'], response.json())

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_list_form(items):
        app = FastAPI()

        @app.post('/form')
        def post_form(items: list=Form(...)):
            return items
        return TestClient(app).post('/form', data={'items': items})

    @staticmethod
    def run_str_form(value):
        app = FastAPI()

        @app.post('/form')
        def post_form(value: str=Form(...)):
            return value
        return TestClient(app).post('/form', data={'value': value})

    def test_diversity_1(self):
        response = self.run_str_form('ozpy')
        self.assertEqual(200, response.status_code)
        self.assertEqual('ozpy', response.json())

    def test_diversity_2(self):
        response = self.run_str_form('btlvy')
        self.assertEqual(200, response.status_code)
        self.assertEqual('btlvy', response.json())

    def test_diversity_3(self):
        response = self.run_str_form('rlxz')
        self.assertEqual(200, response.status_code)
        self.assertEqual('rlxz', response.json())

    def test_diversity_4(self):
        response = self.run_str_form('pemqfk')
        self.assertEqual(200, response.status_code)
        self.assertEqual('pemqfk', response.json())

    def test_diversity_5(self):
        response = self.run_str_form('uood')
        self.assertEqual(200, response.status_code)
        self.assertEqual('uood', response.json())

    def test_diversity_6(self):
        response = self.run_str_form('lkg')
        self.assertEqual(200, response.status_code)
        self.assertEqual('lkg', response.json())

    def test_diversity_7(self):
        response = self.run_str_form('kcn')
        self.assertEqual(200, response.status_code)
        self.assertEqual('kcn', response.json())

    def test_diversity_8(self):
        response = self.run_str_form('xptwcnl')
        self.assertEqual(200, response.status_code)
        self.assertEqual('xptwcnl', response.json())

    def test_diversity_9(self):
        response = self.run_str_form('bvejuqsvi')
        self.assertEqual(200, response.status_code)
        self.assertEqual('bvejuqsvi', response.json())

    def test_diversity_10(self):
        response = self.run_str_form('vfowsecz')
        self.assertEqual(200, response.status_code)
        self.assertEqual('vfowsecz', response.json())