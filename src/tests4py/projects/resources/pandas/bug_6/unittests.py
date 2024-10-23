import unittest
from pandas import PeriodIndex, Series
from pandas._testing import assert_series_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        ser = Series([1], index=PeriodIndex(['2830'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_2(self):
        ser = Series([1], index=PeriodIndex(['698'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_3(self):
        ser = Series([1], index=PeriodIndex(['8468'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_4(self):
        ser = Series([1], index=PeriodIndex(['2992'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_5(self):
        ser = Series([1], index=PeriodIndex(['3412'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_6(self):
        ser = Series([1], index=PeriodIndex(['6406'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_7(self):
        ser = Series([1], index=PeriodIndex(['3510'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_8(self):
        ser = Series([1], index=PeriodIndex(['2965'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_9(self):
        ser = Series([1], index=PeriodIndex(['7980'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))

    def test_diversity_10(self):
        ser = Series([1], index=PeriodIndex(['5221'], name='A', freq='D'))
        grp = ser.groupby(level='A')
        result = grp.size()
        self.assertEqual(None, assert_series_equal(result, ser))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual("", "")

    def test_diversity_2(self):
        self.assertEqual("", "")

    def test_diversity_3(self):
        self.assertEqual("", "")

    def test_diversity_4(self):
        self.assertEqual("", "")

    def test_diversity_5(self):
        self.assertEqual("", "")

    def test_diversity_6(self):
        self.assertEqual("", "")

    def test_diversity_7(self):
        self.assertEqual("", "")

    def test_diversity_8(self):
        self.assertEqual("", "")

    def test_diversity_9(self):
        self.assertEqual("", "")

    def test_diversity_10(self):
        self.assertEqual("", "")
