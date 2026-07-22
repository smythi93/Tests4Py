import unittest
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.testing import bind_unused_port
class _T4PEchoHandler(tornado.websocket.WebSocketHandler):

    def on_message(self, message):
        self.write_message(message)
_T4P_WS_SCENARIOS = {'MISSING_KEY': {'Connection': 'Upgrade', 'Upgrade': 'WebSocket', 'Sec-WebSocket-Version': '13'}, 'EMPTY_KEY': {'Connection': 'Upgrade', 'Upgrade': 'WebSocket', 'Sec-WebSocket-Version': '13', 'Sec-WebSocket-Key': ''}, 'PLAIN': {}, 'BAD_VERSION': {'Connection': 'Upgrade', 'Upgrade': 'WebSocket', 'Sec-WebSocket-Version': '8', 'Sec-WebSocket-Key': 'abc'}}
def run_ws(scenario, nonce=''):
    headers = _T4P_WS_SCENARIOS[scenario]

    async def _run():
        app = tornado.web.Application([('/echo', _T4PEchoHandler)])
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        resp = await AsyncHTTPClient().fetch(HTTPRequest('http://127.0.0.1:%d/echo' % port, headers=headers), raise_error=False)
        server.stop()
        return resp.code
    return tornado.ioloop.IOLoop.current().run_sync(_run)



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(400, run_ws('MISSING_KEY', 'uijmttn'))

    def test_diversity_2(self):
        self.assertEqual(400, run_ws('EMPTY_KEY', 'ctgr'))

    def test_diversity_3(self):
        self.assertEqual(400, run_ws('EMPTY_KEY', 'hbdgn'))

    def test_diversity_4(self):
        self.assertEqual(400, run_ws('EMPTY_KEY', 'uqaw'))

    def test_diversity_5(self):
        self.assertEqual(400, run_ws('MISSING_KEY', 'luqjm'))

    def test_diversity_6(self):
        self.assertEqual(400, run_ws('MISSING_KEY', 'khwjrtl'))

    def test_diversity_7(self):
        self.assertEqual(400, run_ws('EMPTY_KEY', 'uynkunp'))

    def test_diversity_8(self):
        self.assertEqual(400, run_ws('EMPTY_KEY', 'dmvr'))

    def test_diversity_9(self):
        self.assertEqual(400, run_ws('MISSING_KEY', 'krgoc'))

    def test_diversity_10(self):
        self.assertEqual(400, run_ws('MISSING_KEY', 'fwxpgvea'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(400, run_ws('PLAIN', 'xalscvc'))

    def test_diversity_2(self):
        self.assertEqual(400, run_ws('PLAIN', 'jbqtqdw'))

    def test_diversity_3(self):
        self.assertEqual(400, run_ws('PLAIN', 'kprj'))

    def test_diversity_4(self):
        self.assertEqual(400, run_ws('PLAIN', 'tiqa'))

    def test_diversity_5(self):
        self.assertEqual(400, run_ws('PLAIN', 'wzyjc'))

    def test_diversity_6(self):
        self.assertEqual(400, run_ws('PLAIN', 'vgvw'))

    def test_diversity_7(self):
        self.assertEqual(400, run_ws('PLAIN', 'lgduy'))

    def test_diversity_8(self):
        self.assertEqual(400, run_ws('PLAIN', 'chij'))

    def test_diversity_9(self):
        self.assertEqual(400, run_ws('PLAIN', 'wtzoou'))

    def test_diversity_10(self):
        self.assertEqual(400, run_ws('PLAIN', 'squihisn'))
