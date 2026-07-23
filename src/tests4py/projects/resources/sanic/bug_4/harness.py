import logging
import sys

logging.disable(logging.CRITICAL)

from sanic import Sanic
from sanic.request import Request
from sanic.compat import Header


class _Transport:
    def get_extra_info(self, key):
        if key == "sockname":
            return ("127.0.0.1", 8000)
        return None


if __name__ == "__main__":
    # argv: <server_or_dash> <path> <host_header>
    #   server_or_dash: a "host:port" SERVER_NAME, or "-" to leave it unset
    #   (the trigger); path is the target route path; host_header is the
    #   request Host header.  Calling request.url_for on a route requires
    #   reading app.config.SERVER_NAME; when SERVER_NAME is unset the buggy
    #   build raises AttributeError while the fixed build guards it.
    server_name = sys.argv[1]
    path = sys.argv[2]
    host_header = sys.argv[3]
    app = Sanic("t4p_sanic_bug4")
    if server_name != "-":
        app.config.SERVER_NAME = server_name
    app.add_route(lambda request: None, path, name="target")
    headers = Header()
    headers["Host"] = host_header
    req = Request(b"/sample", headers, "1.1", "GET", _Transport(), app)
    try:
        url = req.url_for("target")
        print("RESULT OK " + str(url))
    except Exception as e:
        print("RESULT ERR " + type(e).__name__)
