import logging
import sys

logging.disable(logging.CRITICAL)

from sanic import Sanic


if __name__ == "__main__":
    # argv: <mode> <host_or_dash> <path>
    #   mode is "ext" or "noext"; host_or_dash is a domain or "-" (no host);
    #   path is the route path (starts with "/").
    mode = sys.argv[1]
    host = sys.argv[2]
    path = sys.argv[3]
    app = Sanic("t4p_sanic_bug3")
    h = None if host == "-" else host
    app.add_route(lambda request: None, path, name="r", host=h)
    try:
        url = app.url_for("r", _external=(mode == "ext"))
        print("RESULT " + url)
    except Exception as e:
        print("ERROR " + type(e).__name__)
