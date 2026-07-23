import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib as mpl
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'orange'}):
            lines = ax.hlines(2.49, -0.02, 4.36)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'orange'))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'cyan'}):
            lines = ax.vlines(0.86, -4.69, 0.03)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'cyan'))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'brown'}):
            lines = ax.hlines(-3.43, -1.85, 1.67)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'brown'))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'cyan'}):
            lines = ax.hlines(-1.45, -1.97, 2.88)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'cyan'))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'brown'}):
            lines = ax.hlines(-2.42, -0.13, 2.22)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'brown'))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'red'}):
            lines = ax.vlines(4.08, -0.48, 3.19)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'red'))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'blue'}):
            lines = ax.vlines(-1.59, -4.54, -1.22)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'blue'))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'purple'}):
            lines = ax.hlines(0.22, -0.93, 0.15)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'purple'))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'brown'}):
            lines = ax.hlines(1.54, -2.34, 1.13)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'brown'))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'magenta'}):
            lines = ax.hlines(1.16, -3.81, -0.76)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'magenta'))
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'k'}):
            lines = ax.hlines(0.1, -1.09, 3.28)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'k'))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': '#000000'}):
            lines = ax.hlines(-2.88, -1.72, 0.43)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), '#000000'))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'black'}):
            lines = ax.vlines(-0.94, -4.85, -1.93)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'black'))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'black'}):
            lines = ax.vlines(3.39, -0.37, 0.7)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'black'))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': '#000000'}):
            lines = ax.hlines(-1.15, -1.61, 3.09)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), '#000000'))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': '#000000'}):
            lines = ax.hlines(4.0, -2.38, 2.07)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), '#000000'))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'black'}):
            lines = ax.hlines(4.96, -0.52, 3.91)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'black'))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'black'}):
            lines = ax.hlines(-1.32, -3.92, 2.05)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'black'))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'black'}):
            lines = ax.vlines(4.61, -1.82, 2.97)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'black'))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        with mpl.rc_context({'lines.color': 'k'}):
            lines = ax.vlines(2.45, -3.91, -0.05)
            self.assertEqual(True, mpl.colors.same_color(lines.get_color(), 'k'))
        plt.close(fig)
