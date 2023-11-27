import unittest
from math import sqrt

# noinspection PyUnresolvedReferences
from middle import middle


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(7, middle(7, 5, 10))

    def test_diversity_2(self):
        self.assertEqual(77, middle(77, 32, 93))

    def test_diversity_3(self):
        self.assertEqual(-3, middle(-3, -5, -2))

    def test_diversity_4(self):
        self.assertEqual(-10, middle(-10, -17, -8))

    def test_diversity_5(self):
        self.assertAlmostEqual(2.7, middle(2.7, 0.5, 3.5), 5)

    def test_diversity_6(self):
        self.assertEqual("d", middle("d", "c", "e"))

    def test_diversity_7(self):
        self.assertEqual("program", middle("python", "paradox", "python"))

    def test_diversity_8(self):
        self.assertEqual(b"d", middle(b"d", b"c", b"e"))

    def test_diversity_9(self):
        self.assertEqual(b"program", middle(b"program", b"paradox", b"python"))

    def test_diversity_10(self):
        self.assertAlmostEqual(sqrt(4), middle(sqrt(4), 2 / 4, 2**4))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(7, middle(10, 7, 5))

    def test_diversity_2(self):
        self.assertEqual(77, middle(93, 77, 32))

    def test_diversity_3(self):
        self.assertEqual(-3, middle(-5, -3, -2))

    def test_diversity_4(self):
        self.assertEqual(-10, middle(-17, -10, -8))

    def test_diversity_5(self):
        self.assertAlmostEqual(4.5, middle(0.350, 4.5, 6.7), 5)

    def test_diversity_6(self):
        self.assertEqual("l", middle("k", "l", "m"))

    def test_diversity_7(self):
        self.assertEqual("program", middle("paradox", "program", "python"))

    def test_diversity_8(self):
        self.assertEqual(b"l", middle(b"k", b"l", b"m"))

    def test_diversity_9(self):
        self.assertEqual(b"program", middle(b"python", b"program", b"paradox"))

    def test_diversity_10(self):
        self.assertAlmostEqual(sqrt(225), middle(abs(-10), sqrt(225), pow(5, 2)))
