import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='2', s=100, linewidths=5.2)
        self.assertEqual(5.2, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='1', s=100, linewidths=5.6)
        self.assertEqual(5.6, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='1', s=100, linewidths=6.2)
        self.assertEqual(6.2, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='x', s=100, linewidths=4.6)
        self.assertEqual(4.6, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='2', s=100, linewidths=4.0)
        self.assertEqual(4.0, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='1', s=100, linewidths=7.7)
        self.assertEqual(7.7, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='+', s=100, linewidths=6.3)
        self.assertEqual(6.3, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='2', s=100, linewidths=5.8)
        self.assertEqual(5.8, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='4', s=100, linewidths=6.4)
        self.assertEqual(6.4, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='+', s=100, linewidths=2.2)
        self.assertEqual(2.2, float(pc.get_linewidths()[0]))
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='o', s=100, linewidths=5.2)
        self.assertEqual(5.2, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='o', s=100, linewidths=3.5)
        self.assertEqual(3.5, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='D', s=100, linewidths=2.5)
        self.assertEqual(2.5, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='D', s=100, linewidths=5.3)
        self.assertEqual(5.3, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='s', s=100, linewidths=8.7)
        self.assertEqual(8.7, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='s', s=100, linewidths=3.6)
        self.assertEqual(3.6, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='^', s=100, linewidths=6.5)
        self.assertEqual(6.5, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='p', s=100, linewidths=5.2)
        self.assertEqual(5.2, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='D', s=100, linewidths=7.0)
        self.assertEqual(7.0, float(pc.get_linewidths()[0]))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        pc = ax.scatter(range(5), [0] * 5, c='C0', marker='v', s=100, linewidths=2.2)
        self.assertEqual(2.2, float(pc.get_linewidths()[0]))
        plt.close(fig)
