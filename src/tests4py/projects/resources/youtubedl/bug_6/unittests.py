import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import parse_dfxp_time_expr


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(None, parse_dfxp_time_expr(''))
        self.assertEqual(3925.0, parse_dfxp_time_expr('01:05:25'))

    def test_diversity_2(self):
        self.assertEqual(None, parse_dfxp_time_expr(None))
        self.assertEqual(38.0, parse_dfxp_time_expr('38'))

    def test_diversity_3(self):
        self.assertEqual(None, parse_dfxp_time_expr(''))
        self.assertEqual(324.4, parse_dfxp_time_expr('324.4'))

    def test_diversity_4(self):
        self.assertEqual(None, parse_dfxp_time_expr(''))
        self.assertEqual(599.4, parse_dfxp_time_expr('599.4'))

    def test_diversity_5(self):
        self.assertEqual(None, parse_dfxp_time_expr(''))
        self.assertEqual(11185.0, parse_dfxp_time_expr('03:06:25'))

    def test_diversity_6(self):
        self.assertEqual(None, parse_dfxp_time_expr(None))
        self.assertEqual(29752.0, parse_dfxp_time_expr('08:15:52'))

    def test_diversity_7(self):
        self.assertEqual(None, parse_dfxp_time_expr(''))
        self.assertEqual(527.6, parse_dfxp_time_expr('527.6s'))

    def test_diversity_8(self):
        self.assertEqual(None, parse_dfxp_time_expr(None))
        self.assertEqual(11943.832, parse_dfxp_time_expr('03:19:03.832'))

    def test_diversity_9(self):
        self.assertEqual(None, parse_dfxp_time_expr(None))
        self.assertEqual(511.8, parse_dfxp_time_expr('511.8s'))

    def test_diversity_10(self):
        self.assertEqual(None, parse_dfxp_time_expr(None))
        self.assertEqual(134.0, parse_dfxp_time_expr('134.0s'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(10749.862, parse_dfxp_time_expr('02:59:09.862'))

    def test_diversity_2(self):
        self.assertEqual(6320.175, parse_dfxp_time_expr('01:45:20.175'))

    def test_diversity_3(self):
        self.assertEqual(62.1, parse_dfxp_time_expr('62.1'))

    def test_diversity_4(self):
        self.assertEqual(222.0, parse_dfxp_time_expr('222.0s'))

    def test_diversity_5(self):
        self.assertEqual(24440.0, parse_dfxp_time_expr('06:47:20'))

    def test_diversity_6(self):
        self.assertEqual(390.4, parse_dfxp_time_expr('390.4s'))

    def test_diversity_7(self):
        self.assertEqual(16040.701, parse_dfxp_time_expr('04:27:20.701'))

    def test_diversity_8(self):
        self.assertEqual(10414.095, parse_dfxp_time_expr('02:53:34.095'))

    def test_diversity_9(self):
        self.assertEqual(284.0, parse_dfxp_time_expr('284s'))

    def test_diversity_10(self):
        self.assertEqual(33453.0, parse_dfxp_time_expr('09:17:33'))
