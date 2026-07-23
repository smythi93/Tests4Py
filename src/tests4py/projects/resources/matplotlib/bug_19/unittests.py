import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure(figsize=(7.33, 7.92))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_2(self):
        fig = plt.figure(figsize=(4.47, 5.21))
        ax = fig.add_subplot(projection='polar')
        ax.autoscale()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_3(self):
        plt.figure(figsize=(5.39, 7.71))
        plt.polar()
        ax = plt.gca()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_4(self):
        plt.figure(figsize=(5.24, 5.34))
        plt.polar()
        ax = plt.gca()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_5(self):
        fig = plt.figure(figsize=(7.9, 4.25))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_6(self):
        plt.figure(figsize=(3.11, 7.94))
        plt.polar()
        ax = plt.gca()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_7(self):
        fig = plt.figure(figsize=(6.0, 4.3))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_8(self):
        fig = plt.figure(figsize=(5.04, 4.71))
        ax = fig.add_subplot(projection='polar')
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_9(self):
        fig = plt.figure(figsize=(3.97, 5.94))
        ax = fig.add_subplot(projection='polar')
        ax.autoscale()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_10(self):
        fig = plt.figure(figsize=(5.47, 7.86))
        ax = fig.add_subplot(projection='polar')
        ax.autoscale()
        fig.canvas.draw()
        self.assertEqual([0.0, 1.05], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure(figsize=(7.71, 3.44))
        ax = fig.add_subplot(projection='polar')
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_2(self):
        fig = plt.figure(figsize=(6.73, 4.43))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_3(self):
        fig = plt.figure(figsize=(6.39, 3.78))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_4(self):
        fig = plt.figure(figsize=(7.75, 7.93))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_5(self):
        fig = plt.figure(figsize=(7.93, 7.26))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_6(self):
        fig = plt.figure(figsize=(3.46, 3.06))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_7(self):
        fig = plt.figure(figsize=(3.33, 3.78))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_8(self):
        fig = plt.figure(figsize=(7.49, 7.44))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_9(self):
        fig = plt.figure(figsize=(7.7, 5.63))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')

    def test_diversity_10(self):
        fig = plt.figure(figsize=(6.81, 5.83))
        ax = fig.add_subplot(projection='polar')
        fig.canvas.draw()
        self.assertEqual([0.0, 1.0], [round(float(ax.get_rmin()), 4), round(float(ax.get_rmax()), 4)])
        plt.close('all')
