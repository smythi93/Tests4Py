import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=17.9, fontproperties='serif')
        self.assertEqual(17.9, t.get_size())
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=47.5, fontproperties='fantasy')
        self.assertEqual(47.5, t.get_size())
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=53.9, fontproperties='fantasy')
        self.assertEqual(53.9, t.get_size())
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=20.5, fontproperties='monospace')
        self.assertEqual(20.5, t.get_size())
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=51.8, fontproperties='serif')
        self.assertEqual(51.8, t.get_size())
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=41.7, fontproperties='fantasy')
        self.assertEqual(41.7, t.get_size())
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=50.9, fontproperties='monospace')
        self.assertEqual(50.9, t.get_size())
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=43.3, fontproperties='serif')
        self.assertEqual(43.3, t.get_size())
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=56.0, fontproperties='cursive')
        self.assertEqual(56.0, t.get_size())
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', size=58.8, fontproperties='fantasy')
        self.assertEqual(58.8, t.get_size())
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='cursive', size=41.6)
        self.assertEqual(41.6, t.get_size())
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='monospace', size=17.7)
        self.assertEqual(17.7, t.get_size())
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='fantasy', size=19.2)
        self.assertEqual(19.2, t.get_size())
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='cursive', size=16.5)
        self.assertEqual(16.5, t.get_size())
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='cursive', size=15.4)
        self.assertEqual(15.4, t.get_size())
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='serif', size=52.9)
        self.assertEqual(52.9, t.get_size())
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='cursive', size=22.8)
        self.assertEqual(22.8, t.get_size())
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='serif', size=44.3)
        self.assertEqual(44.3, t.get_size())
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='fantasy', size=48.7)
        self.assertEqual(48.7, t.get_size())
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        t = ax.set_xlabel('value', fontproperties='cursive', size=24.1)
        self.assertEqual(24.1, t.get_size())
        plt.close(fig)
