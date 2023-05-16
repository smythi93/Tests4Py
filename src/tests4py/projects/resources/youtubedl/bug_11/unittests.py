import unittest

from youtube_dl.utils import str_to_int


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(str_to_int(523), 523)

    def test_diversity_2(self):
        self.assertEqual(str_to_int(12), 12)

    def test_diversity_3(self):
        self.assertEqual(str_to_int(12356734), 12356734)

    def test_diversity_4(self):
        self.assertEqual(str_to_int(12.3), 12.3)

    def test_diversity_5(self):
        self.assertEqual(str_to_int(0), 0)

    def test_diversity_6(self):
        self.assertEqual(str_to_int(0.1), 0.1)

    def test_diversity_7(self):
        self.assertEqual(str_to_int(-1), -1)

    def test_diversity_8(self):
        self.assertEqual(str_to_int(-0), -0)

    def test_diversity_9(self):
        self.assertEqual(str_to_int(100.3), 100.3)

    def test_diversity_10(self):
        self.assertEqual(str_to_int(-900.5), -900.5)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(str_to_int('123,456'), 123456)

    def test_diversity_2(self):
        self.assertEqual(str_to_int('123.456'), 123456)

    def test_diversity_3(self):
        self.assertEqual(str_to_int('.1'), 1)

    def test_diversity_4(self):
        self.assertEqual(str_to_int('100.1'), 1001)

    def test_diversity_5(self):
        self.assertEqual(str_to_int('-100'), -100)

    def test_diversity_6(self):
        self.assertEqual(str_to_int('-5.5'), -55)

    def test_diversity_7(self):
        self.assertEqual(str_to_int('-123,4'), -1234)

    def test_diversity_8(self):
        self.assertEqual(str_to_int('-123.3'), -1233)

    def test_diversity_9(self):
        self.assertEqual(str_to_int('-0.1'), -1)

    def test_diversity_10(self):
        self.assertEqual(str_to_int('-1'), -1)
