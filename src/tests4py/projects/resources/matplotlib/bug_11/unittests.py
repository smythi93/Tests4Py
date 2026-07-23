import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 5.087)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 3.36)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 6.857)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 6.43)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 5.019)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 5.415)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 5.356)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 6.471)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 9.648)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, '', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 3.023)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'ucteigxb', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 11.782)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'srnkqrz', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 7.152)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'kxko', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 4.161)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'qfyopz', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 8.493)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'vkfn', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 3.657)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'sjkdd', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 4.447)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'ssqkbc', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 8.202)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'kjeupans', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 10.007)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'xbwsfw', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 3.18)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        t1 = ax.text(0.5, 0.5, 'qlettkiz', ha='left', va='bottom')
        fig.canvas.draw()
        dpi = fig.dpi
        t1.get_window_extent()
        t1.get_window_extent(dpi=dpi * 4.508)
        self.assertEqual(True, fig.dpi == dpi)
        plt.close(fig)
