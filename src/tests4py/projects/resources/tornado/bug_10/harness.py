import sys

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.websocket import websocket_connect, WebSocketHandler
from tornado.template import DictLoader
from tornado import gen

if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    io = tornado.ioloop.IOLoop()
    io.make_current()
    holder = {}

    class RenderHandler(WebSocketHandler):
        def on_message(self, message):
            self.write_message(self.render_string("message.html", message=message))

    class EchoHandler(WebSocketHandler):
        def on_message(self, message):
            self.write_message(message)

    handler = RenderHandler if mode == "RENDER" else EchoHandler

    @gen.coroutine
    def _main():
        app = tornado.web.Application(
            [("/ws", handler)],
            template_loader=DictLoader({"message.html": "<b>{{ message }}</b>"}),
        )
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        try:
            ws = yield websocket_connect("ws://127.0.0.1:%d/ws" % port)
            ws.write_message(word)
            msg = yield ws.read_message()
            holder["out"] = msg if msg is not None else "ERROR:None"
        except Exception as e:
            holder["out"] = "ERROR:%s" % type(e).__name__

    io.run_sync(_main)
    print(holder["out"])
