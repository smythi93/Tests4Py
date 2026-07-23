import logging
import sys

# noinspection PyUnresolvedReferences
from twisted.python.failure import Failure

# noinspection PyUnresolvedReferences
from scrapy.spiders import Spider

# noinspection PyUnresolvedReferences
from scrapy.pipelines.media import MediaPipeline

# noinspection PyUnresolvedReferences
from scrapy.utils.log import failure_to_exc_info


def _mocked_download_func(request, info):
    return None


class _Capture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record)


if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    pipe = MediaPipeline(download_func=_mocked_download_func)
    spider = Spider("%s.com" % word)
    pipe.open_spider(spider)
    info = pipe.spiderinfo
    item = dict(name=word)
    handler = _Capture()
    logger = logging.getLogger("scrapy.pipelines.media")
    logger.addHandler(handler)
    old_level = logger.level
    logger.setLevel(logging.DEBUG)
    try:
        if mode == "fail":
            fail = Failure(Exception("boom %s" % word))
            results = [(True, 1), (False, fail)]
            pipe.item_completed(results, item, info)
            ok = (
                len(handler.records) == 1
                and handler.records[0].levelname == "ERROR"
                and handler.records[0].exc_info == failure_to_exc_info(fail)
            )
        else:
            results = [(True, 1), (True, 2)]
            pipe.item_completed(results, item, info)
            ok = len(handler.records) == 0
    finally:
        logger.removeHandler(handler)
        logger.setLevel(old_level)
    print("OK" if ok else "BAD")
