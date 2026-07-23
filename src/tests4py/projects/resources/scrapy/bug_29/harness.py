import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.http import Request

# noinspection PyUnresolvedReferences
from scrapy.utils.request import request_httprepr

if __name__ == "__main__":
    url = base64.urlsafe_b64decode(sys.argv[1].encode("ascii")).decode("utf-8")
    try:
        result = request_httprepr(Request(url))
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + base64.urlsafe_b64encode(result).decode("ascii"))
