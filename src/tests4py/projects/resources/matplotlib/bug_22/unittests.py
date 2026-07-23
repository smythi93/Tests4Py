import unittest
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib as mpl
import matplotlib.pyplot as plt

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-02-01', '%Y-%m-%d'), datetime.datetime.strptime('2019-02-17', '%Y-%m-%d'), datetime.datetime.strptime('2019-12-17', '%Y-%m-%d')], stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-01-07', '%Y-%m-%d'), datetime.datetime.strptime('2019-01-10', '%Y-%m-%d'), datetime.datetime.strptime('2019-01-20', '%Y-%m-%d')], stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-04-18', '%Y-%m-%d'), datetime.datetime.strptime('2019-05-17', '%Y-%m-%d'), datetime.datetime.strptime('2019-05-28', '%Y-%m-%d')], stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-07-29', '%Y-%m-%d'), datetime.datetime.strptime('2019-12-01', '%Y-%m-%d')], stacked=True)
        self.assertEqual(2, len(bins))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-01-06', '%Y-%m-%d'), datetime.datetime.strptime('2019-09-02', '%Y-%m-%d')], stacked=True)
        self.assertEqual(2, len(bins))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-05-21', '%Y-%m-%d'), datetime.datetime.strptime('2019-06-02', '%Y-%m-%d')], stacked=True)
        self.assertEqual(2, len(bins))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-04-10', '%Y-%m-%d'), datetime.datetime.strptime('2019-05-18', '%Y-%m-%d'), datetime.datetime.strptime('2019-09-23', '%Y-%m-%d')], stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-04-04', '%Y-%m-%d'), datetime.datetime.strptime('2019-06-18', '%Y-%m-%d'), datetime.datetime.strptime('2019-12-18', '%Y-%m-%d')], stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-01-13', '%Y-%m-%d'), datetime.datetime.strptime('2019-01-19', '%Y-%m-%d'), datetime.datetime.strptime('2019-07-22', '%Y-%m-%d'), datetime.datetime.strptime('2019-10-05', '%Y-%m-%d')], stacked=True)
        self.assertEqual(4, len(bins))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=[datetime.datetime.strptime('2019-03-11', '%Y-%m-%d'), datetime.datetime.strptime('2019-08-25', '%Y-%m-%d'), datetime.datetime.strptime('2019-09-27', '%Y-%m-%d')], stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-01-24', '%Y-%m-%d'), datetime.datetime.strptime('2019-02-19', '%Y-%m-%d'), datetime.datetime.strptime('2019-04-27', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

    def test_diversity_2(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-02-26', '%Y-%m-%d'), datetime.datetime.strptime('2019-05-31', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(2, len(bins))
        plt.close(fig)

    def test_diversity_3(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-04-04', '%Y-%m-%d'), datetime.datetime.strptime('2019-05-29', '%Y-%m-%d'), datetime.datetime.strptime('2019-09-03', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(3, len(bins))
        plt.close(fig)

    def test_diversity_4(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-03-04', '%Y-%m-%d'), datetime.datetime.strptime('2019-07-04', '%Y-%m-%d'), datetime.datetime.strptime('2019-09-11', '%Y-%m-%d'), datetime.datetime.strptime('2019-09-29', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(4, len(bins))
        plt.close(fig)

    def test_diversity_5(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-05-21', '%Y-%m-%d'), datetime.datetime.strptime('2019-09-17', '%Y-%m-%d'), datetime.datetime.strptime('2019-10-24', '%Y-%m-%d'), datetime.datetime.strptime('2019-12-08', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(4, len(bins))
        plt.close(fig)

    def test_diversity_6(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-01-16', '%Y-%m-%d'), datetime.datetime.strptime('2019-02-25', '%Y-%m-%d'), datetime.datetime.strptime('2019-05-08', '%Y-%m-%d'), datetime.datetime.strptime('2019-10-18', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(4, len(bins))
        plt.close(fig)

    def test_diversity_7(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-06-06', '%Y-%m-%d'), datetime.datetime.strptime('2019-11-29', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(2, len(bins))
        plt.close(fig)

    def test_diversity_8(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-03-25', '%Y-%m-%d'), datetime.datetime.strptime('2019-04-30', '%Y-%m-%d'), datetime.datetime.strptime('2019-08-05', '%Y-%m-%d'), datetime.datetime.strptime('2019-12-01', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(4, len(bins))
        plt.close(fig)

    def test_diversity_9(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-08-19', '%Y-%m-%d'), datetime.datetime.strptime('2019-11-19', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(2, len(bins))
        plt.close(fig)

    def test_diversity_10(self):
        fig, ax = plt.subplots()
        data = [[datetime.datetime(2019, 1, 5), datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 1), datetime.datetime(2019, 3, 1)], [datetime.datetime(2019, 1, 11), datetime.datetime(2019, 2, 5), datetime.datetime(2019, 2, 18), datetime.datetime(2019, 3, 1)]]
        _, bins, _ = ax.hist(data, bins=mpl.dates.date2num([datetime.datetime.strptime('2019-09-20', '%Y-%m-%d'), datetime.datetime.strptime('2019-10-20', '%Y-%m-%d')]), stacked=True)
        self.assertEqual(2, len(bins))
        plt.close(fig)
