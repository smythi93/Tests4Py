import unittest
import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib.path import Path
def run_compound_codes(code_lists):
    paths = [Path(np.array([[float(k), float(k)] for k in range(len(cs))], dtype=float), cs) for cs in code_lists]
    return [int(c) for c in Path.make_compound_path(*paths).codes]


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([1, 2, 1, 2], run_compound_codes([[1, 2, 0], [1, 2]]))

    def test_diversity_2(self):
        self.assertEqual([1, 2, 1, 2], run_compound_codes([[1, 0, 2], [1, 2]]))

    def test_diversity_3(self):
        self.assertEqual([1, 2, 1, 2], run_compound_codes([[1, 2], [1, 0, 2]]))

    def test_diversity_4(self):
        self.assertEqual([1, 2, 1, 2, 1, 2], run_compound_codes([[1, 2, 0], [1, 2], [1, 2]]))

    def test_diversity_5(self):
        self.assertEqual([1, 2, 1, 2, 1, 2], run_compound_codes([[1, 2, 0, 1, 2], [1, 2]]))

    def test_diversity_6(self):
        self.assertEqual([1, 1, 2], run_compound_codes([[1, 0], [1, 2]]))

    def test_diversity_7(self):
        self.assertEqual([1, 2, 1, 2], run_compound_codes([[1, 2, 0], [1, 0, 2]]))

    def test_diversity_8(self):
        self.assertEqual([1, 2, 1, 2, 1, 2], run_compound_codes([[1, 2, 0], [1, 2, 0], [1, 2]]))

    def test_diversity_9(self):
        self.assertEqual([1, 2, 1, 2], run_compound_codes([[1, 2, 0, 0], [1, 2]]))

    def test_diversity_10(self):
        self.assertEqual([1, 2, 1, 2], run_compound_codes([[1, 0, 2, 0], [1, 2]]))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([1, 2, 1, 2], run_compound_codes([[1, 2], [1, 2]]))

    def test_diversity_2(self):
        self.assertEqual([1, 2, 2, 1, 2], run_compound_codes([[1, 2, 2], [1, 2]]))

    def test_diversity_3(self):
        self.assertEqual([1, 2, 1, 2, 2], run_compound_codes([[1, 2], [1, 2, 2]]))

    def test_diversity_4(self):
        self.assertEqual([1, 2, 2, 2, 1, 2], run_compound_codes([[1, 2, 2, 2], [1, 2]]))

    def test_diversity_5(self):
        self.assertEqual([1, 2, 1, 2, 1, 2], run_compound_codes([[1, 2], [1, 2], [1, 2]]))

    def test_diversity_6(self):
        self.assertEqual([1, 1, 2, 1, 2], run_compound_codes([[1, 1, 2], [1, 2]]))

    def test_diversity_7(self):
        self.assertEqual([1, 2, 2, 2, 2, 1, 2], run_compound_codes([[1, 2, 2, 2, 2], [1, 2]]))

    def test_diversity_8(self):
        self.assertEqual([1, 2, 1, 2, 1, 2], run_compound_codes([[1, 2, 1, 2], [1, 2]]))

    def test_diversity_9(self):
        self.assertEqual([1, 2, 1, 1, 2], run_compound_codes([[1, 2], [1, 1, 2]]))

    def test_diversity_10(self):
        self.assertEqual([1, 1, 1, 2, 1, 2], run_compound_codes([[1, 1, 1, 2], [1, 2]]))
