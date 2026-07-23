import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.534, 237.412), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.534) < 1e-06 and abs(cur[1] - 237.412) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_2(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.924, 553.475), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.924) < 1e-06 and abs(cur[1] - 553.475) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_3(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(0.834, 207.554), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 0.834) < 1e-06 and abs(cur[1] - 207.554) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_4(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.286, 311.674), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.286) < 1e-06 and abs(cur[1] - 311.674) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_5(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.671, 362.344), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.671) < 1e-06 and abs(cur[1] - 362.344) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_6(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.742, 596.583), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.742) < 1e-06 and abs(cur[1] - 596.583) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_7(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.954, 357.616), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.954) < 1e-06 and abs(cur[1] - 357.616) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_8(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.149, 342.264), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.149) < 1e-06 and abs(cur[1] - 342.264) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_9(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.05, 337.193), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.05) < 1e-06 and abs(cur[1] - 337.193) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

    def test_diversity_10(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(0.594, 122.55), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='datalim')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 0.594) < 1e-06 and abs(cur[1] - 122.55) < 1e-06
        self.assertEqual(False, unchanged)
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.181, 467.585), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.181) < 1e-06 and abs(cur[1] - 467.585) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_2(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.159, 259.334), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.159) < 1e-06 and abs(cur[1] - 259.334) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_3(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.017, 357.842), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.017) < 1e-06 and abs(cur[1] - 357.842) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_4(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(0.559, 141.378), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 0.559) < 1e-06 and abs(cur[1] - 141.378) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_5(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(0.57, 95.925), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 0.57) < 1e-06 and abs(cur[1] - 95.925) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_6(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(0.669, 210.777), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 0.669) < 1e-06 and abs(cur[1] - 210.777) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_7(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.428, 243.568), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.428) < 1e-06 and abs(cur[1] - 243.568) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_8(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.464, 436.423), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.464) < 1e-06 and abs(cur[1] - 436.423) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_9(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.683, 427.067), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.683) < 1e-06 and abs(cur[1] - 427.067) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)

    def test_diversity_10(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.plot([0.4, 0.6], [0.4, 0.6])
        ax.set(xscale='log', xlim=(1.471, 425.274), yscale='logit', ylim=(1 / 101, 1 / 11), aspect=1, adjustable='box')
        ax.margins(0)
        ax.apply_aspect()
        cur = ax.get_xlim()
        unchanged = abs(cur[0] - 1.471) < 1e-06 and abs(cur[1] - 425.274) < 1e-06
        self.assertEqual(True, unchanged)
        plt.close(fig)
