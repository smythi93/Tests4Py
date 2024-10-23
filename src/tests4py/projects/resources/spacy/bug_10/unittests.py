import unittest
import pytest
from spacy.matcher import Matcher
from spacy.util import get_lang_class


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('dsHKDdxtde', [], [{'TEXT': 'test'}])

    def test_diversity_2(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('aWNlgmAmuurn', [], [{'TEXT': 'test'}])

    def test_diversity_3(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('MgJSCoFSKEJpMB', [], [{'TEXT': 'test'}])

    def test_diversity_4(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('nTVxocrDyxvE', [], [{'TEXT': 'test'}])

    def test_diversity_5(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('eECvPzmocKCsPSy', [], [{'TEXT': 'test'}])

    def test_diversity_6(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('cUAtXbivC', [], [{'TEXT': 'test'}])

    def test_diversity_7(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('FxIzGrSHyHOFD', [], [{'TEXT': 'test'}])

    def test_diversity_8(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('JQweoGLezogCaCK', [], [{'TEXT': 'test'}])

    def test_diversity_9(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('NaogNGBpBa', [], [{'TEXT': 'test'}])

    def test_diversity_10(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('MUFrvtuK', [], [{'TEXT': 'test'}])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('wSZvowCE', [], [{'INVALID KEY': 'test'}])

    def test_diversity2(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('iWtIDq', [], [{'INVALID KEY': 'test'}])

    def test_diversity_3(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('tlwGBQqdHth', [], [{'INVALID KEY': 'test'}])

    def test_diversity_4(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('zjHdduQLXEPzX', [], [{'INVALID KEY': 'test'}])

    def test_diversity_5(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('ZNnpxHnl', [], [{'INVALID KEY': 'test'}])

    def test_diversity_6(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('NlOyPBqQEcYdch', [], [{'INVALID KEY': 'test'}])

    def test_diversity_7(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('cvbvieJR', [], [{'INVALID KEY': 'test'}])

    def test_diversity_8(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('dscUWdaDkBsN', [], [{'INVALID KEY': 'test'}])

    def test_diversity_9(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('iOLnWpbbBCIRh', [], [{'INVALID KEY': 'test'}])

    def test_diversity_10(self):
        matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
        with pytest.raises(ValueError):
            matcher.add('jdvgwevguw', [], [{'INVALID KEY': 'test'}])
