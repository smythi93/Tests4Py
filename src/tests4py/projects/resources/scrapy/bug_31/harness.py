import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.http import Request

# noinspection PyUnresolvedReferences
from scrapy.http.cookies import WrappedRequest

if __name__ == "__main__":
    value = base64.urlsafe_b64decode(sys.argv[1].encode("ascii"))
    request = Request("http://example.com", headers={b"X-Test": value})
    wrapped = WrappedRequest(request)
    try:
        result = wrapped.get_header("X-Test")
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + result)
