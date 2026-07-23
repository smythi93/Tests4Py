import sys
import warnings

# noinspection PyUnresolvedReferences
from scrapy.spiders import Spider

# noinspection PyUnresolvedReferences
from scrapy.http import Request

if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    url = "http://%s.example.com" % word
    if mode == "override":
        class S(Spider):
            name = word
            start_urls = [url]

            def make_requests_from_url(self, u):
                return Request(u + "/foo", dont_filter=True)
    else:
        class S(Spider):
            name = word
            start_urls = [url]

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        reqs = list(S().start_requests())
    count = sum(1 for x in w if "make_requests_from_url" in str(x.message))
    print("OK:%d:%d" % (len(reqs), count))
