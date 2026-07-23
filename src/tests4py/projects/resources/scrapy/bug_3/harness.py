import base64
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
    request_url = base64.urlsafe_b64decode(sys.argv[2].encode("ascii")).decode("utf-8")
    location = base64.urlsafe_b64decode(sys.argv[3].encode("ascii")).decode("utf-8")
    crawler = get_crawler(Spider)
    spider = crawler._create_spider("foo")
    middleware = RedirectMiddleware.from_crawler(crawler)
    request = Request(request_url)
    response = Response(request_url, headers={"Location": location}, status=302)
    try:
        result = middleware.process_response(request, response, spider)
        url = result.url
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + url)
