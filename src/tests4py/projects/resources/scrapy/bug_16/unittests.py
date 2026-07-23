import unittest

# noinspection PyUnresolvedReferences
from scrapy.utils.url import canonicalize_url


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://jenrg.example.net/fjmm%A3efvqi', canonicalize_url('http://jenrg.example.net/fjmm%a3efvqi'))

    def test_diversity_2(self):
        self.assertEqual('http://knc.example.com/cd%87zo', canonicalize_url('http://knc.example.com/cd%87zo'))

    def test_diversity_3(self):
        self.assertEqual('http://ruhxo.example.net/eoj%A3xura', canonicalize_url('http://ruhxo.example.net/eoj%a3xura'))

    def test_diversity_4(self):
        self.assertEqual('http://opwlxyi.example.com/kby%83ln', canonicalize_url('http://opwlxyi.example.com/kby%83ln'))

    def test_diversity_5(self):
        self.assertEqual('http://csb.example.org/ofdfg%A0bnqy', canonicalize_url('http://csb.example.org/ofdfg%a0bnqy'))

    def test_diversity_6(self):
        self.assertEqual('http://qcig.example.com/jb%8Etle', canonicalize_url('http://qcig.example.com/jb%8etle'))

    def test_diversity_7(self):
        self.assertEqual('http://lzlzwf.example.io/fjoi%ABfs', canonicalize_url('http://lzlzwf.example.io/fjoi%abfs'))

    def test_diversity_8(self):
        self.assertEqual('http://majy.example.org/knt%BCjvf', canonicalize_url('http://majy.example.org/knt%bcjvf'))

    def test_diversity_9(self):
        self.assertEqual('http://jvjh.example.com/exj%A4qcg', canonicalize_url('http://jvjh.example.com/exj%a4qcg'))

    def test_diversity_10(self):
        self.assertEqual('http://fnzo.example.net/srfpe%90capzz', canonicalize_url('http://fnzo.example.net/srfpe%90capzz'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://hzikezd.example.net/vwbym/zljkpn', canonicalize_url('http://hzikezd.example.net/vwbym/zljkpn'))

    def test_diversity_2(self):
        self.assertEqual('http://iczsx.example.org/ccas', canonicalize_url('http://iczsx.example.org/ccas'))

    def test_diversity_3(self):
        self.assertEqual('http://gzbtiugf.example.io/gsqink/md/ea', canonicalize_url('http://gzbtiugf.example.io/gsqink/md/ea'))

    def test_diversity_4(self):
        self.assertEqual('http://zcaf.example.io/tzehrz/uuit', canonicalize_url('http://zcaf.example.io/tzehrz/uuit'))

    def test_diversity_5(self):
        self.assertEqual('http://zcwejnh.example.io/umeliy/ortox', canonicalize_url('http://zcwejnh.example.io/umeliy/ortox'))

    def test_diversity_6(self):
        self.assertEqual('http://arhlbss.example.net/vrer/clil/rw', canonicalize_url('http://arhlbss.example.net/vrer/clil/rw'))

    def test_diversity_7(self):
        self.assertEqual('http://dgrgnp.example.com/ylimnf/cviw', canonicalize_url('http://dgrgnp.example.com/ylimnf/cviw'))

    def test_diversity_8(self):
        self.assertEqual('http://ukli.example.net/znlb/dj', canonicalize_url('http://ukli.example.net/znlb/dj'))

    def test_diversity_9(self):
        self.assertEqual('http://neh.example.io/irhe', canonicalize_url('http://neh.example.io/irhe'))

    def test_diversity_10(self):
        self.assertEqual('http://hepvro.example.io/aeybqq/jlz/rsezf', canonicalize_url('http://hepvro.example.io/aeybqq/jlz/rsezf'))
