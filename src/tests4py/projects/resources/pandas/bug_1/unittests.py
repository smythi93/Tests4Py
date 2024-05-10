import unittest
from pandas.core.dtypes.common import is_string_dtype
from pandas.core.dtypes.dtypes import PeriodDtype


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(1121)))

    def test_diversity_2(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(1244)))

    def test_diversity_3(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(4353)))

    def test_diversity_4(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(645)))

    def test_diversity_5(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(541)))

    def test_diversity_6(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(634)))

    def test_diversity_7(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(6345)))

    def test_diversity_8(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(123)))

    def test_diversity_9(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(456)))

    def test_diversity_10(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype(846)))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('-7333M')))

    def test_diversity_2(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('-8521S')))
    def test_diversity_3(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('-8534D')))

    def test_diversity_4(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('3627M')))

    def test_diversity_5(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('-3580D')))

    def test_diversity_6(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('3527H')))

    def test_diversity_7(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('9903D')))

    def test_diversity_8(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('5305A')))

    def test_diversity_9(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('-1833W')))

    def test_diversity_10(self):
        self.assertEqual(False, is_string_dtype(PeriodDtype('-7535D')))

