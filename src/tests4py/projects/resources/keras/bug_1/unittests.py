import unittest
from spacy.language import Language
from spacy.vocab import Vocab


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        def pipe(doc):
            return doc
        text = 'TJmoNjMrwMpZf'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_2(self):

        def pipe(doc):
            return doc
        text = 'zwWhrxAvWAN'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_3(self):

        def pipe(doc):
            return doc
        text = 'wYognIXwId'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_4(self):

        def pipe(doc):
            return doc
        text = 'qzrMVjLNIScniti'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_5(self):

        def pipe(doc):
            return doc
        text = 'wmCkuS'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_6(self):

        def pipe(doc):
            return doc
        text = 'JxWApFi'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_7(self):

        def pipe(doc):
            return doc
        text = 'oShCvKCHFctg'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_8(self):

        def pipe(doc):
            return doc
        text = 'LbOMfcA'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_9(self):

        def pipe(doc):
            return doc
        text = 'HWYmdzcbdvX'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])

    def test_diversity_10(self):

        def pipe(doc):
            return doc
        text = 'dIaVb'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        nlp.add_pipe(pipe)
        nlp.evaluate([(text, annots)])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        def pipe(doc):
            return doc

        text = 'ZGofI'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_2(self):
        def pipe(doc):
            return doc

        text = 'fKmgfatpjH'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_3(self):
        def pipe(doc):
            return doc

        text = 'FKsssXlyFlgVNq'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_4(self):
        def pipe(doc):
            return doc

        text = 'LZGKT'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_5(self):
        def pipe(doc):
            return doc

        text = 'sJkVeiHxIS'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_6(self):
        def pipe(doc):
            return doc

        text = 'QbSlPMGZcwmBz'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_7(self):
        def pipe(doc):
            return doc

        text = 'XbIFBeOeTIT'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_8(self):
        def pipe(doc):
            return doc

        text = 'BGKrAH'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_9(self):
        def pipe(doc):
            return doc

        text = 'IblRBuUzDFOA'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])

    def test_diversity_10(self):
        def pipe(doc):
            return doc

        text = 'AZbwuVEqvS'
        annots = {'cats': {'POSITIVE': 1.0, 'NEGATIVE': 0.0}}
        nlp = Language(Vocab())
        doc = nlp(text)
        nlp.add_pipe(pipe)
        with self.assertRaises(TypeError):
            nlp.evaluate([(doc, annots)])
