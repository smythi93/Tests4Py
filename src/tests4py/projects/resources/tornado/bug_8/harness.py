import sys

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.testing import bind_unused_port


class EchoHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, message):
        self.write_message(message)


SCENARIOS = {
    "MISSING_KEY": {
        "Connection": "Upgrade",
        "Upgrade": "WebSocket",
        "Sec-WebSocket-Version": "13",
    },
    "EMPTY_KEY": {
        "Connection": "Upgrade",
        "Upgrade": "WebSocket",
        "Sec-WebSocket-Version": "13",
        "Sec-WebSocket-Key": "",
    },
    "PLAIN": {},
    "BAD_VERSION": {
        "Connection": "Upgrade",
        "Upgrade": "WebSocket",
        "Sec-WebSocket-Version": "8",
        "Sec-WebSocket-Key": "abc",
    },
}


if __name__ == "__main__":
    scenario = sys.argv[1]
    headers = SCENARIOS[scenario]

    async def _run():
        app = tornado.web.Application([(r"/echo", EchoHandler)])
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        resp = await AsyncHTTPClient().fetch(
            HTTPRequest("http://127.0.0.1:%d/echo" % port, headers=headers),
            raise_error=False,
        )
        server.stop()
        return resp.code

    print(tornado.ioloop.IOLoop.current().run_sync(_run))
