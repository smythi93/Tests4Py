import unittest
from unittest import TestCase
from expression.evaluate import evaluate


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(AssertionError, evaluate("30/(3-1)-1*4"))

    def test_diversity_2(self):
        self.assertEqual(AssertionError, evaluate("550/11*1"))

    def test_diversity_3(self):
        self.assertEqual(ZeroDivisionError, evaluate("20/(3-3)"))

    def test_diversity_4(self):
        self.assertEqual(AssertionError, evaluate("45+(3+3)+5"))

    def test_diversity_5(self):
        self.assertEqual(AssertionError, evaluate("(80/5)+(1-8)"))

    def test_diversity_6(self):
        self.assertEqual(AssertionError, evaluate("50/(2*4)"))

    def test_diversity_7(self):
        self.assertEqual(AssertionError, evaluate("30/(8/4)"))

    def test_diversity_8(self):
        self.assertEqual(AssertionError, evaluate("(2+1)*4"))

    def test_diversity_9(self):
        self.assertEqual(AssertionError, evaluate("4/(3-0)*3"))

    def test_diversity_10(self):
        self.assertRaises(ValueError, evaluate("(4-2)*6"))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(5, evaluate(" ( 2 + 3 ) "))

    def test_diversity_2(self):
        self.assertAlmostEqual(0.5, evaluate(" 2 / 4 "), 5)

    def test_diversity_3(self):
        self.assertEqual(5, evaluate(" ( 30 / 5 ) / ( 3 + 3 ) "))

    def test_diversity_4(self):
        self.assertEqual(40, evaluate(" 40 / 40 "))

    def test_diversity_5(self):
        self.assertEqual(16, evaluate(" 4 * 4 "))

    def test_diversity_6(self):
        self.assertEqual(2, evaluate(" 40 / ( 2 + 3 ) "))

    def test_diversity_7(self):
        self.assertEqual(2, evaluate(" ( 2 + 3 ) - 21 + 4 "))

    def test_diversity_8(self):
        self.assertEqual(2, evaluate(" ( 2 + 3 ) - 5 * 3 "))

    def test_diversity_9(self):
        self.assertEqual(2, evaluate(" 300 - ( 12 + 3 ) "))

    def test_diversity_10(self):
        self.assertEqual(2, evaluate(" 15 - ( 2 + 3 ) "))
