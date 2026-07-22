import unittest
import matplotlib
matplotlib.use('Agg')
from matplotlib.markers import MarkerStyle
def run_is_filled(marker, fillstyle):
    return bool(MarkerStyle(marker, fillstyle).is_filled())


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, run_is_filled('o', 'none'))

    def test_diversity_2(self):
        self.assertEqual(False, run_is_filled('v', 'none'))

    def test_diversity_3(self):
        self.assertEqual(False, run_is_filled('^', 'none'))

    def test_diversity_4(self):
        self.assertEqual(False, run_is_filled('8', 'none'))

    def test_diversity_5(self):
        self.assertEqual(False, run_is_filled('s', 'none'))

    def test_diversity_6(self):
        self.assertEqual(False, run_is_filled('p', 'none'))

    def test_diversity_7(self):
        self.assertEqual(False, run_is_filled('*', 'none'))

    def test_diversity_8(self):
        self.assertEqual(False, run_is_filled('h', 'none'))

    def test_diversity_9(self):
        self.assertEqual(False, run_is_filled('H', 'none'))

    def test_diversity_10(self):
        self.assertEqual(False, run_is_filled('D', 'none'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, run_is_filled('o', 'full'))

    def test_diversity_2(self):
        self.assertEqual(True, run_is_filled('v', 'full'))

    def test_diversity_3(self):
        self.assertEqual(True, run_is_filled('^', 'full'))

    def test_diversity_4(self):
        self.assertEqual(True, run_is_filled('8', 'full'))

    def test_diversity_5(self):
        self.assertEqual(True, run_is_filled('s', 'full'))

    def test_diversity_6(self):
        self.assertEqual(True, run_is_filled('p', 'full'))

    def test_diversity_7(self):
        self.assertEqual(True, run_is_filled('*', 'full'))

    def test_diversity_8(self):
        self.assertEqual(True, run_is_filled('h', 'full'))

    def test_diversity_9(self):
        self.assertEqual(True, run_is_filled('H', 'full'))

    def test_diversity_10(self):
        self.assertEqual(True, run_is_filled('d', 'full'))
