import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.responsetypes import responsetypes

if __name__ == "__main__":
    content_disposition = base64.urlsafe_b64decode(sys.argv[1].encode("ascii"))
    try:
        cls = responsetypes.from_content_disposition(content_disposition)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + cls.__name__)
