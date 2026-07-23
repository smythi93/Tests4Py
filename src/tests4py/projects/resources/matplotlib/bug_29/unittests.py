import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-3.87, 13.32], [-3.87, 13.32])
        ax0.yaxis.set_inverted(True)
        self.assertEqual(True, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_2(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([-7.59, 1.0], [-7.59, 1.0])
        ax0.xaxis.set_inverted(True)
        self.assertEqual(True, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_3(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([-10.4, -4.13], [-10.4, -4.13])
        ax0.xaxis.set_inverted(True)
        self.assertEqual(True, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_4(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([-0.27, 17.4], [-0.27, 17.4])
        ax0.xaxis.set_inverted(True)
        self.assertEqual(True, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_5(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-6.6, -1.68], [-6.6, -1.68])
        ax0.yaxis.set_inverted(True)
        self.assertEqual(True, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_6(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([9.08, 18.14], [9.08, 18.14])
        ax0.yaxis.set_inverted(True)
        self.assertEqual(True, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_7(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([6.54, 12.54], [6.54, 12.54])
        ax0.yaxis.set_inverted(True)
        self.assertEqual(True, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_8(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-17.1, -11.86], [-17.1, -11.86])
        ax0.yaxis.set_inverted(True)
        self.assertEqual(True, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_9(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([3.7, 13.26], [3.7, 13.26])
        ax0.yaxis.set_inverted(True)
        self.assertEqual(True, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_10(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-2.0, 4.64], [-2.0, 4.64])
        ax0.yaxis.set_inverted(True)
        self.assertEqual(True, ax1.yaxis_inverted())
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-11.87, 4.82], [-11.87, 4.82])
        ax0.yaxis.set_inverted(False)
        self.assertEqual(False, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_2(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([6.8, 12.28], [6.8, 12.28])
        ax0.xaxis.set_inverted(False)
        self.assertEqual(False, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_3(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([9.87, 23.37], [9.87, 23.37])
        ax0.xaxis.set_inverted(False)
        self.assertEqual(False, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_4(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([-14.76, -7.6], [-14.76, -7.6])
        ax0.xaxis.set_inverted(False)
        self.assertEqual(False, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_5(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([3.9, 13.17], [3.9, 13.17])
        ax0.xaxis.set_inverted(False)
        self.assertEqual(False, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_6(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-1.93, 3.1], [-1.93, 3.1])
        ax0.yaxis.set_inverted(False)
        self.assertEqual(False, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_7(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-2.96, -1.18], [-2.96, -1.18])
        ax0.yaxis.set_inverted(False)
        self.assertEqual(False, ax1.yaxis_inverted())
        plt.close(fig)

    def test_diversity_8(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([-1.62, 6.02], [-1.62, 6.02])
        ax0.xaxis.set_inverted(False)
        self.assertEqual(False, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_9(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharex=ax0)
        ax0.plot([6.37, 8.87], [6.37, 8.87])
        ax0.xaxis.set_inverted(False)
        self.assertEqual(False, ax1.xaxis_inverted())
        plt.close(fig)

    def test_diversity_10(self):
        fig = plt.figure()
        ax0 = plt.subplot(211)
        ax1 = plt.subplot(212, sharey=ax0)
        ax0.plot([-13.72, -9.61], [-13.72, -9.61])
        ax0.yaxis.set_inverted(False)
        self.assertEqual(False, ax1.yaxis_inverted())
        plt.close(fig)
