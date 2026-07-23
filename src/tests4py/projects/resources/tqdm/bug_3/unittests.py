import unittest

# noinspection PyUnresolvedReferences
from tqdm import tqdm


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(bool(tqdm((x for x in range(220)), disable=True)))

    def test_diversity_2(self):
        self.assertTrue(bool(tqdm((x for x in range(345)), disable=True)))

    def test_diversity_3(self):
        self.assertTrue(bool(tqdm((x for x in range(152)), disable=True)))

    def test_diversity_4(self):
        self.assertTrue(bool(tqdm((x for x in range(160)), disable=True)))

    def test_diversity_5(self):
        self.assertTrue(bool(tqdm((x for x in range(212)), disable=True)))

    def test_diversity_6(self):
        self.assertTrue(bool(tqdm((x for x in range(603)), disable=True)))

    def test_diversity_7(self):
        self.assertTrue(bool(tqdm((x for x in range(300)), disable=True)))

    def test_diversity_8(self):
        self.assertTrue(bool(tqdm((x for x in range(814)), disable=True)))

    def test_diversity_9(self):
        self.assertTrue(bool(tqdm((x for x in range(110)), disable=True)))

    def test_diversity_10(self):
        self.assertTrue(bool(tqdm((x for x in range(718)), disable=True)))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(True, bool(tqdm(list(range(847)), disable=True)))

    def test_diversity_2(self):
        self.assertEqual(True, bool(tqdm(total=538, disable=True)))

    def test_diversity_3(self):
        self.assertEqual(True, bool(tqdm(list(range(822)), disable=True)))

    def test_diversity_4(self):
        self.assertEqual(True, bool(tqdm(list(range(904)), disable=True)))

    def test_diversity_5(self):
        self.assertEqual(True, bool(tqdm(total=898, disable=True)))

    def test_diversity_6(self):
        self.assertEqual(True, bool(tqdm(total=831, disable=True)))

    def test_diversity_7(self):
        self.assertEqual(True, bool(tqdm(list(range(805)), disable=True)))

    def test_diversity_8(self):
        self.assertEqual(True, bool(tqdm(total=73, disable=True)))

    def test_diversity_9(self):
        self.assertEqual(True, bool(tqdm(total=172, disable=True)))

    def test_diversity_10(self):
        self.assertEqual(True, bool(tqdm(total=999, disable=True)))

