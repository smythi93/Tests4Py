import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

if __name__ == "__main__":
    url = base64.urlsafe_b64decode(sys.argv[1].encode("ascii")).decode("utf-8")
    middleware = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
    try:
        creds, proxy = middleware._get_proxy(url, "http")
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + (creds.decode("ascii") if creds else "None"))
