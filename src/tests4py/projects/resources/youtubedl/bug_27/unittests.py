import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import parse_dfxp_time_expr


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(7319.355, parse_dfxp_time_expr('02:01:59:355'))

    def test_diversity_2(self):
        self.assertEqual(5589.687, parse_dfxp_time_expr('01:33:09:687'))

    def test_diversity_3(self):
        self.assertEqual(16142.427, parse_dfxp_time_expr('04:29:02:427'))

    def test_diversity_4(self):
        self.assertEqual(16971.042, parse_dfxp_time_expr('04:42:51:042'))

    def test_diversity_5(self):
        self.assertEqual(8229.308, parse_dfxp_time_expr('02:17:09:308'))

    def test_diversity_6(self):
        self.assertEqual(10193.476, parse_dfxp_time_expr('02:49:53:476'))

    def test_diversity_7(self):
        self.assertEqual(2184.783, parse_dfxp_time_expr('00:36:24:783'))

    def test_diversity_8(self):
        self.assertEqual(19881.597, parse_dfxp_time_expr('05:31:21:597'))

    def test_diversity_9(self):
        self.assertEqual(27002.802, parse_dfxp_time_expr('07:30:02:802'))

    def test_diversity_10(self):
        self.assertEqual(28552.61, parse_dfxp_time_expr('07:55:52:610'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(450.8, parse_dfxp_time_expr('450.8s'))

    def test_diversity_2(self):
        self.assertEqual(15427.0, parse_dfxp_time_expr('04:17:07'))

    def test_diversity_3(self):
        self.assertEqual(426.6, parse_dfxp_time_expr('426.6s'))

    def test_diversity_4(self):
        self.assertEqual(542.1, parse_dfxp_time_expr('542.1'))

    def test_diversity_5(self):
        self.assertEqual(24772.0, parse_dfxp_time_expr('06:52:52'))

    def test_diversity_6(self):
        self.assertEqual(196.0, parse_dfxp_time_expr('196s'))

    def test_diversity_7(self):
        self.assertEqual(160.9, parse_dfxp_time_expr('160.9'))

    def test_diversity_8(self):
        self.assertEqual(158.0, parse_dfxp_time_expr('158s'))

    def test_diversity_9(self):
        self.assertEqual(3925.0, parse_dfxp_time_expr('01:05:25'))

    def test_diversity_10(self):
        self.assertEqual(48.4, parse_dfxp_time_expr('48.4s'))
