import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.http import TextResponse

# noinspection PyUnresolvedReferences
from scrapy.spiders import SitemapSpider

if __name__ == "__main__":
    mode = sys.argv[1]
    robots_url = base64.urlsafe_b64decode(sys.argv[2].encode("ascii")).decode("utf-8")
    body = b"" if mode == "empty" else base64.urlsafe_b64decode(
        sys.argv[3].encode("ascii")
    )
    spider = SitemapSpider.__new__(SitemapSpider)
    response = TextResponse(url=robots_url, body=body, encoding="utf-8")
    try:
        urls = [request.url for request in spider._parse_sitemap(response)]
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + ",".join(urls))
