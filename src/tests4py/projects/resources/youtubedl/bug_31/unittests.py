import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import parse_duration


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(906.0, parse_duration('15.1 minute'))

    def test_diversity_2(self):
        self.assertEqual(59760.00000000001, parse_duration('16.6hour'))

    def test_diversity_3(self):
        self.assertEqual(871200.0, parse_duration('242hour'))

    def test_diversity_4(self):
        self.assertEqual(957600.0, parse_duration('266 hour'))

    def test_diversity_5(self):
        self.assertEqual(5760.0, parse_duration('96minutes'))

    def test_diversity_6(self):
        self.assertEqual(1032.0, parse_duration('17.2minutes'))

    def test_diversity_7(self):
        self.assertEqual(564.0, parse_duration('9.4minutes'))

    def test_diversity_8(self):
        self.assertEqual(390.0, parse_duration('6.5 minute'))

    def test_diversity_9(self):
        self.assertEqual(912.0, parse_duration('15.2mins'))

    def test_diversity_10(self):
        self.assertEqual(8820.0, parse_duration('147min'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(27173, parse_duration('7:32:53'))

    def test_diversity_2(self):
        self.assertEqual(80419, parse_duration('22:20:19'))

    def test_diversity_3(self):
        self.assertEqual(277, parse_duration('4:37'))

    def test_diversity_4(self):
        self.assertEqual(3244, parse_duration('54:04'))

    def test_diversity_5(self):
        self.assertEqual(3493, parse_duration('3493s'))

    def test_diversity_6(self):
        self.assertEqual(12312, parse_duration('3:25:12'))

    def test_diversity_7(self):
        self.assertEqual(3765, parse_duration('3765s'))

    def test_diversity_8(self):
        self.assertEqual(1936, parse_duration('1936s'))

    def test_diversity_9(self):
        self.assertEqual(3594, parse_duration('59:54'))

    def test_diversity_10(self):
        self.assertEqual(61004, parse_duration('16:56:44'))
