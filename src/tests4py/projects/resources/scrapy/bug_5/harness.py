import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.http import Response

if __name__ == "__main__":
    mode = sys.argv[1]
    base = base64.urlsafe_b64decode(sys.argv[2].encode("ascii")).decode("utf-8")
    if mode == "none":
        target = None
    else:
        target = base64.urlsafe_b64decode(sys.argv[3].encode("ascii")).decode("utf-8")
    response = Response(url=base)
    try:
        request = response.follow(target)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + request.url)
