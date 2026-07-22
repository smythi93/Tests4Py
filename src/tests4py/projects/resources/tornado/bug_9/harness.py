import sys

from tornado.httputil import url_concat

NONE_TOKEN = "__NONE__"

if __name__ == "__main__":
    url = sys.argv[1]
    tokens = sys.argv[2:]
    if tokens == [NONE_TOKEN]:
        args = None
    else:
        args = [tuple(t.split("=", 1)) for t in tokens]
    try:
        print(url_concat(url, args))
    except Exception:
        print("ERROR")
