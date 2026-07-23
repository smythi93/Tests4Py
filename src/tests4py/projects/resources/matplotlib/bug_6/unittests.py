import unittest
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(3), range(3), c=[[0.211, 0.539, 0.367]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(3), range(3), c=[[0.178, 0.812, 0.077]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(3), range(3), c=[[0.215, 0.763, 0.728]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(4), range(4), c=[[0.392, 0.428, 0.255, 0.054]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(4), range(4), c=[[0.062, 0.632, 0.654, 0.309]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(3), range(3), c=[[0.888, 0.444, 0.17]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(3), range(3), c=[[0.48, 0.713, 0.839]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(4), range(4), c=[[0.131, 0.221, 0.803, 0.204]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(4), range(4), c=[[0.202, 0.785, 0.79, 0.613]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(4), range(4), c=[[0.347, 0.276, 0.327, 0.556]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(8), range(8), c=[[0.342, 0.313, 0.452]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(6), range(6), c=[[0.542, 0.665, 0.535, 0.698]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(8), range(8), c=[[0.438, 0.652, 0.542]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(6), range(6), c=[[0.548, 0.487, 0.108, 0.4]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(6), range(6), c=[[0.912, 0.623, 0.327, 0.935]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(6), range(6), c=[[0.504, 0.417, 0.696, 0.377]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(4), range(4), c=[[0.318, 0.321, 0.228]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(2), range(2), c=[[0.47, 0.921, 0.571]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(4), range(4), c=[[0.633, 0.149, 0.177]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        coll = ax.scatter(np.ones(8), range(8), c=[[0.188, 0.927, 0.612]])
        self.assertEqual(True, coll.get_array() is None)
        plt.close(fig)
