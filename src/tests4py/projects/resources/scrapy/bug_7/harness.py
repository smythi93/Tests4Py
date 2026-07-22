import base64
import sys

# noinspection PyUnresolvedReferences
from scrapy.http import FormRequest, HtmlResponse

if __name__ == "__main__":
    base_url = base64.urlsafe_b64decode(sys.argv[1].encode("ascii")).decode("utf-8")
    action = base64.urlsafe_b64decode(sys.argv[2].encode("ascii")).decode("utf-8")
    body = '<html><body><form action="%s"></form></body></html>' % action
    response = HtmlResponse(url=base_url, body=body.encode("utf-8"), encoding="utf-8")
    try:
        request = FormRequest.from_response(response)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + request.url)
