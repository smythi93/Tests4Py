import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((222.8, 210.6)) is None)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((453.6, 123.4)) is None)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((237.7, 107.9)) is None)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((262.8, 181.6)) is None)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((151.0, 108.3)) is None)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((548.7, 259.6)) is None)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((174.8, 181.7)) is None)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((381.8, 375.0)) is None)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((442.7, 339.6)) is None)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        ax.set_visible(False)
        self.assertEqual(True, fig.canvas.inaxes((330.8, 334.0)) is None)
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((338.8, 292.6)) is None)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((311.4, 367.7)) is None)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((333.0, 77.8)) is None)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((328.2, 400.0)) is None)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((483.7, 375.1)) is None)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((267.9, 219.7)) is None)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((167.5, 235.3)) is None)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((286.6, 273.7)) is None)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((202.8, 321.0)) is None)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        self.assertEqual(False, fig.canvas.inaxes((511.2, 155.3)) is None)
        plt.close(fig)
