import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.utils.url import canonicalize_url

if __name__ == "__main__":
    url = base64.urlsafe_b64decode(sys.argv[1].encode("ascii")).decode("utf-8")
    try:
        result = canonicalize_url(url)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + result)
