import unittest
from expression.evaluate import evaluate
from expression.expr.parse import parse
from expression.expr.arithmetic import Constant, Div, Add, Mul


class TestsFailing(unittest.TestCase):
    # Each failing test asserts the CORRECT (fixed) behaviour: dividing by zero
    # must raise a controlled error (AssertionError on the fixed build, or
    # ValueError). On the buggy build the division raises ZeroDivisionError,
    # which is not caught by assertRaises, so the test fails on buggy and passes
    # on fixed (fault-distinguishing).
    def test_diversity_1(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "1 / 0")

    def test_diversity_2(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "100 / (20 - 20)")

    def test_diversity_3(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "7 / (3 - 3)")

    def test_diversity_4(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "42 / (0 * 9)")

    def test_diversity_5(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "(5 + 6) / 0")

    def test_diversity_6(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "8 / (4 - 4)")

    def test_diversity_7(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "13 / (10 - 10)")

    def test_diversity_8(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "25 / (2 * 0)")

    def test_diversity_9(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "(9 + 1) / 0")

    def test_diversity_10(self):
        self.assertRaises((ValueError, AssertionError), evaluate, "6 / (7 - 7)")


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(5, evaluate("2 + 3"))

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
        self.assertEqual(7, evaluate("21 / 3"))

    def test_diversity_7(self):
        term = parse("1 + 0")
        self.assertIsInstance(term, Add)
        self.assertIsInstance(term.left, Constant)
        self.assertIsInstance(term.right, Constant)
        self.assertEqual(1, term.left.value)
        self.assertEqual(0, term.right.value)

    def test_diversity_8(self):
        self.assertEqual(25, evaluate("(2 + 3) * 5"))

    def test_diversity_9(self):
        term = parse("0")
        self.assertIsInstance(term, Constant)
        self.assertEqual(0, term.value)

    def test_diversity_10(self):
        self.assertEqual(10, evaluate("15 - (2 + 3)"))
