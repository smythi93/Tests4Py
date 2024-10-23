import unittest
from pandas import pandas
from pandas._testing import assert_index_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        midx1 = pandas.MultiIndex.from_product([[1681, 1682], [1683, 1684]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[1681, 1682], [1683, 1684]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_2(self):
        midx1 = pandas.MultiIndex.from_product([[7411, 7412], [7413, 7414]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[7411, 7412], [7413, 7414]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_3(self):
        midx1 = pandas.MultiIndex.from_product([[4402, 4403], [4404, 4405]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[4402, 4403], [4404, 4405]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_4(self):
        midx1 = pandas.MultiIndex.from_product([[5355, 5356], [5357, 5358]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[5355, 5356], [5357, 5358]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_5(self):
        midx1 = pandas.MultiIndex.from_product([[5936, 5937], [5938, 5939]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[5936, 5937], [5938, 5939]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_6(self):
        midx1 = pandas.MultiIndex.from_product([[8178, 8179], [8180, 8181]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[8178, 8179], [8180, 8181]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_7(self):
        midx1 = pandas.MultiIndex.from_product([[6050, 6051], [6052, 6053]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[6050, 6051], [6052, 6053]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_8(self):
        midx1 = pandas.MultiIndex.from_product([[1297, 1298], [1299, 1300]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[1297, 1298], [1299, 1300]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_9(self):
        midx1 = pandas.MultiIndex.from_product([[9199, 9200], [9201, 9202]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[9199, 9200], [9201, 9202]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_10(self):
        midx1 = pandas.MultiIndex.from_product([[8838, 8839], [8840, 8841]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[8838, 8839], [8840, 8841]], names=['c', 'd'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        midx1 = pandas.MultiIndex.from_product([[3333, 3334], [3335, 3336]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[3333, 3334], [3335, 3336]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_2(self):
        midx1 = pandas.MultiIndex.from_product([[2217, 2218], [2219, 2220]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[2217, 2218], [2219, 2220]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_3(self):
        midx1 = pandas.MultiIndex.from_product([[8595, 8596], [8597, 8598]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[8595, 8596], [8597, 8598]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_4(self):
        midx1 = pandas.MultiIndex.from_product([[700, 701], [702, 703]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[700, 701], [702, 703]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_5(self):
        midx1 = pandas.MultiIndex.from_product([[7741, 7742], [7743, 7744]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[7741, 7742], [7743, 7744]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_6(self):
        midx1 = pandas.MultiIndex.from_product([[5236, 5237], [5238, 5239]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[5236, 5237], [5238, 5239]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_7(self):
        midx1 = pandas.MultiIndex.from_product([[161, 162], [163, 164]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[161, 162], [163, 164]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_8(self):
        midx1 = pandas.MultiIndex.from_product([[6959, 6960], [6961, 6962]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[6959, 6960], [6961, 6962]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_9(self):
        midx1 = pandas.MultiIndex.from_product([[2183, 2184], [2185, 2186]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[2183, 2184], [2185, 2186]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)

    def test_diversity_10(self):
        midx1 = pandas.MultiIndex.from_product([[1689, 1690], [1691, 1692]], names=['a', 'b'])
        midx2 = pandas.MultiIndex.from_product([[1689, 1690], [1691, 1692]], names=['b', 'a'])
        join_idx, lidx, ridx = midx1.join(midx2, return_indexers=False)
        assert_index_equal(midx1, join_idx)
        self.assertEqual(None, lidx)
