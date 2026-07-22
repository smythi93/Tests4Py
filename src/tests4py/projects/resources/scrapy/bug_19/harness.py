import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.http import Request

# noinspection PyUnresolvedReferences
from scrapy.http.cookies import WrappedRequest

if __name__ == "__main__":
    attr = sys.argv[1]
    url = base64.urlsafe_b64decode(sys.argv[2].encode("ascii")).decode("utf-8")
    wrapped = WrappedRequest(Request(url))
    try:
        value = getattr(wrapped, attr)
        if callable(value):
            value = value()
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + str(value))
