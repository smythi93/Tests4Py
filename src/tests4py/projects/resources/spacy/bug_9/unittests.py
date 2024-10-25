import unittest
import pytest
from spacy.lookups import Lookups
from spacy.language import Language


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('BRNoXxUJ')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_2(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('hsdhjwhg')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_3(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('ghafsdhagsfd')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_4(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('HGASVHjjsa')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_5(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('DWzMLpTVJvBxG')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_6(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('hjbsdjfsdbs')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_7(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lljkjduwehiq')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_8(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('afsdgasfdhaq')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_9(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('qhgwehgqfweytq')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_10(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('bmcmzhcgjshgcka')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('gwudquqgdhqk')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_2(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('gwdvhqvdhgqj')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_3(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('afbdkwbhefbwj')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_4(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('rfbhjbfjw')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_5(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('knfjvkefnkvje')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_6(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('asdfyqtwfsqj')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_7(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('hfkebfkbkfw')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_8(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('euywgewbfk')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_9(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('gdhghajd')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list

    def test_diversity_10(self):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table('SkSohId')
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list
