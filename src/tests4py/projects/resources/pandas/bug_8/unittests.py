import unittest
import pandas
import numpy
from pandas._testing import assert_frame_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        df = pandas.DataFrame(numpy.eye(196), dtype='float64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_2(self):
        df = pandas.DataFrame(numpy.eye(188), dtype='float')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_3(self):
        df = pandas.DataFrame(numpy.eye(265), dtype='float')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_4(self):
        df = pandas.DataFrame(numpy.eye(213), dtype='float64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_5(self):
        df = pandas.DataFrame(numpy.eye(342), dtype='float')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_6(self):
        df = pandas.DataFrame(numpy.eye(111), dtype='float64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_7(self):
        df = pandas.DataFrame(numpy.eye(85), dtype='float64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_8(self):
        df = pandas.DataFrame(numpy.eye(86), dtype='float64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_9(self):
        df = pandas.DataFrame(numpy.eye(13), dtype='float')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_10(self):
        df = pandas.DataFrame(numpy.eye(172), dtype='float')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        df = pandas.DataFrame(numpy.eye(11), dtype='boolean')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_2(self):
        df = pandas.DataFrame(numpy.eye(331), dtype='int64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_3(self):
        df = pandas.DataFrame(numpy.eye(371), dtype='Int64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_4(self):
        df = pandas.DataFrame(numpy.eye(323), dtype='boolean')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_5(self):
        df = pandas.DataFrame(numpy.eye(76), dtype='Int64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_6(self):
        df = pandas.DataFrame(numpy.eye(49), dtype='int64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_7(self):
        df = pandas.DataFrame(numpy.eye(51), dtype='boolean')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_8(self):
        df = pandas.DataFrame(numpy.eye(88), dtype='int64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_9(self):
        df = pandas.DataFrame(numpy.eye(101), dtype='boolean')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))

    def test_diversity_10(self):
        df = pandas.DataFrame(numpy.eye(72), dtype='Int64')
        result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
        self.assertEqual(None, assert_frame_equal(result, df))
