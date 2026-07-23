import sys

# noinspection PyUnresolvedReferences
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware

# noinspection PyUnresolvedReferences
from scrapy.http import Request, Response

# noinspection PyUnresolvedReferences
from scrapy.spiders import Spider

# noinspection PyUnresolvedReferences
from scrapy.utils.test import get_crawler

if __name__ == "__main__":
    mode = sys.argv[1]
    status = int(sys.argv[2])
    word = sys.argv[3]
    url = "http://%s.example.com/%d" % (word, status)
    url2 = "http://%s.example.com/redirected" % word
    crawler = get_crawler(Spider)
    spider = crawler._create_spider("foo")
    mw = RedirectMiddleware.from_crawler(crawler)
    meta = {}
    if mode == "list":
        meta = {"handle_httpstatus_list": [status]}
    elif mode == "all":
        meta = {"handle_httpstatus_all": True}
    elif mode == "dont":
        meta = {"dont_redirect": True}
    elif mode == "spiderlist":
        spider.handle_httpstatus_list = [status]
    request = Request(url, meta=meta)
    response = Response(url, headers={"Location": url2}, status=status, request=request)
    try:
        result = mw.process_response(request, response, spider)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("SAME" if result is response else "REDIRECT")
