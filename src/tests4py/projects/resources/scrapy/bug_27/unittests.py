import unittest

# noinspection PyUnresolvedReferences
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
from scrapy.spiders import Spider
from scrapy.http import Request, Response
from scrapy.utils.test import get_crawler


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ejfugm.example.com/307', meta={'handle_httpstatus_list': [307]})
        rsp = Response('http://ejfugm.example.com/307', headers={'Location': 'http://ejfugm.example.com/redirected'}, status=307, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://rcwwge.example.com/307', meta={'handle_httpstatus_list': [307]})
        rsp = Response('http://rcwwge.example.com/307', headers={'Location': 'http://rcwwge.example.com/redirected'}, status=307, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://bxkw.example.com/307', meta={'handle_httpstatus_list': [307]})
        rsp = Response('http://bxkw.example.com/307', headers={'Location': 'http://bxkw.example.com/redirected'}, status=307, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://wyhqvbsy.example.com/301', meta={'handle_httpstatus_list': [301]})
        rsp = Response('http://wyhqvbsy.example.com/301', headers={'Location': 'http://wyhqvbsy.example.com/redirected'}, status=301, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://vhtdp.example.com/302', meta={'handle_httpstatus_all': True})
        rsp = Response('http://vhtdp.example.com/302', headers={'Location': 'http://vhtdp.example.com/redirected'}, status=302, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://wrhheca.example.com/301', meta={'handle_httpstatus_all': True})
        rsp = Response('http://wrhheca.example.com/301', headers={'Location': 'http://wrhheca.example.com/redirected'}, status=301, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://palax.example.com/301', meta={'handle_httpstatus_list': [301]})
        rsp = Response('http://palax.example.com/301', headers={'Location': 'http://palax.example.com/redirected'}, status=301, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://vwi.example.com/302', meta={'handle_httpstatus_all': True})
        rsp = Response('http://vwi.example.com/302', headers={'Location': 'http://vwi.example.com/redirected'}, status=302, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ljzblfv.example.com/303', meta={'handle_httpstatus_list': [303]})
        rsp = Response('http://ljzblfv.example.com/303', headers={'Location': 'http://ljzblfv.example.com/redirected'}, status=303, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://oklz.example.com/303', meta={'handle_httpstatus_all': True})
        rsp = Response('http://oklz.example.com/303', headers={'Location': 'http://oklz.example.com/redirected'}, status=303, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://mpo.example.com/302', meta={'dont_redirect': True})
        rsp = Response('http://mpo.example.com/302', headers={'Location': 'http://mpo.example.com/redirected'}, status=302, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        spider.handle_httpstatus_list = [303]
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://hoc.example.com/303', meta={})
        rsp = Response('http://hoc.example.com/303', headers={'Location': 'http://hoc.example.com/redirected'}, status=303, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://pzo.example.com/303', meta={'dont_redirect': True})
        rsp = Response('http://pzo.example.com/303', headers={'Location': 'http://pzo.example.com/redirected'}, status=303, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        spider.handle_httpstatus_list = [307]
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ctlt.example.com/307', meta={})
        rsp = Response('http://ctlt.example.com/307', headers={'Location': 'http://ctlt.example.com/redirected'}, status=307, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://tcjagr.example.com/302', meta={'dont_redirect': True})
        rsp = Response('http://tcjagr.example.com/302', headers={'Location': 'http://tcjagr.example.com/redirected'}, status=302, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://qnicbdsd.example.com/301', meta={'dont_redirect': True})
        rsp = Response('http://qnicbdsd.example.com/301', headers={'Location': 'http://qnicbdsd.example.com/redirected'}, status=301, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        spider.handle_httpstatus_list = [301]
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ykoc.example.com/301', meta={})
        rsp = Response('http://ykoc.example.com/301', headers={'Location': 'http://ykoc.example.com/redirected'}, status=301, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://gtjp.example.com/301', meta={'dont_redirect': True})
        rsp = Response('http://gtjp.example.com/301', headers={'Location': 'http://gtjp.example.com/redirected'}, status=301, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        spider.handle_httpstatus_list = [301]
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ydptvshp.example.com/301', meta={})
        rsp = Response('http://ydptvshp.example.com/301', headers={'Location': 'http://ydptvshp.example.com/redirected'}, status=301, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://vck.example.com/303', meta={'dont_redirect': True})
        rsp = Response('http://vck.example.com/303', headers={'Location': 'http://vck.example.com/redirected'}, status=303, request=req)
        self.assertIs(rsp, mw.process_response(req, rsp, spider))
