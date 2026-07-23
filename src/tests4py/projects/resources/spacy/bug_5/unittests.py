import unittest
from spacy.language import Language
from spacy.vocab import Vocab



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('nzpogt getlz', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_2(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('abfs psk', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_3(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('gqfklw rck xfcpfu aef', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_4(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('iax cvza ocaof wxds', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_5(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('rgeekrk', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_6(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('ahqbvw akeji', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_7(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('jxd', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_8(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('otfmnff ibz itrr lyif', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_9(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('lphhde ubxujde ngrvep dbc', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_10(self):
        nlp = Language(Vocab())
        def pipe(doc):
            return doc
        nlp.add_pipe(pipe, name='plain')
        nlp.evaluate([('mja bfqd', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        nlp = Language(Vocab())
        class PipeWithPipe(object):
            name = 'withpipe'

            def __call__(self, doc):
                return doc

            def pipe(self, docs, **kwargs):
                for doc in docs:
                    yield doc
        nlp.add_pipe(PipeWithPipe(), name='withpipe')
        nlp.evaluate([('ekwprh qnbh', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_2(self):
        nlp = Language(Vocab())
        class PipeWithPipe(object):
            name = 'withpipe'

            def __call__(self, doc):
                return doc

            def pipe(self, docs, **kwargs):
                for doc in docs:
                    yield doc
        nlp.add_pipe(PipeWithPipe(), name='withpipe')
        nlp.evaluate([('lynqc rxmise dejgvcw', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_3(self):
        nlp = Language(Vocab())
        nlp.evaluate([('hefxn qfyv', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_4(self):
        nlp = Language(Vocab())
        nlp.evaluate([('fwpsrfq uapxefj azlivz ynp', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_5(self):
        nlp = Language(Vocab())
        nlp.evaluate([('qatc efr', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_6(self):
        nlp = Language(Vocab())
        nlp.evaluate([('amxcgvc uwn', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_7(self):
        nlp = Language(Vocab())
        class PipeWithPipe(object):
            name = 'withpipe'

            def __call__(self, doc):
                return doc

            def pipe(self, docs, **kwargs):
                for doc in docs:
                    yield doc
        nlp.add_pipe(PipeWithPipe(), name='withpipe')
        nlp.evaluate([('qehtflk srsa qcjbic fbcvja', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_8(self):
        nlp = Language(Vocab())
        nlp.evaluate([('timpx szhttfq', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_9(self):
        nlp = Language(Vocab())
        class PipeWithPipe(object):
            name = 'withpipe'

            def __call__(self, doc):
                return doc

            def pipe(self, docs, **kwargs):
                for doc in docs:
                    yield doc
        nlp.add_pipe(PipeWithPipe(), name='withpipe')
        nlp.evaluate([('ctnctyc', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)

    def test_diversity_10(self):
        nlp = Language(Vocab())
        class PipeWithPipe(object):
            name = 'withpipe'

            def __call__(self, doc):
                return doc

            def pipe(self, docs, **kwargs):
                for doc in docs:
                    yield doc
        nlp.add_pipe(PipeWithPipe(), name='withpipe')
        nlp.evaluate([('jafchnz fle bvd qsr', {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}})])
        self.assertTrue(True)
