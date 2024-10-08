import unittest
import spacy
import pytest
from spacy.language import Language, component


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('bBaftWVnDyAWcI', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('gqQideFIfh', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('gqQideFIfh')
        assert not record.list

    def test_diversity_2(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('VjzrHUL', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('QjAZs', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('QjAZs')
        assert not record.list

    def test_diversity_3(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('bCDrLSsVvmskd', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('KNETkxaK', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('KNETkxaK')
        assert not record.list

    def test_diversity_4(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('alxwSPujdPM', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('tmUZMfkJ', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('tmUZMfkJ')
        assert not record.list

    def test_diversity_5(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('agXCuUyyUGK', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('nVKaofrEFlJxbtH', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('nVKaofrEFlJxbtH')
        assert not record.list

    def test_diversity_6(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('agrQF', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('SrdQKJsGc', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('SrdQKJsGc')
        assert not record.list

    def test_diversity_7(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('cDqyoXgCPl', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('SjUIQSOJglJdz', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('SjUIQSOJglJdz')
        assert not record.list

    def test_diversity_8(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('yDcKn', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('bmHusB', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('bmHusB')
        assert not record.list

    def test_diversity_9(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('RlSgzeIHZNmXvS', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('irLGv', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('irLGv')
        assert not record.list

    def test_diversity_10(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('HpHJPVpXPfXcUxx', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('JIINkyCxbfShmZB', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('JIINkyCxbfShmZB')
        assert not record.list


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('wySYiTtKmCmmR', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('orCknyhOw', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('orCknyhOw')
        assert record.list

    def test_diversity_2(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('dcHIbUes', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('XpgxIUDChmyI', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('XpgxIUDChmyI')
        assert record.list

    def test_diversity_3(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('zZfmuCWut', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('kYFIuAx', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('kYFIuAx')
        assert record.list

    def test_diversity_4(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('QBHTDmDc', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('KQrHovWIm', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('KQrHovWIm')
        assert record.list

    def test_diversity_5(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('LVyHOoZf', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('GkKnJwcnDTD', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('GkKnJwcnDTD')
        assert record.list

    def test_diversity_6(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('ZOBJm', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('vahDEYFjiH', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('vahDEYFjiH')
        assert record.list

    def test_diversity_7(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('gdmITTMXkRAMfOr', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('tSRgTuZQfx', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('tSRgTuZQfx')
        assert record.list

    def test_diversity_8(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('chAPKiANq', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('aGjEqgrYjeF', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('aGjEqgrYjeF')
        assert record.list

    def test_diversity_9(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('rbyDBLtQAvH', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('oefUvmnmD', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('oefUvmnmD')
        assert record.list

    def test_diversity_10(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True

        @component('bucqxnUlCj', assigns=['token.tag'])
        def c1(doc):
            return doc

        @component('TUMloPGTryw', requires=['token.pos'])
        def c2(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1)
        with pytest.warns(UserWarning):
            nlp.add_pipe(c2)
        with pytest.warns(None) as record:
            nlp.remove_pipe('TUMloPGTryw')
        assert record.list
