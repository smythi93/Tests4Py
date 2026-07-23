import sys

# noinspection PyUnresolvedReferences
from unittest import TextTestResult

# noinspection PyUnresolvedReferences
from twisted.python import failure

# noinspection PyUnresolvedReferences
from scrapy.spidermiddlewares.httperror import HttpError

# noinspection PyUnresolvedReferences
from scrapy.spiders import Spider

# noinspection PyUnresolvedReferences
from scrapy.http import Request

# noinspection PyUnresolvedReferences
from scrapy.contracts import ContractsManager

# noinspection PyUnresolvedReferences
from scrapy.contracts.default import UrlContract, ReturnsContract, ScrapesContract


def build(word):
    url = "http://%s.scrapy.org" % word

    class ResponseMock(object):
        pass

    resp = ResponseMock()
    resp.url = url

    class TestSpider(Spider):
        name = "demo_%s" % word

        def returns_request(self, response):
            """method which returns request
            @url http://scrapy.org
            @returns requests 1
            """
            return Request("http://scrapy.org")

        def raises_cb(self, response):
            """method whose callback raises
            @url http://scrapy.org
            """
            raise ValueError("boom %s" % word)

    conman = ContractsManager([UrlContract, ReturnsContract, ScrapesContract])
    results = TextTestResult(stream=None, descriptions=False, verbosity=0)
    return TestSpider(), conman, results, resp


if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    spider, conman, results, resp = build(word)
    raised = None
    if mode == "errback":
        try:
            raise HttpError(resp, "Ignoring non-200 response")
        except HttpError:
            failure_mock = failure.Failure()
        request = conman.from_method(spider.returns_request, results)
        try:
            request.errback(failure_mock)
        except Exception as exception:  # noqa: BLE001
            raised = type(exception).__name__
    else:
        request = conman.from_method(spider.raises_cb, results)
        try:
            request.callback(resp)
        except Exception as exception:  # noqa: BLE001
            raised = type(exception).__name__
    if raised:
        print("ERR:" + raised)
    else:
        print("OK:%d" % (1 if results.errors else 0))
