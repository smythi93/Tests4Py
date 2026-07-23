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

# noinspection PyUnresolvedReferences
from w3lib.url import safe_url_string

# noinspection PyUnresolvedReferences
from six.moves.urllib.parse import urljoin

if __name__ == "__main__":
    location = base64.urlsafe_b64decode(sys.argv[1].encode("ascii"))
    url = "http://scrapytest.org/first"
    crawler = get_crawler(Spider)
    spider = crawler._create_spider("foo")
    mw = RedirectMiddleware.from_crawler(crawler)
    request = Request(url)
    response = Response(url, headers={"Location": location}, status=302)
    try:
        result = mw.process_response(request, response, spider)
        actual = result.url
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        expected = urljoin(url, safe_url_string(location))
        print("MATCH" if actual == expected else "NOMATCH:" + actual)
