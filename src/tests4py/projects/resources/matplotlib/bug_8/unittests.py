import unittest
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-0.842, 0.581), auto=True)
        fig.canvas.draw()
        self.assertEqual([-0.842, 0.581], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-1.3, 0.338), auto=True)
        fig.canvas.draw()
        self.assertEqual([-1.3, 0.338], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-1.349, 0.649), auto=None)
        fig.canvas.draw()
        self.assertEqual([-1.349, 0.649], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-0.753, 1.546), auto=True)
        fig.canvas.draw()
        self.assertEqual([-0.753, 1.546], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-0.803, 1.976), auto=None)
        fig.canvas.draw()
        self.assertEqual([-0.803, 1.976], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-0.757, 0.711), auto=True)
        fig.canvas.draw()
        self.assertEqual([-0.757, 0.711], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-0.616, 0.98), auto=None)
        fig.canvas.draw()
        self.assertEqual([-0.616, 0.98], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-0.948, 0.584), auto=True)
        fig.canvas.draw()
        self.assertEqual([-0.948, 0.584], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-1.658, 0.701), auto=None)
        fig.canvas.draw()
        self.assertEqual([-1.658, 0.701], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-0.52, 0.66), auto=True)
        fig.canvas.draw()
        self.assertEqual([-0.52, 0.66], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-1.113, 1.474), auto=False)
        fig.canvas.draw()
        self.assertEqual([-1.113, 1.474], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-0.771, 1.313), auto=False)
        fig.canvas.draw()
        self.assertEqual([-0.771, 1.313], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-0.403, 1.672), auto=False)
        fig.canvas.draw()
        self.assertEqual([-0.403, 1.672], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-1.91, 1.067), auto=False)
        fig.canvas.draw()
        self.assertEqual([-1.91, 1.067], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-1.512, 0.495), auto=False)
        fig.canvas.draw()
        self.assertEqual([-1.512, 0.495], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-1.692, 0.767), auto=False)
        fig.canvas.draw()
        self.assertEqual([-1.692, 0.767], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        ax.scatter(np.arange(100), np.linspace(-0.1, 0.1, 100))
        ax.set_ylim((-0.966, 1.312), auto=False)
        fig.canvas.draw()
        self.assertEqual([-0.966, 1.312], [round(float(v), 3) for v in ax.get_ylim()])
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-1.58, 1.637), auto=False)
        fig.canvas.draw()
        self.assertEqual([-1.58, 1.637], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-1.923, 0.996), auto=False)
        fig.canvas.draw()
        self.assertEqual([-1.923, 0.996], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        ax.scatter(np.linspace(-0.1, 0.1, 100), np.arange(100))
        ax.set_xlim((-0.952, 1.723), auto=False)
        fig.canvas.draw()
        self.assertEqual([-0.952, 1.723], [round(float(v), 3) for v in ax.get_xlim()])
        plt.close(fig)
