import unittest

# noinspection PyUnresolvedReferences
import warnings
from scrapy.spiders import Spider
from scrapy.http import Request


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        class S(Spider):
            name = 'oruw'
            start_urls = ['http://oruw.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_2(self):
        class S(Spider):
            name = 'czvxry'
            start_urls = ['http://czvxry.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_3(self):
        class S(Spider):
            name = 'bxesisn'
            start_urls = ['http://bxesisn.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_4(self):
        class S(Spider):
            name = 'cywgj'
            start_urls = ['http://cywgj.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_5(self):
        class S(Spider):
            name = 'jhclbp'
            start_urls = ['http://jhclbp.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_6(self):
        class S(Spider):
            name = 'wgwxkyua'
            start_urls = ['http://wgwxkyua.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_7(self):
        class S(Spider):
            name = 'jjy'
            start_urls = ['http://jjy.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_8(self):
        class S(Spider):
            name = 'lkolue'
            start_urls = ['http://lkolue.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_9(self):
        class S(Spider):
            name = 'ewkr'
            start_urls = ['http://ewkr.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)

    def test_diversity_10(self):
        class S(Spider):
            name = 'gws'
            start_urls = ['http://gws.example.com']
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(0, count)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        class S(Spider):
            name = 'swax'
            start_urls = ['http://swax.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_2(self):
        class S(Spider):
            name = 'ofoudjaw'
            start_urls = ['http://ofoudjaw.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_3(self):
        class S(Spider):
            name = 'hqvbs'
            start_urls = ['http://hqvbs.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_4(self):
        class S(Spider):
            name = 'rjhpuc'
            start_urls = ['http://rjhpuc.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_5(self):
        class S(Spider):
            name = 'plpruyc'
            start_urls = ['http://plpruyc.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_6(self):
        class S(Spider):
            name = 'ylf'
            start_urls = ['http://ylf.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_7(self):
        class S(Spider):
            name = 'palax'
            start_urls = ['http://palax.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_8(self):
        class S(Spider):
            name = 'nvdqg'
            start_urls = ['http://nvdqg.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_9(self):
        class S(Spider):
            name = 'zeilj'
            start_urls = ['http://zeilj.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)

    def test_diversity_10(self):
        class S(Spider):
            name = 'blfvjnn'
            start_urls = ['http://blfvjnn.example.com']
        
            def make_requests_from_url(self, u):
                return Request(u + '/foo', dont_filter=True)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            reqs = list(S().start_requests())
        count = sum((1 for x in w if 'make_requests_from_url' in str(x.message)))
        self.assertEqual(1, len(reqs))
        self.assertEqual(1, count)
