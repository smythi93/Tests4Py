import logging
import sys

logging.disable(logging.CRITICAL)

from sanic import Sanic


def _make_mw(i):
    def mw(request, response=None):
        return None

    mw.idx = i
    return mw


if __name__ == "__main__":
    # argv: <kind> <n>
    # kind is "request" or "response"; register n named middleware of that
    # kind on a single route and print the resulting deque order (by index).
    kind = sys.argv[1]
    n = int(sys.argv[2])
    app = Sanic("t4p_sanic_bug1_" + kind + "_" + str(n))
    for i in range(n):
        app.register_named_middleware(_make_mw(i), ["route"], attach_to=kind)
    if kind == "response":
        dq = app.named_response_middleware.get("route")
    else:
        dq = app.named_request_middleware.get("route")
    order = [m.idx for m in dq] if dq else []
    print("RESULT " + " ".join(str(x) for x in order))
