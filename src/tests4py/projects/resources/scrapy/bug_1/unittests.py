import unittest

# noinspection PyUnresolvedReferences
from scrapy.spidermiddlewares.offsite import OffsiteMiddleware
from scrapy.spiders import Spider
from scrapy.utils.test import get_crawler


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['jhclbp.io', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('jhclbp.io'))
        self.assertTrue(regex.search('sub.' + 'jhclbp.io'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['tyig.com', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('tyig.com'))
        self.assertTrue(regex.search('sub.' + 'tyig.com'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['adqe.com', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('adqe.com'))
        self.assertTrue(regex.search('sub.' + 'adqe.com'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['lkolue.org', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('lkolue.org'))
        self.assertTrue(regex.search('sub.' + 'lkolue.org'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['nvlc.net', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('nvlc.net'))
        self.assertTrue(regex.search('sub.' + 'nvlc.net'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['geuppqof.io', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('geuppqof.io'))
        self.assertTrue(regex.search('sub.' + 'geuppqof.io'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['wgqy.net', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('wgqy.net'))
        self.assertTrue(regex.search('sub.' + 'wgqy.net'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['nxauy.io', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('nxauy.io'))
        self.assertTrue(regex.search('sub.' + 'nxauy.io'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['sevhtdpl.net', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('sevhtdpl.net'))
        self.assertTrue(regex.search('sub.' + 'sevhtdpl.net'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['cuylf.net', None]
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('cuylf.net'))
        self.assertTrue(regex.search('sub.' + 'cuylf.net'))
        self.assertFalse(regex.search('evil.com'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['msuednv.com']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('msuednv.com'))
        self.assertTrue(regex.search('sub.' + 'msuednv.com'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['wizeiljz.com']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('wizeiljz.com'))
        self.assertTrue(regex.search('sub.' + 'wizeiljz.com'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['lfvjnne.io']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('lfvjnne.io'))
        self.assertTrue(regex.search('sub.' + 'lfvjnne.io'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['brfebp.com']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('brfebp.com'))
        self.assertTrue(regex.search('sub.' + 'brfebp.com'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['wpcghphp.org']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('wpcghphp.org'))
        self.assertTrue(regex.search('sub.' + 'wpcghphp.org'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['vrfiqbh.org']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('vrfiqbh.org'))
        self.assertTrue(regex.search('sub.' + 'vrfiqbh.org'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['tcjagr.org']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('tcjagr.org'))
        self.assertTrue(regex.search('sub.' + 'tcjagr.org'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['rgw.io']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('rgw.io'))
        self.assertTrue(regex.search('sub.' + 'rgw.io'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['ixc.org']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('ixc.org'))
        self.assertTrue(regex.search('sub.' + 'ixc.org'))
        self.assertFalse(regex.search('evil.com'))

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        mw = OffsiteMiddleware.from_crawler(crawler)
        spider = crawler._create_spider('foo')
        spider.allowed_domains = ['mfttzf.com']
        regex = mw.get_host_regex(spider)
        self.assertTrue(regex.search('mfttzf.com'))
        self.assertTrue(regex.search('sub.' + 'mfttzf.com'))
        self.assertFalse(regex.search('evil.com'))
