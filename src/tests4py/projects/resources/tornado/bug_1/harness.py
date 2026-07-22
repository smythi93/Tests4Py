import sys

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.websocket import websocket_connect, WebSocketHandler
from tornado import gen

if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    io = tornado.ioloop.IOLoop()
    io.make_current()
    holder = {}

    class NoDelayHandler(WebSocketHandler):
        def open(self):
            self.set_nodelay(True)
            self.write_message(word)

    class PlainHandler(WebSocketHandler):
        def open(self):
            self.write_message(word)

    handler = NoDelayHandler if mode == "NODELAY" else PlainHandler

    @gen.coroutine
    def _main():
        app = tornado.web.Application([("/ws", handler)])
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        try:
            ws = yield websocket_connect("ws://127.0.0.1:%d/ws" % port)
            msg = yield ws.read_message()
            holder["out"] = msg if msg is not None else "ERROR:None"
        except Exception as e:
            holder["out"] = "ERROR:%s" % type(e).__name__

    io.run_sync(_main)
    print(holder["out"])
