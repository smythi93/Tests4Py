import unittest
from spacy.errors import Errors



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'xgxv'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_2(self):
        tag = 'cqgqainnb'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_3(self):
        tag = 'dfnfle'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_4(self):
        tag = 'ztqtuv'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_5(self):
        tag = 'qurrqth'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_6(self):
        tag = 'pdtbnqt'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_7(self):
        tag = 'dnzu'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_8(self):
        tag = 'fvwbqkfi'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_9(self):
        tag = 'eidyjx'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)

    def test_diversity_10(self):
        tag = 'ylwjhcisg'
        value = getattr(Errors, 'E175')
        self.assertTrue(value.startswith('[' + 'E175' + '] '))
        self.assertGreater(len(value), len('E175') + 3)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'qsgfaathtp'
        value = getattr(Errors, 'E009')
        self.assertTrue(value.startswith('[' + 'E009' + '] '))
        self.assertGreater(len(value), len('E009') + 3)

    def test_diversity_2(self):
        tag = 'agiyyjgyc'
        value = getattr(Errors, 'E039')
        self.assertTrue(value.startswith('[' + 'E039' + '] '))
        self.assertGreater(len(value), len('E039') + 3)

    def test_diversity_3(self):
        tag = 'fjyabh'
        value = getattr(Errors, 'E033')
        self.assertTrue(value.startswith('[' + 'E033' + '] '))
        self.assertGreater(len(value), len('E033') + 3)

    def test_diversity_4(self):
        tag = 'nteaqzw'
        value = getattr(Errors, 'E012')
        self.assertTrue(value.startswith('[' + 'E012' + '] '))
        self.assertGreater(len(value), len('E012') + 3)

    def test_diversity_5(self):
        tag = 'okebotj'
        value = getattr(Errors, 'E011')
        self.assertTrue(value.startswith('[' + 'E011' + '] '))
        self.assertGreater(len(value), len('E011') + 3)

    def test_diversity_6(self):
        tag = 'ntswwturoq'
        value = getattr(Errors, 'E017')
        self.assertTrue(value.startswith('[' + 'E017' + '] '))
        self.assertGreater(len(value), len('E017') + 3)

    def test_diversity_7(self):
        tag = 'bgbz'
        value = getattr(Errors, 'E032')
        self.assertTrue(value.startswith('[' + 'E032' + '] '))
        self.assertGreater(len(value), len('E032') + 3)

    def test_diversity_8(self):
        tag = 'qzzgyr'
        value = getattr(Errors, 'E036')
        self.assertTrue(value.startswith('[' + 'E036' + '] '))
        self.assertGreater(len(value), len('E036') + 3)

    def test_diversity_9(self):
        tag = 'hszhjl'
        value = getattr(Errors, 'E031')
        self.assertTrue(value.startswith('[' + 'E031' + '] '))
        self.assertGreater(len(value), len('E031') + 3)

    def test_diversity_10(self):
        tag = 'nhamqt'
        value = getattr(Errors, 'E011')
        self.assertTrue(value.startswith('[' + 'E011' + '] '))
        self.assertGreater(len(value), len('E011') + 3)
