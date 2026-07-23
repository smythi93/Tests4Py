import unittest
import hashlib
import warnings
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.533], c='none')
            ax.margins(0)
            ax.set_rorigin(3.816)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_2(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.672], c='none')
            ax.margins(0)
            ax.set_rorigin(5.041)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_3(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.542], c='none')
            ax.margins(0)
            ax.set_rorigin(3.068)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_4(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.637], c='none')
            ax.margins(0)
            ax.set_rorigin(5.228)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_5(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.845], c='none')
            ax.margins(0)
            ax.set_rorigin(4.408)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_6(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 1.946], c='none')
            ax.margins(0)
            ax.set_rorigin(2.919)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_7(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.586], c='none')
            ax.margins(0)
            ax.set_rorigin(5.216)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_8(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 1.653], c='none')
            ax.margins(0)
            ax.set_rorigin(3.465)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_9(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.054], c='none')
            ax.margins(0)
            ax.set_rorigin(2.91)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_10(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            ax.yaxis.set_inverted(True)
            ax.plot([0, 0], [0, 2.867], c='none')
            ax.margins(0)
            ax.set_rorigin(4.725)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 2.841 * 0.8)
            ax.set_rlim(0, 2.841)
            ax.set_rorigin(-0.959)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_2(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 3.718 * 0.8)
            ax.set_rlim(0, 3.718)
            ax.set_rorigin(-1.101)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_3(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 3.77 * 0.8)
            ax.set_rlim(0, 3.77)
            ax.set_rorigin(-2.65)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_4(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 3.431 * 0.8)
            ax.set_rlim(0, 3.431)
            ax.set_rorigin(-1.992)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_5(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 2.649 * 0.8)
            ax.set_rlim(0, 2.649)
            ax.set_rorigin(-1.474)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_6(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 3.887 * 0.8)
            ax.set_rlim(0, 3.887)
            ax.set_rorigin(-2.436)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_7(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 2.456 * 0.8)
            ax.set_rlim(0, 2.456)
            ax.set_rorigin(-2.199)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_8(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 3.894 * 0.8)
            ax.set_rlim(0, 3.894)
            ax.set_rorigin(-2.837)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_9(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 3.064 * 0.8)
            ax.set_rlim(0, 3.064)
            ax.set_rorigin(-2.849)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))

    def test_diversity_10(self):

        def _render(unstale):
            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
            theta = np.linspace(0, 2 * np.pi, 50)
            ax.plot(theta, np.ones(50) * 2.114 * 0.8)
            ax.set_rlim(0, 2.114)
            ax.set_rorigin(-2.862)
            if unstale:
                ax._unstale_viewLim()
            fig.canvas.draw()
            buf = np.asarray(fig.canvas.buffer_rgba()).copy()
            plt.close(fig)
            return hashlib.md5(buf.tobytes()).hexdigest()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            self.assertEqual(True, _render(False) == _render(True))
