import unittest
from pandas import DataFrame


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        df = DataFrame({'a': [775, 762]}, index=[(775, 762), (14, 264)])
        self.assertEqual(762, df.at[(775, 762), 'a'])

    def test_diversity_2(self):
        df = DataFrame({'z': [31, 22]}, index=[(31, 22), (53, 954)])
        self.assertEqual(22, df.at[(31, 22), 'z'])

    def test_diversity_3(self):
        df = DataFrame({'g': [392, 175]}, index=[(392, 175), (626, 330)])
        self.assertEqual(2, df.index.nlevels)

    def test_diversity_4(self):
        df = DataFrame({'u': [768, 423]}, index=[(768, 423), (95, 285)])
        self.assertEqual(423, df.at[(768, 423), 'u'])

    def test_diversity_5(self):
        df = DataFrame({'f': [60, 282]}, index=[(60, 282), (893, 805)])
        self.assertEqual(2, df.index.nlevels)

    def test_diversity_6(self):
        df = DataFrame({'c': [848, 545]}, index=[(848, 545), (100, 813)])
        self.assertEqual(2, df.index.nlevels)

    def test_diversity_7(self):
        df = DataFrame({'i': [503, 161]}, index=[(503, 161), (875, 178)])
        self.assertEqual(2, df.index.nlevels)

    def test_diversity_8(self):
        df = DataFrame({'w': [630, 392]}, index=[(630, 392), (464, 142)])
        self.assertEqual(2, df.index.nlevels)

    def test_diversity_9(self):
        df = DataFrame({'o': [890, 481]}, index=[(890, 481), (537, 613)])
        self.assertEqual(2, df.index.nlevels)

    def test_diversity_10(self):
        df = DataFrame({'f': [990, 733]}, index=[(990, 733), (273, 62)])
        self.assertEqual(733, df.at[(990, 733), 'f'])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        df = DataFrame({'f': [454, 190]}, index=[(454, 190), (56, 48)])
        self.assertEqual(454, df.at[(454, 190), 'f'])

    def test_diversity_2(self):
        df = DataFrame({'q': [76, 371]}, index=[(76, 371), (513, 81)])
        self.assertEqual(76, df.at[(76, 371), 'q'])

    def test_diversity_3(self):
        df = DataFrame({'y': [691, 45]}, index=[(691, 45), (265, 95)])
        self.assertEqual(691, df.at[(691, 45), 'y'])

    def test_diversity_4(self):
        df = DataFrame({'t': [819, 523]}, index=[(819, 523), (185, 80)])
        self.assertEqual(1, df.index.nlevels)

    def test_diversity_5(self):
        df = DataFrame({'p': [514, 591]}, index=[(514, 591), (534, 64)])
        self.assertEqual(1, df.index.nlevels)

    def test_diversity_6(self):
        df = DataFrame({'h': [274, 476]}, index=[(274, 476), (476, 421)])
        self.assertEqual(274, df.at[(274, 476), 'h'])

    def test_diversity_7(self):
        df = DataFrame({'l': [658, 807]}, index=[(658, 807), (154, 318)])
        self.assertEqual(658, df.at[(658, 807), 'l'])

    def test_diversity_8(self):
        df = DataFrame({'u': [690, 343]}, index=[(690, 343), (844, 797)])
        self.assertEqual(1, df.index.nlevels)

    def test_diversity_9(self):
        df = DataFrame({'p': [316, 585]}, index=[(316, 585), (891, 477)])
        self.assertEqual(316, df.at[(316, 585), 'p'])

    def test_diversity_10(self):
        df = DataFrame({'r': [841, 399]}, index=[(841, 399), (347, 736)])
        self.assertEqual(841, df.at[(841, 399), 'r'])
