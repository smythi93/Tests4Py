import sys

# noinspection PyUnresolvedReferences
from scrapy.http import HtmlResponse, FormRequest

if __name__ == "__main__":
    # argv: expected response_url base_href action   (expected is for the oracle)
    response_url = sys.argv[2]
    base_href = sys.argv[3]
    action = sys.argv[4]
    base_tag = "" if base_href == "none" else '<base href="%s">' % base_href
    body = (
        "<html><head>%s</head><body>"
        '<form action="%s"></form></body></html>' % (base_tag, action)
    )
    response = HtmlResponse(url=response_url, body=body.encode("utf-8"), encoding="utf-8")
    req = FormRequest.from_response(response)
    print(req.url)
