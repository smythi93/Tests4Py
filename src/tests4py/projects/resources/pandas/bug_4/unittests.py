import unittest
from pandas import pandas
import numpy
from pandas._testing import assert_index_equal, assert_numpy_array_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 4919], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_2(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 564], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_3(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 765], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_4(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 543], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_5(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 234], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_6(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 645], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_7(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 231], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_8(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 765], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_9(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 432], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_10(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 756], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 432], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_2(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 645], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_3(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 12], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_4(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 222], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_5(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 5454], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_6(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 6643], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_7(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 654], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_8(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 333], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_9(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 4010], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))

    def test_diversity_10(self):
        midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
        idx = pandas.Index([1, 2, 1550], name='b')
        jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
        exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
        exp_lidx = numpy.array([1, 2, 5, 6, 9, 10, 13, 14], dtype=numpy.intp)
        exp_ridx = numpy.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=numpy.intp)
        assert_index_equal(jidx, exp_idx)
        self.assertEqual(None, assert_numpy_array_equal(lidx, exp_lidx))
