import unittest
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.web import RequestHandler
from tornado.auth import FacebookGraphMixin
from tornado import gen
class _T4PFacebookLogin(RequestHandler, FacebookGraphMixin):

    def initialize(self, base):
        self._OAUTH_AUTHORIZE_URL = base + '/facebook/server/authorize'
        self._OAUTH_ACCESS_TOKEN_URL = base + '/facebook/server/access_token'
        self._FACEBOOK_BASE_URL = base + '/facebook/server'

    @gen.coroutine
    def get(self):
        if self.get_argument('code', None):
            user = (yield self.get_authenticated_user(redirect_uri=self.request.full_url(), client_id=self.settings['facebook_api_key'], client_secret=self.settings['facebook_secret'], code=self.get_argument('code')))
            self.write(user)
        else:
            yield self.authorize_redirect(redirect_uri=self.request.full_url(), client_id=self.settings['facebook_api_key'], extra_params={'scope': 'read_stream'})
class _T4PAccessToken(RequestHandler):

    def get(self):
        self.write('access_token=asdf')
class _T4PMe(RequestHandler):

    def get(self):
        self.write('{}')
def run_facebook(mode, nonce=''):
    io = tornado.ioloop.IOLoop()
    io.make_current()
    holder = {}

    @gen.coroutine
    def _main():
        sock, port = bind_unused_port()
        base = 'http://127.0.0.1:%d' % port
        app = tornado.web.Application([('/facebook/client/login', _T4PFacebookLogin, dict(base=base)), ('/facebook/server/access_token', _T4PAccessToken), ('/facebook/server/me', _T4PMe)], facebook_api_key='test_key', facebook_secret='test_secret')
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        client = AsyncHTTPClient()
        suffix = '?code=1234' if mode == 'CODE' else ''
        url = base + '/facebook/client/login' + suffix
        resp = (yield client.fetch(HTTPRequest(url, follow_redirects=False, request_timeout=10), raise_error=False))
        holder['out'] = resp.code
    io.run_sync(_main)
    return holder['out']



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(200, run_facebook('CODE', 'mvogsqd'))

    def test_diversity_2(self):
        self.assertEqual(200, run_facebook('CODE', 'jltaagw'))

    def test_diversity_3(self):
        self.assertEqual(200, run_facebook('CODE', 'dfnqttzj'))

    def test_diversity_4(self):
        self.assertEqual(200, run_facebook('CODE', 'hhqj'))

    def test_diversity_5(self):
        self.assertEqual(200, run_facebook('CODE', 'godqlj'))

    def test_diversity_6(self):
        self.assertEqual(200, run_facebook('CODE', 'cftfflse'))

    def test_diversity_7(self):
        self.assertEqual(200, run_facebook('CODE', 'vfceu'))

    def test_diversity_8(self):
        self.assertEqual(200, run_facebook('CODE', 'pwke'))

    def test_diversity_9(self):
        self.assertEqual(200, run_facebook('CODE', 'rriojx'))

    def test_diversity_10(self):
        self.assertEqual(200, run_facebook('CODE', 'jkub'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'sgzr'))

    def test_diversity_2(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'tlbld'))

    def test_diversity_3(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'xnttdc'))

    def test_diversity_4(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'viithws'))

    def test_diversity_5(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'emrmer'))

    def test_diversity_6(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'miosc'))

    def test_diversity_7(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'ppjfli'))

    def test_diversity_8(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'tbtfbbqe'))

    def test_diversity_9(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'ewvwb'))

    def test_diversity_10(self):
        self.assertEqual(302, run_facebook('REDIRECT', 'tgdwr'))
