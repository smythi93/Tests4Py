import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.http import Request

if __name__ == "__main__":
    mode = sys.argv[1]
    url = base64.urlsafe_b64decode(sys.argv[2].encode("ascii")).decode("utf-8")
    try:
        request = Request(url)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + request.url)
