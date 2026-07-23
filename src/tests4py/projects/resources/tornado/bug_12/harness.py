import sys

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.web import RequestHandler
from tornado.auth import FacebookGraphMixin
from tornado import gen


class FacebookClientLoginHandler(RequestHandler, FacebookGraphMixin):
    def initialize(self, base):
        self._OAUTH_AUTHORIZE_URL = base + "/facebook/server/authorize"
        self._OAUTH_ACCESS_TOKEN_URL = base + "/facebook/server/access_token"
        self._FACEBOOK_BASE_URL = base + "/facebook/server"

    @gen.coroutine
    def get(self):
        if self.get_argument("code", None):
            user = yield self.get_authenticated_user(
                redirect_uri=self.request.full_url(),
                client_id=self.settings["facebook_api_key"],
                client_secret=self.settings["facebook_secret"],
                code=self.get_argument("code"),
            )
            self.write(user)
        else:
            yield self.authorize_redirect(
                redirect_uri=self.request.full_url(),
                client_id=self.settings["facebook_api_key"],
                extra_params={"scope": "read_stream"},
            )


class AccessTokenHandler(RequestHandler):
    def get(self):
        self.write("access_token=asdf")


class MeHandler(RequestHandler):
    def get(self):
        self.write("{}")


if __name__ == "__main__":
    mode = sys.argv[1]
    io = tornado.ioloop.IOLoop()
    io.make_current()
    holder = {}

    @gen.coroutine
    def _main():
        sock, port = bind_unused_port()
        base = "http://127.0.0.1:%d" % port
        app = tornado.web.Application(
            [
                ("/facebook/client/login", FacebookClientLoginHandler, dict(base=base)),
                ("/facebook/server/access_token", AccessTokenHandler),
                ("/facebook/server/me", MeHandler),
            ],
            facebook_api_key="test_key",
            facebook_secret="test_secret",
        )
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        client = AsyncHTTPClient()
        suffix = "?code=1234" if mode == "CODE" else ""
        url = base + "/facebook/client/login" + suffix
        resp = yield client.fetch(
            HTTPRequest(url, follow_redirects=False, request_timeout=10),
            raise_error=False,
        )
        holder["out"] = resp.code

    io.run_sync(_main)
    print(holder["out"])
