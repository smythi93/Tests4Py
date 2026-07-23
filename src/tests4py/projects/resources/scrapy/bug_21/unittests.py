import unittest

# noinspection PyUnresolvedReferences
from unittest import mock
from twisted.internet import error
from twisted.internet.defer import Deferred
from twisted.python import failure
from scrapy.downloadermiddlewares.robotstxt import RobotsTxtMiddleware
from scrapy.http import Request
from scrapy.settings import Settings


class TestsFailing(unittest.TestCase):
    def _run(self, mode, word):
        crawler = mock.MagicMock()
        crawler.settings = Settings()
        crawler.settings.set('ROBOTSTXT_OBEY', True)
        crawler.engine.download = mock.MagicMock()
        if mode == 'immediate':
            err = error.DNSLookupError('Robotstxt address not found')

            def side(request, spider):
                d = Deferred()
                d.errback(failure.Failure(err))
                return d
        else:

            def side(request, spider):
                return Deferred()
        crawler.engine.download.side_effect = side
        mw = RobotsTxtMiddleware(crawler)
        spider = mock.MagicMock()
        try:
            mw.robot_parser(Request('http://%s.local' % word), spider)
        except Exception as exc:
            return 'ERR:' + type(exc).__name__
        return 'OK'

    def test_diversity_1(self):
        self.assertEqual('OK', self._run('immediate', 'oruw'))

    def test_diversity_2(self):
        self.assertEqual('OK', self._run('immediate', 'czvxry'))

    def test_diversity_3(self):
        self.assertEqual('OK', self._run('immediate', 'bxesisn'))

    def test_diversity_4(self):
        self.assertEqual('OK', self._run('immediate', 'cywgj'))

    def test_diversity_5(self):
        self.assertEqual('OK', self._run('immediate', 'jhclbp'))

    def test_diversity_6(self):
        self.assertEqual('OK', self._run('immediate', 'wgwxkyua'))

    def test_diversity_7(self):
        self.assertEqual('OK', self._run('immediate', 'jjy'))

    def test_diversity_8(self):
        self.assertEqual('OK', self._run('immediate', 'lkolue'))

    def test_diversity_9(self):
        self.assertEqual('OK', self._run('immediate', 'ewkr'))

    def test_diversity_10(self):
        self.assertEqual('OK', self._run('immediate', 'gws'))


class TestsPassing(unittest.TestCase):
    def _run(self, mode, word):
        crawler = mock.MagicMock()
        crawler.settings = Settings()
        crawler.settings.set('ROBOTSTXT_OBEY', True)
        crawler.engine.download = mock.MagicMock()
        if mode == 'immediate':
            err = error.DNSLookupError('Robotstxt address not found')

            def side(request, spider):
                d = Deferred()
                d.errback(failure.Failure(err))
                return d
        else:

            def side(request, spider):
                return Deferred()
        crawler.engine.download.side_effect = side
        mw = RobotsTxtMiddleware(crawler)
        spider = mock.MagicMock()
        try:
            mw.robot_parser(Request('http://%s.local' % word), spider)
        except Exception as exc:
            return 'ERR:' + type(exc).__name__
        return 'OK'

    def test_diversity_1(self):
        self.assertEqual('OK', self._run('pending', 'swax'))

    def test_diversity_2(self):
        self.assertEqual('OK', self._run('pending', 'ofoudjaw'))

    def test_diversity_3(self):
        self.assertEqual('OK', self._run('pending', 'hqvbs'))

    def test_diversity_4(self):
        self.assertEqual('OK', self._run('pending', 'rjhpuc'))

    def test_diversity_5(self):
        self.assertEqual('OK', self._run('pending', 'plpruyc'))

    def test_diversity_6(self):
        self.assertEqual('OK', self._run('pending', 'ylf'))

    def test_diversity_7(self):
        self.assertEqual('OK', self._run('pending', 'palax'))

    def test_diversity_8(self):
        self.assertEqual('OK', self._run('pending', 'nvdqg'))

    def test_diversity_9(self):
        self.assertEqual('OK', self._run('pending', 'zeilj'))

    def test_diversity_10(self):
        self.assertEqual('OK', self._run('pending', 'blfvjnn'))
