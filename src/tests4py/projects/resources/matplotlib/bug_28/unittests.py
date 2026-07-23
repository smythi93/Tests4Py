import unittest
import warnings
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-8.2, 6.26)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-0.41, 11.74)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-9.8, 11.09)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-2.84, 21.05)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-7.36, 31.1)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-5.24, 91.86)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-9.25, 25.27)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-5.59, 13.6)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-6.94, 35.77)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(-2.78, 43.79)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(4.76, 42.27)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(0.42, 45.15)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(0.67, 49.32)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(4.41, 45.49)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(0.81, 29.49)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(2.29, 36.93)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(4.76, 38.06)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(4.75, 6.96)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(0.79, 18.61)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        ax.set_xscale('log')
        ok = 'FAIL'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ax.set_xlim(4.51, 20.88)
            ok = 'OK'
        self.assertEqual('OK', ok)
        plt.close(fig)
