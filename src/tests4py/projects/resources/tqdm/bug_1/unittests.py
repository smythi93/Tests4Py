import unittest

# noinspection PyUnresolvedReferences
from tqdm.contrib import tenumerate


def run_tenumerate(items, start):
    return [i for i, _ in tenumerate(items, start=start, disable=True)]


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual([343, 344, 345, 346, 347], run_tenumerate(['T', 'gzLh', 'tQF', 'NA', 'hHIIiMB'], 343))

    def test_diversity_2(self):
        self.assertEqual([-282, -281], run_tenumerate(['fxW', 'cVLF'], -282))

    def test_diversity_3(self):
        self.assertEqual([4, 5, 6, 7], run_tenumerate(['rzgG', 'zCfQ', 'NmpcOS', 'FPRgd'], 4))

    def test_diversity_4(self):
        self.assertEqual([449, 450, 451, 452, 453, 454], run_tenumerate(['VRGGOUg', 'zH', 'Or', 'LQE', 'qhGw', 'ICQkO'], 449))

    def test_diversity_5(self):
        self.assertEqual([-94, -93, -92, -91, -90], run_tenumerate(['CCfxoo', 'mrFraBq', 'vE', 'jHZrmBbR', 'WwKnWj'], -94))

    def test_diversity_6(self):
        self.assertEqual([-5, -4, -3], run_tenumerate(['PJOXdfp', 'DYa', 'eZsOOYzl'], -5))

    def test_diversity_7(self):
        self.assertEqual([-402, -401, -400, -399, -398], run_tenumerate(['kUC', 'HHKGJZv', 'JmZTAQeo', 'qTKFzjqK', 'pF'], -402))

    def test_diversity_8(self):
        self.assertEqual([-487, -486, -485, -484, -483], run_tenumerate(['pBgcd', 'qMlRxU', 'qtCZy', 'A', 'JhoiAuq'], -487))

    def test_diversity_9(self):
        self.assertEqual([-261, -260], run_tenumerate(['aV', 'yqka'], -261))

    def test_diversity_10(self):
        self.assertEqual([404, 405], run_tenumerate(['GYnE', 'dshBchHd'], 404))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual([0, 1, 2, 3, 4], run_tenumerate(['vNhBMZiK', 'AZROv', 'jvFX', 'yTq', 'CiLVr'], 0))

    def test_diversity_2(self):
        self.assertEqual([0, 1, 2, 3, 4], run_tenumerate(['AkNzv', 'GxatPGr', 'ZblF', 'kYWPEM', 'APUA'], 0))

    def test_diversity_3(self):
        self.assertEqual([0, 1, 2, 3, 4], run_tenumerate(['Iigs', 'A', 'sghHUl', 'vaW', 'WX'], 0))

    def test_diversity_4(self):
        self.assertEqual([0, 1, 2, 3], run_tenumerate(['MPBDwk', 'VVMfDxXX', 'j', 'fuQPQf'], 0))

    def test_diversity_5(self):
        self.assertEqual([0, 1], run_tenumerate(['L', 'MO'], 0))

    def test_diversity_6(self):
        self.assertEqual([0, 1, 2, 3, 4], run_tenumerate(['WdeKgPv', 'fC', 'MjmSPA', 'A', 'NHY'], 0))

    def test_diversity_7(self):
        self.assertEqual([0, 1, 2], run_tenumerate(['oYZfG', 'Fu', 'nmkCxA'], 0))

    def test_diversity_8(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], run_tenumerate(['Jn', 'IQyWxVu', 'rAzwS', 'PhmqnFs', 'tOqB', 's'], 0))

    def test_diversity_9(self):
        self.assertEqual([0, 1, 2, 3, 4, 5], run_tenumerate(['IlqTKyZ', 'guu', 'hayTX', 'as', 'taiL', 'Ju'], 0))

    def test_diversity_10(self):
        self.assertEqual([0, 1, 2], run_tenumerate(['XNJnmTRR', 'GnvKY', 'h'], 0))

