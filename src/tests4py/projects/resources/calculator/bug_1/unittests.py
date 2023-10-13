import unittest
import calc
from math import pi
from calc import sqrt, tan, cos, sin, main


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertAlmostEqual(ValueError, main("sqrt(-81)"), -1)

    def test_diversity_2(self):
        self.assertAlmostEqual(ValueError, main("sqrt(tan(5))"), -1)

    def test_diversity_3(self):
        self.assertAlmostEqual(ValueError, main("sqrt(sin(-2000))"), -1)

    def test_diversity_4(self):
        self.assertAlmostEqual(ValueError, main("sqrt(-64)"), -1)

    def test_diversity_5(self):
        self.assertAlmostEqual(ValueError, main("sqrt(sin(500))"), -1)

    def test_diversity_6(self):
        self.assertAlmostEqual(ValueError, main("sqrt(0)"), -1)

    def test_diversity_7(self):
        self.assertAlmostEqual(ValueError, main("sqrt(-25)"), -1)

    def test_diversity_8(self):
        self.assertRaises(AssertionError, sqrt, -1)

    def test_diversity_9(self):
        self.assertAlmostEqual(ValueError, main(f"sqrt(-7925)", -1))

    def test_diversity_10(self):
        self.assertAlmostEqual(ValueError, main("sqrt(cos(1600))"), -1)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertAlmostEqual(1.18055, main(f"tan({8901})"), 5)

    def test_diversity_2(self):
        self.assertAlmostEqual(-1.0, main(f"cos({pi})"), 5)

    def test_diversity_3(self):
        self.assertAlmostEqual(-1.22464, main(f"tan({pi})"), 5)

    def test_diversity_4(self):
        self.assertAlmostEqual(16, main(f"sqrt(256)"), 5)

    def test_diversity_5(self):
        self.assertAlmostEqual(16, main("sqrt(%d)" % 256), 5)

    def test_diversity_6(self):
        self.assertAlmostEqual(9, main("sqrt(81)"), 5)

    def test_diversity_7(self):
        self.assertAlmostEqual(15, main(f"sqrt(225)"), 5)

    def test_diversity_8(self):
        self.assertAlmostEqual(25, main("sqrt(625)"), 5)

    def test_diversity_9(self):
        self.assertAlmostEqual(0.15425, main(f"cos({180})"), 5)

    def test_diversity_10(self):
        self.assertAlmostEqual(6, main(f"sqrt(36)"), 5)
