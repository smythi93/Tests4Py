import unittest
import pandas
from pandas.tseries.offsets import BMonthBegin, BMonthEnd, BQuarterBegin, BQuarterEnd, BYearBegin, BYearEnd, MonthBegin, \
    MonthEnd, QuarterBegin, QuarterEnd, YearBegin, YearEnd


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        n = 1
        offset = BMonthEnd(n=n)
        rng = pandas.date_range(start='8/1/1538', periods=454, freq='T')
        ser = pandas.Series(rng)
        res2 = ser + offset
        self.assertEqual(res2.iloc[0], ser.iloc[0] + offset)

    def test_diversity_2(self):
        n = -2
        offset = YearEnd(n=n)
        rng = pandas.date_range(start='7/16/1415', periods=8946, freq='T')
        ser = pandas.Series(rng)
        res2 = ser + offset
        self.assertEqual(res2.iloc[0], ser.iloc[0] + offset)

    def test_diversity_3(self):
        n = -2
        offset = MonthEnd(n=n)
        rng = pandas.date_range(start='3/12/1019', periods=7584, freq='T')
        ser = pandas.Series(rng)
        res2 = ser + offset
        self.assertEqual(res2.iloc[0], ser.iloc[0] + offset)

    def test_diversity_4(self):
        n = -2
        offset = BYearEnd(n=n)
        rng = pandas.date_range(start='2/2/1412', periods=4136, freq='T')
        res = rng + offset
        self.assertEqual(res[-1], rng[-1] + offset)

    def test_diversity_5(self):
        n = 1
        offset = QuarterBegin(n=n)
        rng = pandas.date_range(start='1/15/1115', periods=4816, freq='T')
        res = rng + offset
        self.assertEqual(res[-1], rng[-1] + offset)

    def test_diversity_6(self):
        n = 1
        offset = BYearBegin(n=n)
        rng = pandas.date_range(start='10/23/1599', periods=5285, freq='T')
        res = rng + offset
        self.assertEqual(res[-1], rng[-1] + offset)

    def test_diversity_7(self):
        n = 1
        offset = YearBegin(n=n)
        rng = pandas.date_range(start='4/15/1203', periods=9406, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)

    def test_diversity_8(self):
        n = 1
        offset = QuarterBegin(n=n)
        rng = pandas.date_range(start='1/23/1385', periods=7401, freq='T')
        ser = pandas.Series(rng)
        res2 = ser + offset
        self.assertEqual(res2.iloc[0], ser.iloc[0] + offset)

    def test_diversity_9(self):
        n = 1
        offset = BYearEnd(n=n)
        rng = pandas.date_range(start='4/24/1190', periods=6858, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)

    def test_diversity_10(self):
        n = 1
        offset = BQuarterEnd(n=n)
        rng = pandas.date_range(start='7/23/1414', periods=4385, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        n = 1
        offset = YearEnd(n=n)
        rng = pandas.date_range(start='9/3/2085', periods=1780, freq='T')
        ser = pandas.Series(rng)
        res2 = ser + offset
        self.assertEqual(res2.iloc[0], ser.iloc[0] + offset)

    def test_diversity_2(self):
        n = 1
        offset = MonthBegin(n=n)
        rng = pandas.date_range(start='9/9/1806', periods=3086, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)

    def test_diversity_3(self):
        n = -2
        offset = BMonthBegin(n=n)
        rng = pandas.date_range(start='2/26/2165', periods=6579, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)

    def test_diversity_4(self):
        n = -2
        offset = BYearEnd(n=n)
        rng = pandas.date_range(start='7/6/1738', periods=4810, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)

    def test_diversity_5(self):
        n = 1
        offset = BYearBegin(n=n)
        rng = pandas.date_range(start='12/9/1749', periods=334, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)

    def test_diversity_6(self):
        n = -2
        offset = BYearBegin(n=n)
        rng = pandas.date_range(start='2/4/1906', periods=7842, freq='T')
        res = rng + offset
        self.assertEqual(res[-1], rng[-1] + offset)

    def test_diversity_7(self):
        n = 1
        offset = BQuarterBegin(n=n)
        rng = pandas.date_range(start='1/16/1972', periods=1410, freq='T')
        ser = pandas.Series(rng)
        res2 = ser + offset
        self.assertEqual(res2.iloc[0], ser.iloc[0] + offset)

    def test_diversity_8(self):
        n = -2
        offset = BYearBegin(n=n)
        rng = pandas.date_range(start='12/4/2189', periods=447, freq='T')
        res = rng + offset
        self.assertEqual(res[-1], rng[-1] + offset)

    def test_diversity_9(self):
        n = 1
        offset = BQuarterBegin(n=n)
        rng = pandas.date_range(start='1/5/1816', periods=529, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)

    def test_diversity_10(self):
        n = 1
        offset = BYearEnd(n=n)
        rng = pandas.date_range(start='9/25/2076', periods=503, freq='T')
        res = rng + offset
        self.assertEqual(res[0], rng[0] + offset)
