import sys

# noinspection PyUnresolvedReferences
from scrapy.spidermiddlewares.offsite import OffsiteMiddleware

# noinspection PyUnresolvedReferences
from scrapy.spiders import Spider

# noinspection PyUnresolvedReferences
from scrapy.utils.test import get_crawler

if __name__ == "__main__":
    mode = sys.argv[1]
    domain = sys.argv[2]
    crawler = get_crawler(Spider)
    mw = OffsiteMiddleware.from_crawler(crawler)
    spider = crawler._create_spider("foo")
    if mode == "none":
        spider.allowed_domains = [domain, None]
    else:
        spider.allowed_domains = [domain]
    try:
        regex = mw.get_host_regex(spider)
        m1 = bool(regex.search(domain))
        m2 = bool(regex.search("sub." + domain))
        m3 = bool(regex.search("evil.com"))
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:%d%d%d" % (m1, m2, m3))
