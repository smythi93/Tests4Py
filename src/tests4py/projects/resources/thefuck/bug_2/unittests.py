import unittest
from thefuck.utils import get_all_executables


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIn('mnsdgjefh', get_all_executables())

    def test_diversity_2(self):
        self.assertIn('NYEfTEWuJlisaiHgK', get_all_executables())

    def test_diversity_3(self):
        self.assertIn('JJFgWmDN', get_all_executables())

    def test_diversity_4(self):
        self.assertIn('runfXeIVrZAWplDW', get_all_executables())

    def test_diversity_5(self):
        self.assertIn('wExmEGsKxhBQog', get_all_executables())

    def test_diversity_6(self):
        self.assertIn('dgGqJoBnq', get_all_executables())

    def test_diversity_7(self):
        self.assertIn('LPXADgIZXbEayKR', get_all_executables())

    def test_diversity_8(self):
        self.assertIn('cwmvbtfEAHWCzHgg', get_all_executables())

    def test_diversity_9(self):
        self.assertIn('SESWAgGOTAmvtMsGr', get_all_executables())

    def test_diversity_10(self):
        self.assertIn('RQjelimEumbvIgjIH', get_all_executables())


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIn('mount', get_all_executables())

    def test_diversity_2(self):
        self.assertIn('last', get_all_executables())

    def test_diversity_3(self):
        self.assertIn('heap', get_all_executables())

    def test_diversity_4(self):
        self.assertIn('pip', get_all_executables())

    def test_diversity_5(self):
        self.assertIn('istack', get_all_executables())

    def test_diversity_6(self):
        self.assertIn('jarsigner', get_all_executables())

    def test_diversity_7(self):
        self.assertIn('libtool', get_all_executables)

    def test_diversity_8(self):
        self.assertIn('nl', get_all_executables())

    def test_diversity_9(self):
        self.assertIn('bundler', get_all_executables())

    def test_diversity_10(self):
        self.assertIn('ifconfig', get_all_executables())
