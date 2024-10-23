import unittest
from spacy.matcher import Matcher
from spacy.util import get_lang_class


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 876}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_2(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 9092}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_3(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 7767}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_4(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 5467}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_5(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 629}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_6(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 4805}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_7(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 9611}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_8(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 2956}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_9(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 8421}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_10(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 2887}, {'OP': '-'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'VINucUGggmJpb'}, {'OP': '?'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_2(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'ZHvwdpvR'}, {'OP': '1'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_3(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'UlhfT'}, {'OP': '?'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_4(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'YQzAS'}, {'OP': '+'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_5(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'hgoQljZrZPZAcWw'}, {'OP': '*'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_6(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'EEbMAlUbKTDma'}, {'OP': '+'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_7(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'CNzxXdrrJQAitf'}, {'OP': '*'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_8(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'CDXXQNemrSmnnOS'}, {'OP': '*'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_9(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'RSgmRA'}, {'OP': '+'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher

    def test_diversity_10(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        pattern = [{'ORTH': 'mcXdHFWZAe'}, {'OP': '+'}]
        assert len(matcher) == 0
        matcher.add('Rule', None, pattern)
        assert 'Rule' in matcher
