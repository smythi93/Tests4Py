import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def run_interval(old_min, old_max, new_min, new_max):
    fig, ax = plt.subplots()
    axis = ax.xaxis
    axis.set_data_interval(old_min, old_max, ignore=True)
    axis.set_data_interval(new_min, new_max, ignore=False)
    r = [round(float(v), 9) for v in axis.get_data_interval()]
    plt.close(fig)
    return r


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([1.0, 0.0], run_interval(1.0, 0.0, 0.3, 0.7))

    def test_diversity_2(self):
        self.assertEqual([1.0, 0.0], run_interval(1.0, 0.0, 0.2, 0.8))

    def test_diversity_3(self):
        self.assertEqual([2.0, 0.0], run_interval(2.0, 0.0, 0.5, 1.5))

    def test_diversity_4(self):
        self.assertEqual([5.0, 1.0], run_interval(5.0, 1.0, 2.0, 4.0))

    def test_diversity_5(self):
        self.assertEqual([10.0, 0.0], run_interval(10.0, 0.0, 3.0, 7.0))

    def test_diversity_6(self):
        self.assertEqual([1.0, -1.0], run_interval(1.0, -1.0, -0.5, 0.5))

    def test_diversity_7(self):
        self.assertEqual([0.0, -2.0], run_interval(0.0, -2.0, -1.5, -0.5))

    def test_diversity_8(self):
        self.assertEqual([100.0, 50.0], run_interval(100.0, 50.0, 60.0, 90.0))

    def test_diversity_9(self):
        self.assertEqual([3.0, 2.0], run_interval(3.0, 2.0, 2.3, 2.7))

    def test_diversity_10(self):
        self.assertEqual([1.0, 0.0], run_interval(1.0, 0.0, 0.4, 0.6))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([0.0, 1.0], run_interval(0.0, 1.0, 0.3, 0.7))

    def test_diversity_2(self):
        self.assertEqual([0.0, 2.0], run_interval(0.0, 2.0, 0.5, 1.5))

    def test_diversity_3(self):
        self.assertEqual([-1.0, 1.0], run_interval(-1.0, 1.0, -0.5, 0.5))

    def test_diversity_4(self):
        self.assertEqual([1.0, 5.0], run_interval(1.0, 5.0, 2.0, 4.0))

    def test_diversity_5(self):
        self.assertEqual([0.0, 10.0], run_interval(0.0, 10.0, 3.0, 7.0))

    def test_diversity_6(self):
        self.assertEqual([-2.0, 0.0], run_interval(-2.0, 0.0, -1.5, -0.5))

    def test_diversity_7(self):
        self.assertEqual([50.0, 100.0], run_interval(50.0, 100.0, 60.0, 90.0))

    def test_diversity_8(self):
        self.assertEqual([2.0, 3.0], run_interval(2.0, 3.0, 2.3, 2.7))

    def test_diversity_9(self):
        self.assertEqual([0.0, 1.0], run_interval(0.0, 1.0, 0.4, 0.6))

    def test_diversity_10(self):
        self.assertEqual([-5.0, 5.0], run_interval(-5.0, 5.0, -1.0, 1.0))
