import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        grays = [round((i + 1) / (9 + 1), 3) for i in range(9)]
        coll = plt.scatter(range(9), range(9), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 9)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_2(self):
        grays = [round((i + 1) / (14 + 1), 3) for i in range(14)]
        coll = plt.scatter(range(14), range(14), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 14)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_3(self):
        grays = [round((i + 1) / (12 + 1), 3) for i in range(12)]
        coll = plt.scatter(range(12), range(12), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 12)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_4(self):
        grays = [round((i + 1) / (16 + 1), 3) for i in range(16)]
        coll = plt.scatter(range(16), range(16), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 16)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_5(self):
        grays = [round((i + 1) / (6 + 1), 3) for i in range(6)]
        coll = plt.scatter(range(6), range(6), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 6)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_6(self):
        grays = [round((i + 1) / (3 + 1), 3) for i in range(3)]
        coll = plt.scatter(range(3), range(3), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 3)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_7(self):
        grays = [round((i + 1) / (15 + 1), 3) for i in range(15)]
        coll = plt.scatter(range(15), range(15), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 15)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_8(self):
        grays = [round((i + 1) / (10 + 1), 3) for i in range(10)]
        coll = plt.scatter(range(10), range(10), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 10)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_9(self):
        grays = [round((i + 1) / (11 + 1), 3) for i in range(11)]
        coll = plt.scatter(range(11), range(11), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 11)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_10(self):
        grays = [round((i + 1) / (13 + 1), 3) for i in range(13)]
        coll = plt.scatter(range(13), range(13), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='none'), linewidths=[1.0] * 13)
        self.assertEqual(0, coll.get_facecolors().shape[0])
        plt.close('all')

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        grays = [round((i + 1) / (9 + 1), 3) for i in range(9)]
        coll = plt.scatter(range(9), range(9), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 9)
        self.assertEqual(9, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_2(self):
        grays = [round((i + 1) / (11 + 1), 3) for i in range(11)]
        coll = plt.scatter(range(11), range(11), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 11)
        self.assertEqual(11, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_3(self):
        grays = [round((i + 1) / (6 + 1), 3) for i in range(6)]
        coll = plt.scatter(range(6), range(6), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 6)
        self.assertEqual(6, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_4(self):
        grays = [round((i + 1) / (13 + 1), 3) for i in range(13)]
        coll = plt.scatter(range(13), range(13), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 13)
        self.assertEqual(13, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_5(self):
        grays = [round((i + 1) / (14 + 1), 3) for i in range(14)]
        coll = plt.scatter(range(14), range(14), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 14)
        self.assertEqual(14, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_6(self):
        grays = [round((i + 1) / (3 + 1), 3) for i in range(3)]
        coll = plt.scatter(range(3), range(3), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 3)
        self.assertEqual(3, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_7(self):
        grays = [round((i + 1) / (8 + 1), 3) for i in range(8)]
        coll = plt.scatter(range(8), range(8), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 8)
        self.assertEqual(8, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_8(self):
        grays = [round((i + 1) / (12 + 1), 3) for i in range(12)]
        coll = plt.scatter(range(12), range(12), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 12)
        self.assertEqual(12, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_9(self):
        grays = [round((i + 1) / (7 + 1), 3) for i in range(7)]
        coll = plt.scatter(range(7), range(7), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 7)
        self.assertEqual(7, coll.get_facecolors().shape[0])
        plt.close('all')

    def test_diversity_10(self):
        grays = [round((i + 1) / (4 + 1), 3) for i in range(4)]
        coll = plt.scatter(range(4), range(4), c=[str(g) for g in grays], marker=MarkerStyle('o', fillstyle='full'), linewidths=[1.0] * 4)
        self.assertEqual(4, coll.get_facecolors().shape[0])
        plt.close('all')
