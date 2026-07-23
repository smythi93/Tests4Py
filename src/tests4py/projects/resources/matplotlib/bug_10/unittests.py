import unittest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 15 for i in range(3)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_2(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 8 for i in range(3)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_3(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 10 for i in range(3)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_4(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 10 for i in range(4)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_5(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 13 for i in range(5)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_6(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 11 for i in range(5)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_7(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 14 for i in range(3)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_8(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 10 for i in range(6)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_9(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 7 for i in range(4)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_10(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 9 for i in range(4)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=False, label2On=False)
        self.assertEqual(False, axis.get_offset_text().get_visible())
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 8 for i in range(4)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=True, label2On=False)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_2(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 12 for i in range(5)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=True, label2On=True)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_3(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 13 for i in range(4)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=True, label2On=True)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_4(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 14 for i in range(6)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=True, label2On=True)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_5(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 13 for i in range(6)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=True, label2On=False)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_6(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 8 for i in range(5)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=True, label2On=False)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_7(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 13 for i in range(3)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=True, label2On=False)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_8(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 13 for i in range(5)]
        ax.plot(data)
        axis = ax.yaxis
        axis.set_tick_params(label1On=True, label2On=False)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_9(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 11 for i in range(6)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=True, label2On=False)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)

    def test_diversity_10(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        data = [(1.01 + 0.01 * i) * 10 ** 15 for i in range(5)]
        ax.plot(data, [0] * len(data))
        axis = ax.xaxis
        axis.set_tick_params(label1On=False, label2On=True)
        self.assertEqual(True, axis.get_offset_text().get_visible())
        plt.close(fig)
