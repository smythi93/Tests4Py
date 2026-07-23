import unittest

# noinspection PyUnresolvedReferences
from tqdm._tqdm import format_sizeof


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('1.00K', format_sizeof(999.98))

    def test_diversity_2(self):
        self.assertEqual('100K', format_sizeof(99980.0))

    def test_diversity_3(self):
        self.assertEqual('1.00T', format_sizeof(999960000000.0))

    def test_diversity_4(self):
        self.assertEqual('100', format_sizeof(99.99))

    def test_diversity_5(self):
        self.assertEqual('100M', format_sizeof(99980000.0))

    def test_diversity_6(self):
        self.assertEqual('100M', format_sizeof(99990000.0))

    def test_diversity_7(self):
        self.assertEqual('100G', format_sizeof(99960000000.0))

    def test_diversity_8(self):
        self.assertEqual('100K', format_sizeof(99970.0))

    def test_diversity_9(self):
        self.assertEqual('100G', format_sizeof(99980000000.0))

    def test_diversity_10(self):
        self.assertEqual('100', format_sizeof(99.97))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('7.50G', format_sizeof(7500000000.0))

    def test_diversity_2(self):
        self.assertEqual('6.90G', format_sizeof(6900000000.0))

    def test_diversity_3(self):
        self.assertEqual('7.27K', format_sizeof(7270.0))

    def test_diversity_4(self):
        self.assertEqual('2.76K', format_sizeof(2760.0))

    def test_diversity_5(self):
        self.assertEqual('5.70', format_sizeof(5.7))

    def test_diversity_6(self):
        self.assertEqual('3.30K', format_sizeof(3300.0))

    def test_diversity_7(self):
        self.assertEqual('3.00M', format_sizeof(3000000.0))

    def test_diversity_8(self):
        self.assertEqual('3.90G', format_sizeof(3900000000.0))

    def test_diversity_9(self):
        self.assertEqual('6.79M', format_sizeof(6790000.0))

    def test_diversity_10(self):
        self.assertEqual('1.81M', format_sizeof(1810000.0))

