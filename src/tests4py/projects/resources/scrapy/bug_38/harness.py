import sys
from urllib.parse import urlparse, parse_qs

# noinspection PyUnresolvedReferences
from scrapy.http import HtmlResponse, FormRequest

if __name__ == "__main__":
    # argv: expected clicktype t_name t_val c_name c_val  (expected is for oracle)
    clicktype = sys.argv[2]
    t_name, t_val, c_name, c_val = sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]
    body = (
        '<form><input type="text" name="%s" value="%s">'
        '<input type="%s" name="%s" value="%s"></form>'
        % (t_name, t_val, clicktype, c_name, c_val)
    )
    response = HtmlResponse(
        url="http://example.com", body=body.encode("utf-8"), encoding="utf-8"
    )
    req = FormRequest.from_response(response)
    params = parse_qs(urlparse(req.url).query)
    canon = "&".join("%s=%s" % (k, v) for k in sorted(params) for v in params[k])
    print(canon)
