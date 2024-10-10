import unittest
import pytest
from spacy.lang.en import English
from spacy.lookups import Lookups


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        text = 'zyXsVXPOTQ'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('parser')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_2(self):
        text = 'oBiTRyTj'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('ner')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_3(self):
        text = 'aoATVNziU'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('ner')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_4(self):
        text = 'JwLcuzZI'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('ner')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_5(self):
        text = 'DWzMLpTVJvBxG'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('ner')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_6(self):
        text = 'FcCwnGuRkGfTB'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('ner')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_7(self):
        text = 'MdheEw'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('parser')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_8(self):
        text = 'tdQRpuYyFPqHNu'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tokenizer')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_9(self):
        text = 'kfqPYLhmXNke'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_10(self):
        text = 'ZeMLYbOMJcWNY'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('ner')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        text = 'wWgvQry'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('textcat')
        assert not len(nlp.vocab.lookups)

    def test_diversity_2(self):
        text = 'pvKyFtUP'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('tagger')
        assert not len(nlp.vocab.lookups)

    def test_diversity_3(self):
        text = 'lChlLNk'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('tagger')
        assert not len(nlp.vocab.lookups)

    def test_diversity_4(self):
        text = 'HzzAE'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('ner')
        assert not len(nlp.vocab.lookups)

    def test_diversity_5(self):
        text = 'gkJvoKi'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('ner')
        assert not len(nlp.vocab.lookups)

    def test_diversity_6(self):
        text = 'GOTEfaluJf'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('textcat')
        assert not len(nlp.vocab.lookups)

    def test_diversity_7(self):
        text = 'XkYKkikczxdQmaS'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('textcat')
        assert not len(nlp.vocab.lookups)

    def test_diversity_8(self):
        text = 'xhbcaZBsqDhXuzy'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('tagger')
        assert not len(nlp.vocab.lookups)

    def test_diversity_9(self):
        text = 'rQFeCtfphYRMNq'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('parser')
        assert not len(nlp.vocab.lookups)

    def test_diversity_10(self):
        text = 'VkbYbufvcFJG'
        nlp = English()
        nlp.vocab.lookups = Lookups()
        tagger = nlp.create_pipe('tagger')
        assert not len(nlp.vocab.lookups)
