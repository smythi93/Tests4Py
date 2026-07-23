import unittest
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.transforms as mtransforms
_DT = {'int8': np.int8, 'int16': np.int16, 'int32': np.int32, 'int64': np.int64, 'float64': np.float64}
def run_nonsingular(dtype, vmin, vmax):
    cast = int if 'int' in dtype else float
    out = mtransforms.nonsingular(_DT[dtype](cast(vmin)), _DT[dtype](cast(vmax)))
    return [round(float(v), 9) for v in out]


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([-128.128, -127.872], run_nonsingular('int8', -128, -128))

    def test_diversity_2(self):
        self.assertEqual([-128.0, 0.0], run_nonsingular('int8', -128, 0))

    def test_diversity_3(self):
        self.assertEqual([-128.0, 1.0], run_nonsingular('int8', -128, 1))

    def test_diversity_4(self):
        self.assertEqual([-32800.768, -32735.232], run_nonsingular('int16', -32768, -32768))

    def test_diversity_5(self):
        self.assertEqual([-32768.0, 0.0], run_nonsingular('int16', -32768, 0))

    def test_diversity_6(self):
        self.assertEqual([-32768.0, 2.0], run_nonsingular('int16', -32768, 2))

    def test_diversity_7(self):
        self.assertEqual([-2149631131.648, -2145336164.352], run_nonsingular('int32', -2147483648, -2147483648))

    def test_diversity_8(self):
        self.assertEqual([-2147483648.0, 0.0], run_nonsingular('int32', -2147483648, 0))

    def test_diversity_9(self):
        self.assertEqual([-9.23259540889163e+18, -9.214148664817921e+18], run_nonsingular('int64', -9223372036854775808, -9223372036854775808))

    def test_diversity_10(self):
        self.assertEqual([-9.223372036854776e+18, 0.0], run_nonsingular('int64', -9223372036854775808, 0))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([1.0, 5.0], run_nonsingular('float64', 1.0, 5.0))

    def test_diversity_2(self):
        self.assertEqual([-10.0, 10.0], run_nonsingular('float64', -10.0, 10.0))

    def test_diversity_3(self):
        self.assertEqual([0.5, 3.5], run_nonsingular('float64', 0.5, 3.5))

    def test_diversity_4(self):
        self.assertEqual([-2.5, 7.5], run_nonsingular('float64', -2.5, 7.5))

    def test_diversity_5(self):
        self.assertEqual([2.0, 8.0], run_nonsingular('float64', 2.0, 8.0))

    def test_diversity_6(self):
        self.assertEqual([-100.0, -50.0], run_nonsingular('float64', -100.0, -50.0))

    def test_diversity_7(self):
        self.assertEqual([3.14, 9.42], run_nonsingular('float64', 3.14, 9.42))

    def test_diversity_8(self):
        self.assertEqual([-1.0, 1.0], run_nonsingular('float64', -1.0, 1.0))

    def test_diversity_9(self):
        self.assertEqual([10.5, 20.5], run_nonsingular('float64', 10.5, 20.5))

    def test_diversity_10(self):
        self.assertEqual([-7.0, -3.0], run_nonsingular('float64', -7.0, -3.0))
