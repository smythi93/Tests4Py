import os
import sys
import tempfile

from tornado.web import Application, StaticFileHandler, HTTPError
from tornado.httputil import HTTPServerRequest, HTTPConnection


class _FakeConn(HTTPConnection):
    def set_close_callback(self, cb):
        pass


if __name__ == "__main__":
    rootname = sys.argv[1]
    reqpath = sys.argv[2]
    base = tempfile.mkdtemp()
    root = os.path.join(base, rootname)
    os.makedirs(root, exist_ok=True)
    app = Application()
    req = HTTPServerRequest(method="GET", uri="/x", connection=_FakeConn())
    handler = StaticFileHandler(app, req, path=root)
    handler.path = reqpath
    absolute_path = handler.get_absolute_path(root, reqpath)
    parent = os.path.dirname(absolute_path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)
    with open(absolute_path, "w") as fp:
        fp.write("data")
    try:
        handler.validate_absolute_path(root, absolute_path)
        print("OK")
    except HTTPError as e:
        print(e.status_code)
