import unittest

from youtube_dl.utils import match_str


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(match_str('!is_live', {'is_live': False}))

    def test_diversity_2(self):
        self.assertTrue(match_str('!test', {'test': False}))

    def test_diversity_3(self):
        self.assertTrue(match_str(
            '!like_count & dislike_count <? 50 & description',
            {'like_count': False, 'dislike_count': 10}))

    def test_diversity_4(self):
        self.assertTrue(match_str(
            'like_count > 100 & dislike_count <? 50 & !description',
            {'like_count': 190, 'dislike_count': 23, 'description': False})
        )

    def test_diversity_5(self):
        self.assertTrue(match_str(
            'like_count > 100 & !description',
            {'like_count': 190, 'dislike_count': 4, 'description': False})
        )

    def test_diversity_6(self):
        self.assertTrue(match_str(
            '!other & !description',
            {'other': False, 'dislike_count': 1, 'description': False})
        )

    def test_diversity_7(self):
        self.assertTrue(match_str(
            '!description',
            {'other': False, 'dislike_count': 99999, 'description': False})
        )

    def test_diversity_8(self):
        self.assertTrue(match_str(
            '!title & title ?> 10',
            {'title': False, 'description': False})
        )

    def test_diversity_9(self):
        self.assertTrue(match_str(
            'title ?> 10 & !title ',
            {'title': False})
        )

    def test_diversity_10(self):
        self.assertTrue(match_str(
            '!is_live & description',
            {'is_live': False, 'description': True})
        )


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        result: bool = match_str('x>?0', {})
        self.assertTrue(result)

    def test_diversity_2(self):
        self.assertFalse(match_str('is_live', {'is_live': None}))

    def test_diversity_3(self):
        self.assertTrue(match_str('!is_live', {'is_live': None}))

    def test_diversity_4(self):
        self.assertFalse(match_str('!title', {'title': ''}))

    def test_diversity_5(self):
        self.assertFalse(match_str(
            'like_count > 100 & dislike_count <? 50 & description',
            {'like_count': 190, 'dislike_count': 10}))

    def test_diversity_6(self):
        self.assertTrue(match_str(
            'like_count > 100 & dislike_count <? 50 & description',
            {'like_count': 190, 'dislike_count': 10, 'description': True})
        )

    def test_diversity_7(self):
        self.assertFalse(match_str(
            'dislike_count >? 50 & description',
            {'like_count': 190, 'dislike_count': 10, 'description': True})
        )

    def test_diversity_8(self):
        self.assertTrue(match_str(
            'like_count > 100',
            {'like_count': 190, 'title': False})
        )

    def test_diversity_9(self):
        self.assertFalse(match_str('!title', {'title': 'abc'}))

    def test_diversity_10(self):
        self.assertFalse(match_str('is_live', {}))
