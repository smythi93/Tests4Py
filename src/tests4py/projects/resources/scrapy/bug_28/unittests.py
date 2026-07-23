import shutil
import tempfile
import unittest

# noinspection PyUnresolvedReferences
from scrapy.dupefilters import RFPDupeFilter
# noinspection PyUnresolvedReferences
from scrapy.http import Request


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/tosf/668923'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/tosf/668923'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_2(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/tfdeypf/426770'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/tfdeypf/426770'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_3(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/bkxsv/184960'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/bkxsv/184960'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_4(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/nsupxlfy/298112'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/nsupxlfy/298112'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_5(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/rcnxsoxfb/450177'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/rcnxsoxfb/450177'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_6(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/vmeuvknrfi/615694'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/vmeuvknrfi/615694'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_7(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/tnyfb/338025'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/tnyfb/338025'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_8(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/rtkmws/546260'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/rtkmws/546260'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_9(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/ollrg/907546'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/ollrg/907546'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_10(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/mgalrg/144223'))
            df.close('finished')
            df2 = RFPDupeFilter(path)
            df2.open()
            seen = df2.request_seen(Request('http://scrapytest.org/mgalrg/144223'))
            df2.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/wnxqlrckoq/124090'))
            seen = df.request_seen(Request('http://scrapytest.org/wnxqlrckoq/124090'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_2(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/qwpldtenc/530973'))
            seen = df.request_seen(Request('http://scrapytest.org/qwpldtenc/530973'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_3(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/ymtukt/888801'))
            seen = df.request_seen(Request('http://scrapytest.org/ymtukt/888801'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_4(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/bgnoyjciz/98426'))
            seen = df.request_seen(Request('http://scrapytest.org/bgnoyjciz/98426'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_5(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/uhwydtkxd/505017'))
            seen = df.request_seen(Request('http://scrapytest.org/uhwydtkxd/505017'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_6(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/zfreozmgdz/38049'))
            seen = df.request_seen(Request('http://scrapytest.org/zfreozmgdz/38049'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_7(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/sgvi/372854'))
            seen = df.request_seen(Request('http://scrapytest.org/sgvi/372854'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_8(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/uzuur/798495'))
            seen = df.request_seen(Request('http://scrapytest.org/uzuur/798495'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_9(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/findbpoork/874082'))
            seen = df.request_seen(Request('http://scrapytest.org/findbpoork/874082'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

    def test_diversity_10(self):
        path = tempfile.mkdtemp()
        try:
            df = RFPDupeFilter(path)
            df.open()
            df.request_seen(Request('http://scrapytest.org/ynevkgk/287532'))
            seen = df.request_seen(Request('http://scrapytest.org/ynevkgk/287532'))
            df.close('finished')
            self.assertTrue(seen)
        finally:
            shutil.rmtree(path)

