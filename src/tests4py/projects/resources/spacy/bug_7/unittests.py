import unittest
from spacy.util import filter_spans
from spacy.tokens import Doc
from spacy.vocab import Vocab



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(6)])
        spans = [doc[3:5], doc[4:6]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(3, 5)], kept)

    def test_diversity_2(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(7)])
        spans = [doc[3:5], doc[4:6]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(3, 5)], kept)

    def test_diversity_3(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(6)])
        spans = [doc[0:2], doc[1:3]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(0, 2)], kept)

    def test_diversity_4(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(10)])
        spans = [doc[3:6], doc[4:7]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(3, 6)], kept)

    def test_diversity_5(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(8)])
        spans = [doc[4:6], doc[5:7]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(4, 6)], kept)

    def test_diversity_6(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(8)])
        spans = [doc[2:4], doc[3:5]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(2, 4)], kept)

    def test_diversity_7(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(11)])
        spans = [doc[1:4], doc[3:6]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(1, 4)], kept)

    def test_diversity_8(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(11)])
        spans = [doc[4:7], doc[6:9]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(4, 7)], kept)

    def test_diversity_9(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(10)])
        spans = [doc[5:8], doc[7:10]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(5, 8)], kept)

    def test_diversity_10(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(9)])
        spans = [doc[1:5], doc[4:8]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(1, 5)], kept)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(7)])
        spans = [doc[0:3], doc[2:3]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(0, 3)], kept)

    def test_diversity_2(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(10)])
        spans = [doc[1:5], doc[1:4]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(1, 5)], kept)

    def test_diversity_3(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(8)])
        spans = [doc[1:6], doc[1:5]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(1, 6)], kept)

    def test_diversity_4(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(6)])
        spans = [doc[1:5], doc[2:4]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(1, 5)], kept)

    def test_diversity_5(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(5)])
        spans = [doc[1:4], doc[2:4]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(1, 4)], kept)

    def test_diversity_6(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(8)])
        spans = [doc[4:8], doc[7:8]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(4, 8)], kept)

    def test_diversity_7(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(6)])
        spans = [doc[1:5], doc[1:4]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(1, 5)], kept)

    def test_diversity_8(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(6)])
        spans = [doc[2:5], doc[3:4]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(2, 5)], kept)

    def test_diversity_9(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(8)])
        spans = [doc[4:7], doc[4:6]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(4, 7)], kept)

    def test_diversity_10(self):
        doc = Doc(Vocab(), words=[str(i) for i in range(10)])
        spans = [doc[6:10], doc[8:10]]
        kept = [(s.start, s.end) for s in filter_spans(spans)]
        self.assertEqual([(6, 10)], kept)
