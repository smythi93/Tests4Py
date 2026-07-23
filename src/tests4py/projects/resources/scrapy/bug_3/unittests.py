import unittest

from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
from scrapy.spiders import Spider
from scrapy.http import Request, Response
from scrapy.utils.test import get_crawler


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://vvtm.org/ii')
        rsp = Response('http://vvtm.org/ii', headers={'Location': '///awnfqjts.net/ianfyu'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://awnfqjts.net/ianfyu', result.url)

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://polcmdu.com/oomm')
        rsp = Response('http://polcmdu.com/oomm', headers={'Location': '///mibzmxre.org/rdep'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://mibzmxre.org/rdep', result.url)

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://wtfr.net/djobx')
        rsp = Response('http://wtfr.net/djobx', headers={'Location': '///xpy.net/fh'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://xpy.net/fh', result.url)

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://lwkwy.com/ctee')
        rsp = Response('http://lwkwy.com/ctee', headers={'Location': '///bnsb.org/ll'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://bnsb.org/ll', result.url)

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://lunkynib.net/hz')
        rsp = Response('http://lunkynib.net/hz', headers={'Location': '///lytncj.com/mcpcwk'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://lytncj.com/mcpcwk', result.url)

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://dntg.net/scwmda')
        rsp = Response('http://dntg.net/scwmda', headers={'Location': '///mapmvz.com/pkwzr'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://mapmvz.com/pkwzr', result.url)

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://gawbvftc.com/sy')
        rsp = Response('http://gawbvftc.com/sy', headers={'Location': '///zrsct.org/zot'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://zrsct.org/zot', result.url)

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://xek.com/bafd')
        rsp = Response('http://xek.com/bafd', headers={'Location': '///ozojhwwk.org/zai'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://ozojhwwk.org/zai', result.url)

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ashy.com/nrm')
        rsp = Response('http://ashy.com/nrm', headers={'Location': '///yidfub.org/kjn'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://yidfub.org/kjn', result.url)

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://wjj.net/eyr')
        rsp = Response('http://wjj.net/eyr', headers={'Location': '///dahnrxtl.com/cj'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://dahnrxtl.com/cj', result.url)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ftscdjy.org/vumrkh')
        rsp = Response('http://ftscdjy.org/vumrkh', headers={'Location': 'http://gps.net/qjcud'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://gps.net/qjcud', result.url)

    def test_diversity_2(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://has.net/zq')
        rsp = Response('http://has.net/zq', headers={'Location': 'http://qdboar.org/healq'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://qdboar.org/healq', result.url)

    def test_diversity_3(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://akcbfbf.org/dh')
        rsp = Response('http://akcbfbf.org/dh', headers={'Location': 'http://uvw.org/ikskpg'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://uvw.org/ikskpg', result.url)

    def test_diversity_4(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://agxlxxdj.com/la')
        rsp = Response('http://agxlxxdj.com/la', headers={'Location': 'http://rxxayjzs.com/esg'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://rxxayjzs.com/esg', result.url)

    def test_diversity_5(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://hanfps.com/abka')
        rsp = Response('http://hanfps.com/abka', headers={'Location': 'http://cuaw.net/hvi'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://cuaw.net/hvi', result.url)

    def test_diversity_6(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://oeuf.net/cb')
        rsp = Response('http://oeuf.net/cb', headers={'Location': 'http://alv.net/wb'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://alv.net/wb', result.url)

    def test_diversity_7(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://fiftcgbt.net/acgmug')
        rsp = Response('http://fiftcgbt.net/acgmug', headers={'Location': 'http://zmnnd.org/lb'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://zmnnd.org/lb', result.url)

    def test_diversity_8(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://ulca.org/zlwvij')
        rsp = Response('http://ulca.org/zlwvij', headers={'Location': 'http://tfj.net/zo'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://tfj.net/zo', result.url)

    def test_diversity_9(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://jxrfqz.org/idt')
        rsp = Response('http://jxrfqz.org/idt', headers={'Location': 'http://qhgpcuxi.com/qudun'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://qhgpcuxi.com/qudun', result.url)

    def test_diversity_10(self):
        crawler = get_crawler(Spider)
        spider = crawler._create_spider('foo')
        mw = RedirectMiddleware.from_crawler(crawler)
        req = Request('http://hdnzu.org/vat')
        rsp = Response('http://hdnzu.org/vat', headers={'Location': 'http://haqqd.org/yn'}, status=302)
        result = mw.process_response(req, rsp, spider)
        self.assertEqual('http://haqqd.org/yn', result.url)
