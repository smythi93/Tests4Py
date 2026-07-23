import unittest

# noinspection PyUnresolvedReferences
from tqdm import tqdm


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIsInstance(tqdm.format_meter(1340, None, 41.09, unit_scale=694.6), str)

    def test_diversity_2(self):
        self.assertIsInstance(tqdm.format_meter(3860, None, 67.29, unit_scale=416.0), str)

    def test_diversity_3(self):
        self.assertIsInstance(tqdm.format_meter(786, None, 9.16, unit_scale=704.0), str)

    def test_diversity_4(self):
        self.assertIsInstance(tqdm.format_meter(4333, None, 79.3, unit_scale=930.0), str)

    def test_diversity_5(self):
        self.assertIsInstance(tqdm.format_meter(898, None, 45.64, unit_scale=120.89), str)

    def test_diversity_6(self):
        self.assertIsInstance(tqdm.format_meter(3820, None, 68.57, unit_scale=671.8), str)

    def test_diversity_7(self):
        self.assertIsInstance(tqdm.format_meter(4300, None, 89.02, unit_scale=865.0), str)

    def test_diversity_8(self):
        self.assertIsInstance(tqdm.format_meter(4304, None, 67.2, unit_scale=424.9), str)

    def test_diversity_9(self):
        self.assertIsInstance(tqdm.format_meter(2984, None, 8.26, unit_scale=367.61), str)

    def test_diversity_10(self):
        self.assertIsInstance(tqdm.format_meter(890, None, 4.65, unit_scale=833.0), str)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIsInstance(tqdm.format_meter(4199, 4487, 15.09, unit_scale=904.15), str)

    def test_diversity_2(self):
        self.assertIsInstance(tqdm.format_meter(4018, 4136, 18.88, unit_scale=940.72), str)

    def test_diversity_3(self):
        self.assertIsInstance(tqdm.format_meter(4797, 4863, 7.83, unit_scale=528.0), str)

    def test_diversity_4(self):
        self.assertIsInstance(tqdm.format_meter(1162, 1212, 25.04, unit_scale=630.0), str)

    def test_diversity_5(self):
        self.assertIsInstance(tqdm.format_meter(297, 1306, 62.78, unit_scale=427.2), str)

    def test_diversity_6(self):
        self.assertIsInstance(tqdm.format_meter(2014, 2055, 79.18, unit_scale=6.5), str)

    def test_diversity_7(self):
        self.assertIsInstance(tqdm.format_meter(118, 3874, 71.12, unit_scale=227.4), str)

    def test_diversity_8(self):
        self.assertIsInstance(tqdm.format_meter(4652, 7883, 84.01, unit_scale=264.58), str)

    def test_diversity_9(self):
        self.assertIsInstance(tqdm.format_meter(3964, 6111, 8.49, unit_scale=440.82), str)

    def test_diversity_10(self):
        self.assertIsInstance(tqdm.format_meter(2877, 5922, 42.55, unit_scale=979.6), str)

