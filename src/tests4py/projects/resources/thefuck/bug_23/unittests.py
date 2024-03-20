import unittest
from thefuck.utils import cache


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIsNone(cache({}, 'kxnpfKjUrswooG', {}))

    def test_diversity_2(self):
        self.assertIsNone(cache({}, 'XbQwSHfjMIbLftg', {}))

    def test_diversity_3(self):
        self.assertIsNone(cache({}, 'JUdRrwOUr', {}))

    def test_diversity_4(self):
        self.assertIsNone(cache({}, 'LkYIpSoPtrvgjmw', {}))

    def test_diversity_5(self):
        self.assertIsNone(cache({}, 'ftiCDwBot', {}))

    def test_diversity_6(self):
        self.assertIsNone(cache({}, 'gUzdtKnY', {}))

    def test_diversity_7(self):
        self.assertIsNone(cache({}, 'rSLEsodtept', {}))

    def test_diversity_8(self):
        self.assertIsNone(cache({}, 'mKTgcPrGWcILzz', {}))

    def test_diversity_9(self):
        self.assertIsNone(cache({}, 'OYBEgGNLdMEMNZ', {}))

    def test_diversity_10(self):
        self.assertIsNone(cache({}, 'LtUWgOOI', {}))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertIsNotNone(cache({}, 'MzYpPETZajJFIYJ', {'key': {'etag': '0', 'value': 'MzYpPETZajJFIYJ'}}))

    def test_diversity_2(self):
        self.assertIsNotNone(cache({'key': {'etag': '0', 'value': 'gupMNKqEJyHSZVl'}}, 'gupMNKqEJyHSZVl', {}))

    def test_diversity_3(self):
        self.assertIsNotNone(cache({}, 'VvHuyEjzurAADM', {'key': {'etag': '0', 'value': 'VvHuyEjzurAADM'}}))

    def test_diversity_4(self):
        self.assertIsNotNone(cache({}, 'VnwdypzRdnwkb', {'key': {'etag': '0', 'value': 'VnwdypzRdnwkb'}}))

    def test_diversity_5(self):
        self.assertIsNotNone(cache({'key': {'etag': '0', 'value': 'YopvFiCuuaXg'}}, 'YopvFiCuuaXg', {}))

    def test_diversity_6(self):
        self.assertIsNotNone(cache({}, 'FLabwklSeb', {'key': {'etag': '0', 'value': 'FLabwklSeb'}}))

    def test_diversity_7(self):
        self.assertIsNotNone(cache({'key': {'etag': '0', 'value': 'gzUjvr'}}, 'gzUjvr', {}))

    def test_diversity_8(self):
        self.assertIsNotNone(cache({}, 'mIlByVG', {'key': {'etag': '0', 'value': 'mIlByVG'}}))

    def test_diversity_9(self):
        self.assertIsNotNone(cache({'key': {'etag': '0', 'value': 'DGWREkiFdO'}}, 'DGWREkiFdO', {}))

    def test_diversity_10(self):
        self.assertIsNotNone(cache({'key': {'etag': '0', 'value': 'CSkbVE'}}, 'CSkbVE', {}))


