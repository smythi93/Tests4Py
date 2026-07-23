import unittest

# noinspection PyUnresolvedReferences
from unittest import TextTestResult
from twisted.python import failure
from scrapy.spidermiddlewares.httperror import HttpError
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.contracts import ContractsManager
from scrapy.contracts.default import UrlContract, ReturnsContract, ScrapesContract


class TestsFailing(unittest.TestCase):
    def _run(self, mode, word):
        url = 'http://%s.scrapy.org' % word

        class ResponseMock(object):
            pass
        resp = ResponseMock()
        resp.url = url

        class TestSpider(Spider):
            name = 'demo_%s' % word

            def returns_request(self, response):
                """method which returns request
                @url http://scrapy.org
                @returns requests 1
                """
                return Request('http://scrapy.org')

            def raises_cb(self, response):
                """method whose callback raises
                @url http://scrapy.org
                """
                raise ValueError('boom')
        conman = ContractsManager([UrlContract, ReturnsContract, ScrapesContract])
        results = TextTestResult(stream=None, descriptions=False, verbosity=0)
        spider = TestSpider()
        if mode == 'errback':
            try:
                raise HttpError(resp, 'Ignoring non-200 response')
            except HttpError:
                fm = failure.Failure()
            request = conman.from_method(spider.returns_request, results)
            request.errback(fm)
        else:
            request = conman.from_method(spider.raises_cb, results)
            request.callback(resp)
        return 'OK:%d' % (1 if results.errors else 0)

    def test_diversity_1(self):
        self.assertEqual('OK:1', self._run('errback', 'oruw'))

    def test_diversity_2(self):
        self.assertEqual('OK:1', self._run('errback', 'czvxry'))

    def test_diversity_3(self):
        self.assertEqual('OK:1', self._run('errback', 'bxesisn'))

    def test_diversity_4(self):
        self.assertEqual('OK:1', self._run('errback', 'cywgj'))

    def test_diversity_5(self):
        self.assertEqual('OK:1', self._run('errback', 'jhclbp'))

    def test_diversity_6(self):
        self.assertEqual('OK:1', self._run('errback', 'wgwxkyua'))

    def test_diversity_7(self):
        self.assertEqual('OK:1', self._run('errback', 'jjy'))

    def test_diversity_8(self):
        self.assertEqual('OK:1', self._run('errback', 'lkolue'))

    def test_diversity_9(self):
        self.assertEqual('OK:1', self._run('errback', 'ewkr'))

    def test_diversity_10(self):
        self.assertEqual('OK:1', self._run('errback', 'gws'))


class TestsPassing(unittest.TestCase):
    def _run(self, mode, word):
        url = 'http://%s.scrapy.org' % word

        class ResponseMock(object):
            pass
        resp = ResponseMock()
        resp.url = url

        class TestSpider(Spider):
            name = 'demo_%s' % word

            def returns_request(self, response):
                """method which returns request
                @url http://scrapy.org
                @returns requests 1
                """
                return Request('http://scrapy.org')

            def raises_cb(self, response):
                """method whose callback raises
                @url http://scrapy.org
                """
                raise ValueError('boom')
        conman = ContractsManager([UrlContract, ReturnsContract, ScrapesContract])
        results = TextTestResult(stream=None, descriptions=False, verbosity=0)
        spider = TestSpider()
        if mode == 'errback':
            try:
                raise HttpError(resp, 'Ignoring non-200 response')
            except HttpError:
                fm = failure.Failure()
            request = conman.from_method(spider.returns_request, results)
            request.errback(fm)
        else:
            request = conman.from_method(spider.raises_cb, results)
            request.callback(resp)
        return 'OK:%d' % (1 if results.errors else 0)

    def test_diversity_1(self):
        self.assertEqual('OK:1', self._run('callback', 'swax'))

    def test_diversity_2(self):
        self.assertEqual('OK:1', self._run('callback', 'ofoudjaw'))

    def test_diversity_3(self):
        self.assertEqual('OK:1', self._run('callback', 'hqvbs'))

    def test_diversity_4(self):
        self.assertEqual('OK:1', self._run('callback', 'rjhpuc'))

    def test_diversity_5(self):
        self.assertEqual('OK:1', self._run('callback', 'plpruyc'))

    def test_diversity_6(self):
        self.assertEqual('OK:1', self._run('callback', 'ylf'))

    def test_diversity_7(self):
        self.assertEqual('OK:1', self._run('callback', 'palax'))

    def test_diversity_8(self):
        self.assertEqual('OK:1', self._run('callback', 'nvdqg'))

    def test_diversity_9(self):
        self.assertEqual('OK:1', self._run('callback', 'zeilj'))

    def test_diversity_10(self):
        self.assertEqual('OK:1', self._run('callback', 'blfvjnn'))
