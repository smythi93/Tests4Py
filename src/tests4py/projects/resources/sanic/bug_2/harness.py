import logging
import sys

logging.disable(logging.CRITICAL)

from sanic.server import AsyncioServer


class _FakeServer:
    def __init__(self, token):
        self.token = token

    def start_serving(self):
        return "start_serving:" + self.token

    def serve_forever(self):
        return "serve_forever:" + self.token

    def is_serving(self):
        return "is_serving:" + self.token

    def wait_closed(self):
        return "wait_closed:" + self.token


if __name__ == "__main__":
    # argv: <method> <token>
    # Build an AsyncioServer wrapping a fake underlying server and invoke the
    # given method.  ``start_serving``/``serve_forever`` are missing on the
    # buggy build (AttributeError); ``is_serving``/``wait_closed`` exist on
    # both.  A present method delegates to the fake server and returns a
    # ``<method>:<token>`` sentinel.
    method = sys.argv[1]
    token = sys.argv[2]
    srv = AsyncioServer(None, None, set(), None, None, None)
    srv.server = _FakeServer(token)
    try:
        val = getattr(srv, method)()
        print("RESULT " + str(val))
    except Exception as e:
        print("RESULT ERR " + type(e).__name__)
