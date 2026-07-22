import unittest

# noinspection PyUnresolvedReferences
from tqdm import tqdm


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(None, tqdm((x for x in range(792)), disable=True).__len__())

    def test_diversity_2(self):
        self.assertEqual(None, tqdm((x for x in range(34)), disable=True).__len__())

    def test_diversity_3(self):
        self.assertEqual(None, tqdm((x for x in range(574)), disable=True).__len__())

    def test_diversity_4(self):
        self.assertEqual(None, tqdm((x for x in range(219)), disable=True).__len__())

    def test_diversity_5(self):
        self.assertEqual(None, tqdm((x for x in range(147)), disable=True).__len__())

    def test_diversity_6(self):
        self.assertEqual(None, tqdm((x for x in range(663)), disable=True).__len__())

    def test_diversity_7(self):
        self.assertEqual(None, tqdm((x for x in range(439)), disable=True).__len__())

    def test_diversity_8(self):
        self.assertEqual(None, tqdm((x for x in range(436)), disable=True).__len__())

    def test_diversity_9(self):
        self.assertEqual(None, tqdm((x for x in range(626)), disable=True).__len__())

    def test_diversity_10(self):
        self.assertEqual(None, tqdm((x for x in range(655)), disable=True).__len__())


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(751, tqdm(range(751), disable=True).__len__())

    def test_diversity_2(self):
        self.assertEqual(641, tqdm(list(range(641)), disable=True).__len__())

    def test_diversity_3(self):
        self.assertEqual(589, tqdm(range(589), disable=True).__len__())

    def test_diversity_4(self):
        self.assertEqual(76, tqdm(list(range(76)), disable=True).__len__())

    def test_diversity_5(self):
        self.assertEqual(546, tqdm(list(range(546)), disable=True).__len__())

    def test_diversity_6(self):
        self.assertEqual(112, tqdm(range(112), disable=True).__len__())

    def test_diversity_7(self):
        self.assertEqual(374, tqdm(range(374), disable=True).__len__())

    def test_diversity_8(self):
        self.assertEqual(367, tqdm(list(range(367)), disable=True).__len__())

    def test_diversity_9(self):
        self.assertEqual(806, tqdm(list(range(806)), disable=True).__len__())

    def test_diversity_10(self):
        self.assertEqual(332, tqdm(list(range(332)), disable=True).__len__())

