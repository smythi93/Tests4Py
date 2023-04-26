import unittest

from youtube_dl.utils import match_str


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_2(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_3(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_4(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_5(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_6(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_7(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_8(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_9(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_10(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        result: bool = match_str('x>?0', {})
        self.assertTrue(result)
