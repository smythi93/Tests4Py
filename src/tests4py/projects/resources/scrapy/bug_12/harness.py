import sys

# noinspection PyUnresolvedReferences
from scrapy.selector import Selector

# noinspection PyUnresolvedReferences
from scrapy.http import TextResponse

if __name__ == "__main__":
    mode = sys.argv[1]
    html = sys.argv[2]
    resp = TextResponse(
        url="http://example.com", body=html.encode("utf-8"), encoding="utf-8"
    )
    try:
        if mode == "both":
            Selector(response=resp, text=html, type="html")
        elif mode == "text":
            Selector(text=html, type="html")
        else:  # "response"
            Selector(response=resp, type="html")
        result = "NOERROR"
    except ValueError:
        result = "VALUEERROR"
    except Exception as exc:  # pragma: no cover
        result = "OTHER:" + type(exc).__name__
    print(result)
