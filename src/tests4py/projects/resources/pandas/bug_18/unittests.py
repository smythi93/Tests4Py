import unittest
import numpy
from pandas.api.indexers import FixedForwardWindowIndexer
from pandas import DataFrame, Series
from pandas._testing import assert_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.234896, 2.224896, 2.224896, 2.224896, 2.234896, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_2(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.237092, 2.227092, 2.227092, 2.227092, 2.237092, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_3(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.233238, 2.223238, 2.223238, 2.223238, 2.233238, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_4(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.237534, 2.227534, 2.227534, 2.227534, 2.237534, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_5(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.23709, 2.22709, 2.22709, 2.22709, 2.23709, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_6(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.23561, 2.22561, 2.22561, 2.22561, 2.23561, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_7(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.235186, 2.225186, 2.225186, 2.225186, 2.235186, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_8(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.235025, 2.225025, 2.225025, 2.225025, 2.235025, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_9(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.233626, 2.223626, 2.223626, 2.223626, 2.233626, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_10(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor([0.0, 2.23733, 2.22733, 2.22733, 2.22733, 2.23733, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.2323963332, 2.2295083332, 2.2283403332, 2.2290913332, 2.2319893332, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_2(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.232396822, 2.229508822, 2.228340822, 2.229091822, 2.231989822, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_3(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.232396807, 2.229508807, 2.228340807, 2.229091807, 2.231989807, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_4(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.2323967504, 2.2295087504, 2.2283407504, 2.2290917504, 2.2319897504, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_5(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.2323966699, 2.2295086699, 2.2283406699, 2.2290916699, 2.2319896699, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_6(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.232396922, 2.229508922, 2.228340922, 2.229091922, 2.231989922, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_7(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.2323963611, 2.2295083611, 2.2283403611, 2.2290913611, 2.2319893611, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_8(self):
        constructor = DataFrame
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.2323969979, 2.2295089979, 2.2283409979, 2.2290919979, 2.2319899979, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_9(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.2323961942, 2.2295081942, 2.2283401942, 2.2290911942, 2.2319891942, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))

    def test_diversity_10(self):
        constructor = Series
        values = numpy.arange(10)
        values[5] = 100.0
        indexer = FixedForwardWindowIndexer(window_size=5)
        rolling = constructor(values).rolling(window=indexer, min_periods=3)
        result = rolling.apply(lambda x: x.skew())
        expected = constructor(
            [0.0, 2.23239689, 2.22950889, 2.22834089, 2.22909189, 2.23198989, 0.0, 0.0, numpy.nan, numpy.nan])
        self.assertEqual(None, assert_equal(result, expected))
