import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([-4.69, float('nan'), 9.94, -1.1, float('nan')], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([-0.65, float('nan'), -9.6, 4.09], 0, 1)
        self.assertEqual(4, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([0.18, -5.73, 5.94, 2.26, float('nan')], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([-5.25, -1.88, float('nan'), -2.71, 4.22], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([float('nan'), 0.9, 8.67, float('nan')], 0, 1)
        self.assertEqual(4, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([float('nan'), float('nan'), 8.74, -4.12, 3.48], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([-1.68, float('nan'), 3.82, -2.7, 8.12], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([-5.13, -0.95, 4.61, float('nan')], 0, 1)
        self.assertEqual(4, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([8.75, float('nan'), 7.88, -5.99, -8.38, 3.28], 0, 1)
        self.assertEqual(6, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([float('nan'), float('nan'), 0.6, 3.25], 0, 1)
        self.assertEqual(4, len(coll.get_segments()))
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([-6.71, 0.85], 0, 1)
        self.assertEqual(2, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([7.02, -9.83, -2.93, -3.2], 0, 1)
        self.assertEqual(4, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([0.89, -9.07, -9.48], 0, 1)
        self.assertEqual(3, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([-3.89, -1.94, -5.97], 0, 1)
        self.assertEqual(3, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([7.85, -4.95, 8.15, -4.75, 5.58, 1.81, 5.49], 0, 1)
        self.assertEqual(7, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([5.01, -7.62, -3.02, -4.48, 9.54], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([4.46, 4.81, 2.56, -7.39, 2.48], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([1.19, -9.59, 3.0, -7.2, -6.75, 4.68], 0, 1)
        self.assertEqual(6, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        coll = ax.vlines([-6.36, -0.79, 5.7, 1.17, -1.02], 0, 1)
        self.assertEqual(5, len(coll.get_segments()))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        coll = ax.hlines([5.78, -4.18, -8.86, -7.6, 7.18, -9.55], 0, 1)
        self.assertEqual(6, len(coll.get_segments()))
        plt.close(fig)
