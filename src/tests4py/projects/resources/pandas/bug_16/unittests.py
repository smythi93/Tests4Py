import unittest
import pandas
from pandas._testing import assert_index_equal
from pandas import PeriodIndex


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        idx = PeriodIndex(['2292-09', '2292-10', '2292-11', '2292-12'], freq='M', name='idx')
        result = idx - pandas.Period('2293-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_2(self):
        idx = PeriodIndex(['1070-09', '1070-10', '1070-11', '1070-12'], freq='M', name='idx')
        result = idx - pandas.Period('1071-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_3(self):
        idx = PeriodIndex(['7991-09', '7991-10', '7991-11', '7991-12'], freq='M', name='idx')
        result = idx - pandas.Period('7992-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_4(self):
        idx = PeriodIndex(['5617-09', '5617-10', '5617-11', '5617-12'], freq='M', name='idx')
        result = idx - pandas.Period('5618-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_5(self):
        idx = PeriodIndex(['8683-09', '8683-10', '8683-11', '8683-12'], freq='M', name='idx')
        result = idx - pandas.Period('8684-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_6(self):
        idx = PeriodIndex(['3755-09', '3755-10', '3755-11', '3755-12'], freq='M', name='idx')
        result = idx - pandas.Period('3756-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_7(self):
        idx = PeriodIndex(['9739-09', '9739-10', '9739-11', '9739-12'], freq='M', name='idx')
        result = idx - pandas.Period('9740-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_8(self):
        idx = PeriodIndex(['1749-09', '1749-10', '1749-11', '1749-12'], freq='M', name='idx')
        result = idx - pandas.Period('1750-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_9(self):
        idx = PeriodIndex(['4396-09', '4396-10', '4396-11', '4396-12'], freq='M', name='idx')
        result = idx - pandas.Period('4397-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_10(self):
        idx = PeriodIndex(['9862-09', '9862-10', '9862-11', '9862-12'], freq='M', name='idx')
        result = idx - pandas.Period('9863-12', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        idx = PeriodIndex(['3604-01', '3604-02', '3604-03', '3604-04'], freq='M', name='idx')
        result = idx - pandas.Period('3605-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_2(self):
        idx = PeriodIndex(['7552-01', '7552-02', '7552-03', '7552-04'], freq='M', name='idx')
        result = idx - pandas.Period('7553-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_3(self):
        idx = PeriodIndex(['4178-01', '4178-02', '4178-03', '4178-04'], freq='M', name='idx')
        result = idx - pandas.Period('4179-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_4(self):
        idx = PeriodIndex(['2428-01', '2428-02', '2428-03', '2428-04'], freq='M', name='idx')
        result = idx - pandas.Period('2429-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_5(self):
        idx = PeriodIndex(['9640-01', '9640-02', '9640-03', '9640-04'], freq='M', name='idx')
        result = idx - pandas.Period('9641-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_6(self):
        idx = PeriodIndex(['4634-01', '4634-02', '4634-03', '4634-04'], freq='M', name='idx')
        result = idx - pandas.Period('4635-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_7(self):
        idx = PeriodIndex(['2247-01', '2247-02', '2247-03', '2247-04'], freq='M', name='idx')
        result = idx - pandas.Period('2248-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_8(self):
        idx = PeriodIndex(['1559-01', '1559-02', '1559-03', '1559-04'], freq='M', name='idx')
        result = idx - pandas.Period('1560-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_9(self):
        idx = PeriodIndex(['1815-01', '1815-02', '1815-03', '1815-04'], freq='M', name='idx')
        result = idx - pandas.Period('1816-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))

    def test_diversity_10(self):
        idx = PeriodIndex(['1677-01', '1677-02', '1677-03', '1677-04'], freq='M', name='idx')
        result = idx - pandas.Period('1678-01', freq='M')
        off = idx.freq
        exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
        self.assertEqual(None, assert_index_equal(result, exp))
