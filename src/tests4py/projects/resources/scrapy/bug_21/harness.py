import sys
from unittest import mock

# noinspection PyUnresolvedReferences
from twisted.internet import error

# noinspection PyUnresolvedReferences
from twisted.internet.defer import Deferred

# noinspection PyUnresolvedReferences
from twisted.python import failure

# noinspection PyUnresolvedReferences
from scrapy.downloadermiddlewares.robotstxt import RobotsTxtMiddleware

# noinspection PyUnresolvedReferences
from scrapy.http import Request

# noinspection PyUnresolvedReferences
from scrapy.settings import Settings

if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    crawler = mock.MagicMock()
    crawler.settings = Settings()
    crawler.settings.set("ROBOTSTXT_OBEY", True)
    crawler.engine.download = mock.MagicMock()
    if mode == "immediate":
        err = error.DNSLookupError("Robotstxt address not found")

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
        mw.robot_parser(Request("http://%s.local" % word), spider)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK")
