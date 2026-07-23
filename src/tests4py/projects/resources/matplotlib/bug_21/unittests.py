import unittest
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 'p'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['caps'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_2(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 's'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['medians'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_3(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 'v'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['medians'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_4(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = '*'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['whiskers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_5(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 'h'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['medians'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_6(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 'o'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['boxes'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_7(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 'o'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['whiskers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_8(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 'v'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['boxes'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_9(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = 'o'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['caps'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_10(self):
        plt.rcdefaults()
        plt.rcParams['lines.marker'] = '+'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('', bxp['medians'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.flierprops.marker'] = 'x'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('x', bxp['fliers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_2(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.flierprops.marker'] = 'D'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('D', bxp['fliers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_3(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.meanprops.marker'] = 'h'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('h', bxp['means'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_4(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.flierprops.marker'] = 'v'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('v', bxp['fliers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_5(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.flierprops.marker'] = '*'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('*', bxp['fliers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_6(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.meanprops.marker'] = '^'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('^', bxp['means'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_7(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.flierprops.marker'] = 's'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('s', bxp['fliers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_8(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.meanprops.marker'] = 'x'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('x', bxp['means'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_9(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.meanprops.marker'] = '*'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('*', bxp['means'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()

    def test_diversity_10(self):
        plt.rcdefaults()
        plt.rcParams['boxplot.flierprops.marker'] = 'o'
        fig, ax = plt.subplots()
        d = np.arange(100)
        d[-1] = 150
        bxp = ax.boxplot(d, showmeans=True)
        self.assertEqual('o', bxp['fliers'][0].get_marker())
        plt.close(fig)
        plt.rcdefaults()
