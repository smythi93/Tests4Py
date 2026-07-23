import unittest

# noinspection PyUnresolvedReferences
from scrapy.utils.datatypes import LocalCache


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        cache = LocalCache()
        for i in range(28):
            cache[str(i)] = i
        self.assertEqual(28, len(cache))
        self.assertEqual(27, cache['27'])

    def test_diversity_2(self):
        cache = LocalCache()
        for i in range(15):
            cache[str(i)] = i
        self.assertEqual(15, len(cache))
        self.assertEqual(14, cache['14'])

    def test_diversity_3(self):
        cache = LocalCache()
        for i in range(39):
            cache[str(i)] = i
        self.assertEqual(39, len(cache))
        self.assertEqual(38, cache['38'])

    def test_diversity_4(self):
        cache = LocalCache()
        for i in range(31):
            cache[str(i)] = i
        self.assertEqual(31, len(cache))
        self.assertEqual(30, cache['30'])

    def test_diversity_5(self):
        cache = LocalCache()
        for i in range(13):
            cache[str(i)] = i
        self.assertEqual(13, len(cache))
        self.assertEqual(12, cache['12'])

    def test_diversity_6(self):
        cache = LocalCache()
        for i in range(19):
            cache[str(i)] = i
        self.assertEqual(19, len(cache))
        self.assertEqual(18, cache['18'])

    def test_diversity_7(self):
        cache = LocalCache()
        for i in range(23):
            cache[str(i)] = i
        self.assertEqual(23, len(cache))
        self.assertEqual(22, cache['22'])

    def test_diversity_8(self):
        cache = LocalCache()
        for i in range(25):
            cache[str(i)] = i
        self.assertEqual(25, len(cache))
        self.assertEqual(24, cache['24'])

    def test_diversity_9(self):
        cache = LocalCache()
        for i in range(7):
            cache[str(i)] = i
        self.assertEqual(7, len(cache))
        self.assertEqual(6, cache['6'])

    def test_diversity_10(self):
        cache = LocalCache()
        for i in range(5):
            cache[str(i)] = i
        self.assertEqual(5, len(cache))
        self.assertEqual(4, cache['4'])


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        cache = LocalCache(limit=12)
        for i in range(17):
            cache[str(i)] = i
        self.assertEqual(12, len(cache))
        self.assertEqual(16, cache['16'])

    def test_diversity_2(self):
        cache = LocalCache(limit=21)
        for i in range(13):
            cache[str(i)] = i
        self.assertEqual(13, len(cache))
        self.assertEqual(12, cache['12'])

    def test_diversity_3(self):
        cache = LocalCache(limit=8)
        for i in range(23):
            cache[str(i)] = i
        self.assertEqual(8, len(cache))
        self.assertEqual(22, cache['22'])

    def test_diversity_4(self):
        cache = LocalCache(limit=9)
        for i in range(5):
            cache[str(i)] = i
        self.assertEqual(5, len(cache))
        self.assertEqual(4, cache['4'])

    def test_diversity_5(self):
        cache = LocalCache(limit=25)
        for i in range(20):
            cache[str(i)] = i
        self.assertEqual(20, len(cache))
        self.assertEqual(19, cache['19'])

    def test_diversity_6(self):
        cache = LocalCache(limit=14)
        for i in range(29):
            cache[str(i)] = i
        self.assertEqual(14, len(cache))
        self.assertEqual(28, cache['28'])

    def test_diversity_7(self):
        cache = LocalCache(limit=23)
        for i in range(24):
            cache[str(i)] = i
        self.assertEqual(23, len(cache))
        self.assertEqual(23, cache['23'])

    def test_diversity_8(self):
        cache = LocalCache(limit=23)
        for i in range(28):
            cache[str(i)] = i
        self.assertEqual(23, len(cache))
        self.assertEqual(27, cache['27'])

    def test_diversity_9(self):
        cache = LocalCache(limit=5)
        for i in range(20):
            cache[str(i)] = i
        self.assertEqual(5, len(cache))
        self.assertEqual(19, cache['19'])

    def test_diversity_10(self):
        cache = LocalCache(limit=17)
        for i in range(36):
            cache[str(i)] = i
        self.assertEqual(17, len(cache))
        self.assertEqual(35, cache['35'])
