import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        plt.figure(figsize=(6.18, 6.42))
        plt.polar()
        ax = plt.gca()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_2(self):
        plt.figure(figsize=(5.25, 6.43))
        plt.polar()
        ax = plt.gca()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_3(self):
        fig = plt.figure(figsize=(7.06, 5.91))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_4(self):
        plt.figure(figsize=(4.06, 7.46))
        plt.polar()
        ax = plt.gca()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_5(self):
        fig = plt.figure(figsize=(4.63, 5.06))
        ax = fig.add_subplot(projection='polar')
        ax.autoscale()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_6(self):
        fig = plt.figure(figsize=(7.83, 5.58))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_7(self):
        fig = plt.figure(figsize=(3.49, 3.34))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_8(self):
        fig = plt.figure(figsize=(4.19, 6.31))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_9(self):
        fig = plt.figure(figsize=(6.79, 7.42))
        ax = fig.add_subplot(projection='polar')
        ax.autoscale()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_10(self):
        plt.figure(figsize=(3.48, 4.44))
        plt.polar()
        ax = plt.gca()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure(figsize=(4.9, 5.51))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_2(self):
        fig = plt.figure(figsize=(5.22, 7.3))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_3(self):
        fig = plt.figure(figsize=(7.27, 4.22))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_4(self):
        fig = plt.figure(figsize=(4.9, 4.31))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_5(self):
        fig = plt.figure(figsize=(4.3, 7.63))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_6(self):
        fig = plt.figure(figsize=(6.6, 6.51))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_7(self):
        fig = plt.figure(figsize=(3.42, 5.75))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_8(self):
        fig = plt.figure(figsize=(5.65, 5.38))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_9(self):
        fig = plt.figure(figsize=(5.72, 5.26))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_10(self):
        fig = plt.figure(figsize=(7.5, 4.22))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')
