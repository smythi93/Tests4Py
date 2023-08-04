import unittest
from math import sqrt

# noinspection PyUnresolvedReferences
from middle import middle


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(4, middle(4, 2, 5))

    def test_diversity_2(self):
        self.assertEqual(64, middle(64, 63, 125))

    def test_diversity_3(self):
        self.assertEqual(-3, middle(-3, -45, 12))

    def test_diversity_4(self):
        self.assertEqual(-2, middle(-2, -3, -1))

    def test_diversity_5(self):
        self.assertAlmostEqual(1.5, middle(1.5, 0.876, 1.51), 5)

    def test_diversity_6(self):
        self.assertEqual("a", middle("a", "", "b"))

    def test_diversity_7(self):
        self.assertEqual("program", middle("program", "automated", "repair"))

    def test_diversity_8(self):
        self.assertEqual(b"a", middle(b"a", b"", b"b"))

    def test_diversity_9(self):
        self.assertEqual(b"program", middle(b"program", b"automated", b"repair"))

    def test_diversity_10(self):
        self.assertAlmostEqual(sqrt(2), middle(sqrt(2), 1 / 2, 2**3))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(4, middle(2, 4, 5))

    def test_diversity_2(self):
        self.assertEqual(64, middle(125, 63, 64))

    def test_diversity_3(self):
        self.assertEqual(-3, middle(-45, -3, 12))

    def test_diversity_4(self):
        self.assertEqual(-2, middle(-3, -1, -2))

    def test_diversity_5(self):
        self.assertAlmostEqual(1.5, middle(0.876, 1.51, 1.5), 5)

    def test_diversity_6(self):
        self.assertEqual("a", middle("", "a", "b"))

    def test_diversity_7(self):
        self.assertEqual("program", middle("automated", "repair", "program"))

    def test_diversity_8(self):
        self.assertEqual(b"a", middle(b"", b"a", b"b"))

    def test_diversity_9(self):
        self.assertEqual(b"program", middle(b"automated", b"repair", b"program"))

    def test_diversity_10(self):
        self.assertAlmostEqual(2, middle(2, 2, 4))
