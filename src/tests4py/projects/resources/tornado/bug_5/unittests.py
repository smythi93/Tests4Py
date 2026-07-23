import unittest
import math
from tornado.ioloop import PeriodicCallback
def run_periodic(callback_time, durations, now=1000):
    pc = PeriodicCallback(None, callback_time)
    pc._next_timeout = now
    calls = []
    for d in durations:
        pc._update_next(now)
        calls.append(pc._next_timeout)
        now = pc._next_timeout + d
    return [int(round(x)) for x in calls]



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([1005, 1020, 1025, 1030, 1035], run_periodic(5000, [14, 3, 0, -18, 15]))

    def test_diversity_2(self):
        self.assertEqual([1005, 1010, 1025, 1045, 1060, 1065], run_periodic(5000, [0, 13, 15, 14, -86, 3]))

    def test_diversity_3(self):
        self.assertEqual([1010, 1020, 1030], run_periodic(10000, [-69, 5, 3]))

    def test_diversity_4(self):
        self.assertEqual([1001, 1015, 1027, 1028, 1035], run_periodic(1000, [13, 11, -69, 6, 9]))

    def test_diversity_5(self):
        self.assertEqual([1002, 1004, 1010], run_periodic(2000, [-74, 5, 3]))

    def test_diversity_6(self):
        self.assertEqual([1005, 1015, 1020, 1040, 1050], run_periodic(5000, [6, -82, 15, 5, 5]))

    def test_diversity_7(self):
        self.assertEqual([1005, 1010, 1020, 1025, 1040], run_periodic(5000, [3, 5, -106, 12, 14]))

    def test_diversity_8(self):
        self.assertEqual([1002, 1010, 1020, 1022], run_periodic(2000, [7, 9, -36, 9]))

    def test_diversity_9(self):
        self.assertEqual([1001, 1002, 1013, 1016, 1019], run_periodic(1000, [-36, 10, 2, 2, 4]))

    def test_diversity_10(self):
        self.assertEqual([1005, 1010, 1015], run_periodic(5000, [3, -91, 9]))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([1005, 1030, 1040, 1070], run_periodic(5000, [22, 6, 29, 15]))

    def test_diversity_2(self):
        self.assertEqual([1005, 1045, 1055, 1090], run_periodic(5000, [36, 7, 32, 4]))

    def test_diversity_3(self):
        self.assertEqual([1001, 1029, 1063], run_periodic(1000, [27, 33, 7]))

    def test_diversity_4(self):
        self.assertEqual([1005, 1040, 1070, 1095, 1140, 1180], run_periodic(5000, [30, 27, 22, 40, 39, 35]))

    def test_diversity_5(self):
        self.assertEqual([1005, 1020, 1025, 1055, 1090], run_periodic(5000, [11, 1, 29, 34, 28]))

    def test_diversity_6(self):
        self.assertEqual([1001, 1014, 1020, 1051, 1079], run_periodic(1000, [12, 5, 30, 27, 11]))

    def test_diversity_7(self):
        self.assertEqual([1002, 1042, 1072], run_periodic(2000, [39, 29, 36]))

    def test_diversity_8(self):
        self.assertEqual([1002, 1028, 1032, 1044, 1064, 1092], run_periodic(2000, [24, 3, 11, 19, 26, 39]))

    def test_diversity_9(self):
        self.assertEqual([1001, 1017, 1046], run_periodic(1000, [15, 28, 28]))

    def test_diversity_10(self):
        self.assertEqual([1010, 1030, 1060, 1070], run_periodic(10000, [15, 29, 8, 37]))
