import unittest
from pandas.core.dtypes.common import is_string_dtype
from pandas.core.dtypes.common import np
import pandas


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, is_string_dtype(6932))

    def test_diversity_2(self):
        self.assertEqual(False, is_string_dtype(6928))

    def test_diversity_3(self):
        self.assertEqual(False, is_string_dtype(2270))

    def test_diversity_4(self):
        self.assertEqual(False, is_string_dtype(6237))

    def test_diversity_5(self):
        self.assertEqual(False, is_string_dtype(2910))

    def test_diversity_6(self):
        self.assertEqual(False, is_string_dtype(3343))

    def test_diversity_7(self):
        self.assertEqual(False, is_string_dtype(4544))

    def test_diversity_8(self):
        self.assertEqual(False, is_string_dtype(266))

    def test_diversity_9(self):
        self.assertEqual(False, is_string_dtype(5480))

    def test_diversity_10(self):
        self.assertEqual(False, is_string_dtype(8175))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, is_string_dtype('DTevGssbJ'))

    def test_diversity_2(self):
        self.assertEqual(True, is_string_dtype('NSBcjJvANmNtpa'))

    def test_diversity_3(self):
        self.assertEqual(True, is_string_dtype('goOzAOZMv'))

    def test_diversity_4(self):
        self.assertEqual(True, is_string_dtype('rWHzJpqgAATzDAD'))

    def test_diversity_5(self):
        self.assertEqual(True, is_string_dtype('NccBGGkdve'))

    def test_diversity_6(self):
        self.assertEqual(True, is_string_dtype('nHuqe'))

    def test_diversity_7(self):
        self.assertEqual(True, is_string_dtype('gJcfcSqsmMetu'))

    def test_diversity_8(self):
        self.assertEqual(True, is_string_dtype('odtgnRsWj'))

    def test_diversity_9(self):
        self.assertEqual(True, is_string_dtype('RhttwIBZT'))

    def test_diversity_10(self):
        self.assertEqual(True, is_string_dtype('NJmzWR'))
