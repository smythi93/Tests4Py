import sys

import requests

from httpie.models import HTTPRequest


if __name__ == "__main__":
    # argv: url  host_header_name  host_header_value
    # host_header_name == "-" means "do not send a Host header".
    url = sys.argv[1]
    name = sys.argv[2]
    value = sys.argv[3]
    headers = {}
    if name != "-":
        headers[name] = value
    req = requests.Request("GET", url, headers=headers).prepare()
    print(HTTPRequest(req).headers)
