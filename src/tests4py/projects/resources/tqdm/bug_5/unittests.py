import unittest

# noinspection PyUnresolvedReferences
from tqdm import tqdm


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(True, bool(tqdm(total=441, disable=True)))

    def test_diversity_2(self):
        self.assertEqual(True, bool(tqdm(total=789, disable=True)))

    def test_diversity_3(self):
        self.assertEqual(True, bool(tqdm(total=911, disable=True)))

    def test_diversity_4(self):
        self.assertEqual(True, bool(tqdm(total=1000, disable=True)))

    def test_diversity_5(self):
        self.assertEqual(True, bool(tqdm(total=807, disable=True)))

    def test_diversity_6(self):
        self.assertEqual(True, bool(tqdm(total=877, disable=True)))

    def test_diversity_7(self):
        self.assertEqual(True, bool(tqdm(total=538, disable=True)))

    def test_diversity_8(self):
        self.assertEqual(True, bool(tqdm(total=795, disable=True)))

    def test_diversity_9(self):
        self.assertEqual(True, bool(tqdm(total=277, disable=True)))

    def test_diversity_10(self):
        self.assertEqual(True, bool(tqdm(total=740, disable=True)))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(True, bool(tqdm(list(range(391)), disable=True)))

    def test_diversity_2(self):
        self.assertEqual(True, bool(tqdm(range(815), disable=True)))

    def test_diversity_3(self):
        self.assertEqual(True, bool(tqdm(range(842), disable=True)))

    def test_diversity_4(self):
        self.assertEqual(True, bool(tqdm(range(954), disable=True)))

    def test_diversity_5(self):
        self.assertEqual(True, bool(tqdm(list(range(374)), disable=True)))

    def test_diversity_6(self):
        self.assertEqual(True, bool(tqdm(list(range(566)), disable=True)))

    def test_diversity_7(self):
        self.assertEqual(True, bool(tqdm(list(range(385)), disable=True)))

    def test_diversity_8(self):
        self.assertEqual(True, bool(tqdm(range(412), disable=True)))

    def test_diversity_9(self):
        self.assertEqual(True, bool(tqdm(range(285), disable=True)))

    def test_diversity_10(self):
        self.assertEqual(True, bool(tqdm(list(range(160)), disable=True)))

