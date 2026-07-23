import os
import sys
import tempfile

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.testing import bind_unused_port

if __name__ == "__main__":
    size = int(sys.argv[1])
    range_header = sys.argv[2]
    tmpdir = tempfile.mkdtemp()
    with open(os.path.join(tmpdir, "f.txt"), "wb") as fp:
        fp.write(b"A" * size)

    async def _run():
        app = tornado.web.Application(
            [(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": tmpdir})]
        )
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        client = AsyncHTTPClient()
        req = HTTPRequest(
            "http://127.0.0.1:%d/static/f.txt" % port,
            method="GET",
            headers={"Range": range_header},
        )
        resp = await client.fetch(req, raise_error=False)
        server.stop()
        return resp.code

    print(tornado.ioloop.IOLoop.current().run_sync(_run))
