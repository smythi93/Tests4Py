import unittest

# noinspection PyUnresolvedReferences
import logging
from twisted.python.failure import Failure
from scrapy.spiders import Spider
from scrapy.pipelines.media import MediaPipeline
from scrapy.utils.log import failure_to_exc_info


class TestsFailing(unittest.TestCase):
    def _run(self, mode, word):

        def _mocked_download_func(request, info):
            return None

        class _Capture(logging.Handler):

            def __init__(self):
                super().__init__()
                self.records = []

            def emit(self, record):
                self.records.append(record)
        pipe = MediaPipeline(download_func=_mocked_download_func)
        spider = Spider('%s.com' % word)
        pipe.open_spider(spider)
        info = pipe.spiderinfo
        item = dict(name=word)
        handler = _Capture()
        logger = logging.getLogger('scrapy.pipelines.media')
        logger.addHandler(handler)
        old_level = logger.level
        logger.setLevel(logging.DEBUG)
        try:
            if mode == 'fail':
                fail = Failure(Exception('boom %s' % word))
                pipe.item_completed([(True, 1), (False, fail)], item, info)
                ok = len(handler.records) == 1 and handler.records[0].levelname == 'ERROR' and (handler.records[0].exc_info == failure_to_exc_info(fail))
            else:
                pipe.item_completed([(True, 1), (True, 2)], item, info)
                ok = len(handler.records) == 0
        finally:
            logger.removeHandler(handler)
            logger.setLevel(old_level)
        return 'OK' if ok else 'BAD'

    def test_diversity_1(self):
        self.assertEqual('OK', self._run('fail', 'oruw'))

    def test_diversity_2(self):
        self.assertEqual('OK', self._run('fail', 'czvxry'))

    def test_diversity_3(self):
        self.assertEqual('OK', self._run('fail', 'bxesisn'))

    def test_diversity_4(self):
        self.assertEqual('OK', self._run('fail', 'cywgj'))

    def test_diversity_5(self):
        self.assertEqual('OK', self._run('fail', 'jhclbp'))

    def test_diversity_6(self):
        self.assertEqual('OK', self._run('fail', 'wgwxkyua'))

    def test_diversity_7(self):
        self.assertEqual('OK', self._run('fail', 'jjy'))

    def test_diversity_8(self):
        self.assertEqual('OK', self._run('fail', 'lkolue'))

    def test_diversity_9(self):
        self.assertEqual('OK', self._run('fail', 'ewkr'))

    def test_diversity_10(self):
        self.assertEqual('OK', self._run('fail', 'gws'))


class TestsPassing(unittest.TestCase):
    def _run(self, mode, word):

        def _mocked_download_func(request, info):
            return None

        class _Capture(logging.Handler):

            def __init__(self):
                super().__init__()
                self.records = []

            def emit(self, record):
                self.records.append(record)
        pipe = MediaPipeline(download_func=_mocked_download_func)
        spider = Spider('%s.com' % word)
        pipe.open_spider(spider)
        info = pipe.spiderinfo
        item = dict(name=word)
        handler = _Capture()
        logger = logging.getLogger('scrapy.pipelines.media')
        logger.addHandler(handler)
        old_level = logger.level
        logger.setLevel(logging.DEBUG)
        try:
            if mode == 'fail':
                fail = Failure(Exception('boom %s' % word))
                pipe.item_completed([(True, 1), (False, fail)], item, info)
                ok = len(handler.records) == 1 and handler.records[0].levelname == 'ERROR' and (handler.records[0].exc_info == failure_to_exc_info(fail))
            else:
                pipe.item_completed([(True, 1), (True, 2)], item, info)
                ok = len(handler.records) == 0
        finally:
            logger.removeHandler(handler)
            logger.setLevel(old_level)
        return 'OK' if ok else 'BAD'

    def test_diversity_1(self):
        self.assertEqual('OK', self._run('success', 'swax'))

    def test_diversity_2(self):
        self.assertEqual('OK', self._run('success', 'ofoudjaw'))

    def test_diversity_3(self):
        self.assertEqual('OK', self._run('success', 'hqvbs'))

    def test_diversity_4(self):
        self.assertEqual('OK', self._run('success', 'rjhpuc'))

    def test_diversity_5(self):
        self.assertEqual('OK', self._run('success', 'plpruyc'))

    def test_diversity_6(self):
        self.assertEqual('OK', self._run('success', 'ylf'))

    def test_diversity_7(self):
        self.assertEqual('OK', self._run('success', 'palax'))

    def test_diversity_8(self):
        self.assertEqual('OK', self._run('success', 'nvdqg'))

    def test_diversity_9(self):
        self.assertEqual('OK', self._run('success', 'zeilj'))

    def test_diversity_10(self):
        self.assertEqual('OK', self._run('success', 'blfvjnn'))
