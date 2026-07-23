import unittest
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.websocket import websocket_connect, WebSocketHandler
from tornado import gen
def run_nodelay(mode, word):
    io = tornado.ioloop.IOLoop()
    io.make_current()
    holder = {}

    class _NoDelay(WebSocketHandler):

        def open(self):
            self.set_nodelay(True)
            self.write_message(word)

    class _Plain(WebSocketHandler):

        def open(self):
            self.write_message(word)
    handler = _NoDelay if mode == 'NODELAY' else _Plain

    @gen.coroutine
    def _main():
        app = tornado.web.Application([('/ws', handler)])
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        try:
            ws = (yield websocket_connect('ws://127.0.0.1:%d/ws' % port))
            msg = (yield ws.read_message())
            holder['out'] = msg if msg is not None else 'ERROR:None'
        except Exception as e:
            holder['out'] = 'ERROR:%s' % type(e).__name__
    io.run_sync(_main)
    return holder['out']



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('fsss', run_nodelay('NODELAY', 'fsss'))

    def test_diversity_2(self):
        self.assertEqual('hxm', run_nodelay('NODELAY', 'hxm'))

    def test_diversity_3(self):
        self.assertEqual('mckqan', run_nodelay('NODELAY', 'mckqan'))

    def test_diversity_4(self):
        self.assertEqual('ohomzjbp', run_nodelay('NODELAY', 'ohomzjbp'))

    def test_diversity_5(self):
        self.assertEqual('qxrayvrh', run_nodelay('NODELAY', 'qxrayvrh'))

    def test_diversity_6(self):
        self.assertEqual('shwarbco', run_nodelay('NODELAY', 'shwarbco'))

    def test_diversity_7(self):
        self.assertEqual('oefjogwjfd', run_nodelay('NODELAY', 'oefjogwjfd'))

    def test_diversity_8(self):
        self.assertEqual('socvemcl', run_nodelay('NODELAY', 'socvemcl'))

    def test_diversity_9(self):
        self.assertEqual('pmtrjqilz', run_nodelay('NODELAY', 'pmtrjqilz'))

    def test_diversity_10(self):
        self.assertEqual('vbutsuis', run_nodelay('NODELAY', 'vbutsuis'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('ekyae', run_nodelay('PLAIN', 'ekyae'))

    def test_diversity_2(self):
        self.assertEqual('vugrwevc', run_nodelay('PLAIN', 'vugrwevc'))

    def test_diversity_3(self):
        self.assertEqual('cpl', run_nodelay('PLAIN', 'cpl'))

    def test_diversity_4(self):
        self.assertEqual('fjxmrxyeuk', run_nodelay('PLAIN', 'fjxmrxyeuk'))

    def test_diversity_5(self):
        self.assertEqual('aeeype', run_nodelay('PLAIN', 'aeeype'))

    def test_diversity_6(self):
        self.assertEqual('npwc', run_nodelay('PLAIN', 'npwc'))

    def test_diversity_7(self):
        self.assertEqual('enkqzlsy', run_nodelay('PLAIN', 'enkqzlsy'))

    def test_diversity_8(self):
        self.assertEqual('ryzuwglrxt', run_nodelay('PLAIN', 'ryzuwglrxt'))

    def test_diversity_9(self):
        self.assertEqual('irc', run_nodelay('PLAIN', 'irc'))

    def test_diversity_10(self):
        self.assertEqual('bfopqgke', run_nodelay('PLAIN', 'bfopqgke'))
