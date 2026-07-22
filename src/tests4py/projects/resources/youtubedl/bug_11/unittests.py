import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import str_to_int


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(395678, str_to_int(395678))

    def test_diversity_2(self):
        self.assertEqual(7, str_to_int(7))

    def test_diversity_3(self):
        self.assertEqual(10, str_to_int(10))

    def test_diversity_4(self):
        self.assertEqual(2688, str_to_int(2688))

    def test_diversity_5(self):
        self.assertEqual(9, str_to_int(9))

    def test_diversity_6(self):
        self.assertEqual(19, str_to_int(19))

    def test_diversity_7(self):
        self.assertEqual(6, str_to_int(6))

    def test_diversity_8(self):
        self.assertEqual(1860408, str_to_int(1860408))

    def test_diversity_9(self):
        self.assertEqual(18512, str_to_int(18512))

    def test_diversity_10(self):
        self.assertEqual(320228, str_to_int(320228))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(665203, str_to_int('665.203'))

    def test_diversity_2(self):
        self.assertEqual(695562, str_to_int('695,562'))

    def test_diversity_3(self):
        self.assertEqual(36608, str_to_int('36,608'))

    def test_diversity_4(self):
        self.assertEqual(889762, str_to_int('889,762'))

    def test_diversity_5(self):
        self.assertEqual(689919, str_to_int('689.919'))

    def test_diversity_6(self):
        self.assertEqual(520943, str_to_int('520.943'))

    def test_diversity_7(self):
        self.assertEqual(62830889, str_to_int('62.830.889'))

    def test_diversity_8(self):
        self.assertEqual(8714, str_to_int('8,714'))

    def test_diversity_9(self):
        self.assertEqual(8711942, str_to_int('8.711.942'))

    def test_diversity_10(self):
        self.assertEqual(289401, str_to_int('289,401'))
