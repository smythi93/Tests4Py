import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='horizontal', label='yibwv')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_xlabel())
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='qdzkqya')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='aoyd')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='qryfd')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='bjn')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='rcajnxs')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='horizontal', label='ytw')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_xlabel())
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='horizontal', label='hxqlw')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_xlabel())
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='horizontal', label='wqvle')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_xlabel())
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='tchmy')
        cbar.set_label(None)
        self.assertEqual('', cbar.ax.get_ylabel())
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='psts')
        cbar.set_label('nahlgyvq')
        self.assertEqual('nahlgyvq', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='noxsnyy')
        cbar.set_label('zpdncct')
        self.assertEqual('zpdncct', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='gzad')
        cbar.set_label('ekv')
        self.assertEqual('ekv', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='horizontal', label='sryp')
        cbar.set_label('zygn')
        self.assertEqual('zygn', cbar.ax.get_xlabel())
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='hjg')
        cbar.set_label('wfemcms')
        self.assertEqual('wfemcms', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='ytwxjg')
        cbar.set_label('bjxxodxd')
        self.assertEqual('bjxxodxd', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='hmgmysg')
        cbar.set_label('rnvytk')
        self.assertEqual('rnvytk', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='horizontal', label='girkyb')
        cbar.set_label('avwirbnl')
        self.assertEqual('avwirbnl', cbar.ax.get_xlabel())
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='onz')
        cbar.set_label('icgq')
        self.assertEqual('icgq', cbar.ax.get_ylabel())
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        im = ax.imshow([[1, 2], [3, 4]])
        cbar = fig.colorbar(im, orientation='vertical', label='gyql')
        cbar.set_label('jot')
        self.assertEqual('jot', cbar.ax.get_ylabel())
        plt.close(fig)
