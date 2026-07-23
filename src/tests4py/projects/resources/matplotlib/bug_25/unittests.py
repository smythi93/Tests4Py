import unittest
import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib.collections import EventCollection

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        arr = np.array([3.891, -1.492, -8.723, -1.056], dtype=float)
        EventCollection(arr)
        self.assertEqual([3.891, -1.492, -8.723, -1.056], [round(float(v), 6) for v in arr])

    def test_diversity_2(self):
        arr = np.array([27.999, 40.781, -44.375, -18.22, 47.381], dtype=float)
        EventCollection(arr)
        self.assertEqual([27.999, 40.781, -44.375, -18.22, 47.381], [round(float(v), 6) for v in arr])

    def test_diversity_3(self):
        arr = np.array([-22.317, 29.798, -9.315, -12.128, 18.41, 47.231], dtype=float)
        EventCollection(arr)
        self.assertEqual([-22.317, 29.798, -9.315, -12.128, 18.41, 47.231], [round(float(v), 6) for v in arr])

    def test_diversity_4(self):
        arr = np.array([43.461, -17.406, -0.796], dtype=float)
        EventCollection(arr)
        self.assertEqual([43.461, -17.406, -0.796], [round(float(v), 6) for v in arr])

    def test_diversity_5(self):
        arr = np.array([-9.835, -35.005, -49.926, 1.727, 46.933, 23.972], dtype=float)
        EventCollection(arr)
        self.assertEqual([-9.835, -35.005, -49.926, 1.727, 46.933, 23.972], [round(float(v), 6) for v in arr])

    def test_diversity_6(self):
        arr = np.array([-45.397, -2.903, 9.853, -4.775], dtype=float)
        EventCollection(arr)
        self.assertEqual([-45.397, -2.903, 9.853, -4.775], [round(float(v), 6) for v in arr])

    def test_diversity_7(self):
        arr = np.array([2.302, 19.67, -14.372, -7.871, -3.261, 23.046], dtype=float)
        EventCollection(arr)
        self.assertEqual([2.302, 19.67, -14.372, -7.871, -3.261, 23.046], [round(float(v), 6) for v in arr])

    def test_diversity_8(self):
        arr = np.array([-13.178, 31.327, -18.202, -12.734, -10.242, -41.97], dtype=float)
        EventCollection(arr)
        self.assertEqual([-13.178, 31.327, -18.202, -12.734, -10.242, -41.97], [round(float(v), 6) for v in arr])

    def test_diversity_9(self):
        arr = np.array([13.919, 32.382, -22.804, 41.061], dtype=float)
        EventCollection(arr)
        self.assertEqual([13.919, 32.382, -22.804, 41.061], [round(float(v), 6) for v in arr])

    def test_diversity_10(self):
        arr = np.array([41.169, 7.544, -31.312, -18.972, 23.369, -15.734], dtype=float)
        EventCollection(arr)
        self.assertEqual([41.169, 7.544, -31.312, -18.972, 23.369, -15.734], [round(float(v), 6) for v in arr])

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        arr = np.array([-30.47, 21.856, 26.792], dtype=float)
        EventCollection(arr)
        self.assertEqual([-30.47, 21.856, 26.792], [round(float(v), 6) for v in arr])

    def test_diversity_2(self):
        arr = np.array([-39.069, -25.483, 23.942, 48.783], dtype=float)
        EventCollection(arr)
        self.assertEqual([-39.069, -25.483, 23.942, 48.783], [round(float(v), 6) for v in arr])

    def test_diversity_3(self):
        arr = np.array([-37.289, -1.248, 7.974, 34.921, 39.854], dtype=float)
        EventCollection(arr)
        self.assertEqual([-37.289, -1.248, 7.974, 34.921, 39.854], [round(float(v), 6) for v in arr])

    def test_diversity_4(self):
        arr = np.array([-43.712, -41.622, 20.774, 42.96], dtype=float)
        EventCollection(arr)
        self.assertEqual([-43.712, -41.622, 20.774, 42.96], [round(float(v), 6) for v in arr])

    def test_diversity_5(self):
        arr = np.array([-36.245, -35.893, -23.527, -8.224, 18.059, 30.458], dtype=float)
        EventCollection(arr)
        self.assertEqual([-36.245, -35.893, -23.527, -8.224, 18.059, 30.458], [round(float(v), 6) for v in arr])

    def test_diversity_6(self):
        arr = np.array([-39.613, -22.774, 4.819, 34.941], dtype=float)
        EventCollection(arr)
        self.assertEqual([-39.613, -22.774, 4.819, 34.941], [round(float(v), 6) for v in arr])

    def test_diversity_7(self):
        arr = np.array([-12.703, -9.201, 4.788, 17.582, 24.291], dtype=float)
        EventCollection(arr)
        self.assertEqual([-12.703, -9.201, 4.788, 17.582, 24.291], [round(float(v), 6) for v in arr])

    def test_diversity_8(self):
        arr = np.array([-36.711, -4.973, 8.812, 39.775, 43.551], dtype=float)
        EventCollection(arr)
        self.assertEqual([-36.711, -4.973, 8.812, 39.775, 43.551], [round(float(v), 6) for v in arr])

    def test_diversity_9(self):
        arr = np.array([-25.864, -13.859, -13.432, 27.179], dtype=float)
        EventCollection(arr)
        self.assertEqual([-25.864, -13.859, -13.432, 27.179], [round(float(v), 6) for v in arr])

    def test_diversity_10(self):
        arr = np.array([-46.172, 24.092, 37.958], dtype=float)
        EventCollection(arr)
        self.assertEqual([-46.172, 24.092, 37.958], [round(float(v), 6) for v in arr])
