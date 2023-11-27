import unittest
from expression.evaluate import evaluate
from expression.expr.parse import parse
from expression.expr.arithmetic import Constant, Div, Add, Mul


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertRaises(ZeroDivisionError, evaluate("100 / (20 - 20)"))

    def test_diversity_2(self):
        self.assertRaises(ZeroDivisionError, evaluate, " 1 / 0 ")

    def test_diversity_3(self):
        self.assertRaises(ZeroDivisionError, evaluate("200 + 100 / 0"))

    def test_diversity_4(self):
        term = parse("1 / 0")
        self.assertIsInstance(term, Div)
        self.assertIsInstance(term.left, Constant)
        self.assertIsInstance(term.right, Constant)
        self.assertEqual(1, term.left.value)
        self.assertEqual(0, term.right.value)

    def test_diversity_5(self):
        self.assertRaises(ZeroDivisionError, evaluate("(108 - 16) / 0"))

    def test_diversity_6(self):
        self.assertRaises(ZeroDivisionError, evaluate("50 / (25 * 0)"))

    def test_diversity_7(self):
        self.assertRaises(ZeroDivisionError, evaluate("30 / (8 - 8)"))

    def test_diversity_8(self):
        self.assertRaises(ZeroDivisionError, evaluate("(10) / (4 - 4)"))

    def test_diversity_9(self):
        self.assertRaises(ZeroDivisionError, evaluate("4 / 0 * 3"))

    def test_diversity_10(self):
        self.assertRaises(ZeroDivisionError, evaluate("(2 - 2) * 6"))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(5, evaluate("(2 + 3)"))

    def test_diversity_2(self):
        self.assertAlmostEqual(0.5, evaluate("2 / 4"), 5)

    def test_diversity_3(self):
        term = Add(Constant(1), Constant(3))
        self.assertEqual(4, term.evaluate())

    def test_diversity_4(self):
        term = Mul(Add(Constant(1), Constant(3)), Constant(2))
        self.assertEqual(8, term.evaluate())

    def test_diversity_5(self):
        self.assertEqual(0, evaluate("0"))

    def test_diversity_6(self):
        term = parse("(1 + 0) * 2")
        self.assertIsInstance(term, Mul)
        self.assertIsInstance(term.left, Add)
        self.assertIsInstance(term.right, Constant)
        self.assertIsInstance(term.left.left, Constant)
        self.assertIsInstance(term.left.right, Constant)
        self.assertEqual(1, term.left.left.value)
        self.assertEqual(0, term.left.right.value)
        self.assertEqual(2, term.right.value)

    def test_diversity_7(self):
        term = parse("1 + 0")
        self.assertIsInstance(term, Add)
        self.assertIsInstance(term.left, Constant)
        self.assertIsInstance(term.right, Constant)
        self.assertEqual(1, term.left.value)
        self.assertEqual(0, term.right.value)

    def test_diversity_8(self):
        self.assertEqual(2, evaluate("(2 + 3) * 5"))

    def test_diversity_9(self):
        term = parse("0")
        self.assertIsInstance(term, Constant)
        self.assertEqual(0, term.value)

    def test_diversity_10(self):
        self.assertEqual(2, evaluate("15 - (2 + 3)"))
