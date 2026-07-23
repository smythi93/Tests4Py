import unittest

# noinspection PyUnresolvedReferences
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
from scrapy.spiders import Spider
from scrapy.http import Request, Response
from scrapy.utils.test import get_crawler
from w3lib.url import safe_url_string
from six.moves.urllib.parse import urljoin


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/lbxkwg\xdfhq'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/uy\xc3\xa0ev'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/dp\xc3\xa0'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/cuyl\xc3\xb1'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/msuedn\xc2\xb5d'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/gnto\xf1snn'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/jnnel\xe9rfe'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/pwbwp\xe9gh'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/dlev\xdffiq'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/bxmy\xc3\xa9fa'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/aqn/kixc/mcy'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/zfdgtj/juqdtx'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/zdgv/jm/nmv'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/xlpmg/ve'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/akh/dbnfq/fjmm'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/ygb/ibkn'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/zc'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/dqbvc'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/uhxo/eyvk'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        loc = b'/xura/oi/lxyizo'
        rsp = Response('http://scrapytest.org/first', headers={'Location': loc}, status=302)
        result = mw.process_response(Request('http://scrapytest.org/first'), rsp, spider)
        self.assertEqual(urljoin('http://scrapytest.org/first', safe_url_string(loc)), result.url)
