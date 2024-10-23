import unittest
from spacy.util import get_lang_class
from spacy.tests.util import get_doc
from spacy.util import filter_spans


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        text = 'This is sentence 3118. This is sentence 4246. And sentence 6997.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_2(self):
        text = 'This is sentence 9904. This is sentence 2201. And sentence 5597.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_3(self):
        text = 'This is sentence 2458. This is sentence 3872. And sentence 4804.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_4(self):
        text = 'This is sentence 4764. This is sentence 4179. And sentence 6457.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_5(self):
        text = 'This is sentence 2318. This is sentence 8135. And sentence 3230.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_6(self):
        text = 'This is sentence 230. This is sentence 9136. And sentence 3283.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_7(self):
        text = 'This is sentence 38. This is sentence 7835. And sentence 2136.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_8(self):
        text = 'This is sentence 3845. This is sentence 7022. And sentence 6351.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_9(self):
        text = 'This is sentence 1332. This is sentence 3232. And sentence 542.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5

    def test_diversity_10(self):
        text = 'This is sentence 4463. This is sentence 3296. And sentence 2291.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 5


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        text = 'This is sentence 1938. This is sentence 2869. And sentence 3534.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_2(self):
        text = 'This is sentence 122. This is sentence 5964. And sentence 1273.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_3(self):
        text = 'This is sentence 6601. This is sentence 6226. And sentence 2853.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_4(self):
        text = 'This is sentence 9273. This is sentence 7279. And sentence 8663.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_5(self):
        text = 'This is sentence 6551. This is sentence 5516. And sentence 1282.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_6(self):
        text = 'This is sentence 6137. This is sentence 3056. And sentence 2710.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_7(self):
        text = 'This is sentence 2775. This is sentence 9587. And sentence 1751.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_8(self):
        text = 'This is sentence 9297. This is sentence 2188. And sentence 6291.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_9(self):
        text = 'This is sentence 3462. This is sentence 2814. And sentence 2377.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3

    def test_diversity_10(self):
        text = 'This is sentence 7591. This is sentence 538. And sentence 7760.'
        heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
        deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det',
                'npadvmod', 'punct']
        tokenizer = get_lang_class('en').Defaults.create_tokenizer()
        tokens = tokenizer(text)
        doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
        spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
        filtered = filter_spans(spans)
        assert len(filtered) == 3
