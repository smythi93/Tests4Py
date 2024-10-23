import unittest
import pandas
import numpy
from pandas import Categorical, Series
from pandas._testing import assert_numpy_array_equal, assert_series_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        cat = Categorical([1704, 1705, numpy.inf])
        result = cat.isna()
        expected = numpy.array([True, True, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_2(self):
        cat = Categorical([1573, 1574, numpy.inf])
        result = cat.isna()
        expected = numpy.array([True, True, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_3(self):
        cat = Categorical([46, 47, numpy.inf])
        result = cat.isna()
        expected = numpy.array([True, True, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_4(self):
        cat = Categorical([411, 412, numpy.inf])
        result = cat.isna()
        expected = numpy.array([True, True, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_5(self):
        cat = Categorical([4385, 4386, pandas.NA])
        result = cat.isna()
        expected = numpy.array([True, True, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_6(self):
        cat = Categorical([6780, 6781, numpy.inf])
        result = cat.isna()
        expected = numpy.array([True, True, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_7(self):
        cat = Categorical([7088, 7089, numpy.nan])
        result = cat.isna()
        expected = numpy.array([True, True, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_8(self):
        cat = Categorical([2069, 2070, pandas.NA])
        result = cat.isna()
        expected = numpy.array([True, True, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_9(self):
        cat = Categorical([4817, 4818, pandas.NA])
        result = cat.isna()
        expected = numpy.array([True, True, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_10(self):
        cat = Categorical([7489, 7490, numpy.inf])
        result = cat.isna()
        expected = numpy.array([True, True, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        cat = Categorical([4633, 4634, numpy.nan])
        result = Series(cat).isna()
        expected = Series(numpy.array([False, False, True]))
        self.assertEqual(None, assert_series_equal(result, expected))

    def test_diversity_2(self):
        cat = Categorical([7508, 7509, pandas.NA])
        result = Series(cat).isna()
        expected = Series(numpy.array([False, False, True]))
        self.assertEqual(None, assert_series_equal(result, expected))

    def test_diversity_3(self):
        cat = Categorical([5896, 5897, numpy.nan])
        result = cat.isna()
        expected = numpy.array([False, False, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_4(self):
        cat = Categorical([9988, 9989, numpy.nan])
        result = Series(cat).isna()
        expected = Series(numpy.array([False, False, True]))
        self.assertEqual(None, assert_series_equal(result, expected))

    def test_diversity_5(self):
        cat = Categorical([9146, 9147, numpy.inf])
        result = cat.isna()
        expected = numpy.array([False, False, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_6(self):
        cat = Categorical([9602, 9603, numpy.nan])
        result = cat.isna()
        expected = numpy.array([False, False, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_7(self):
        cat = Categorical([8039, 8040, numpy.inf])
        result = cat.isna()
        expected = numpy.array([False, False, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_8(self):
        cat = Categorical([1084, 1085, pandas.NA])
        result = cat.isna()
        expected = numpy.array([False, False, True])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_9(self):
        cat = Categorical([9848, 9849, numpy.inf])
        result = cat.isna()
        expected = numpy.array([False, False, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))

    def test_diversity_10(self):
        cat = Categorical([8415, 8416, numpy.inf])
        result = cat.isna()
        expected = numpy.array([False, False, False])
        self.assertEqual(None, assert_numpy_array_equal(result, expected))
