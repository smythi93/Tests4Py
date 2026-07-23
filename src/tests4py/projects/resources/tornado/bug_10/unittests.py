import unittest
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.websocket import websocket_connect, WebSocketHandler
from tornado.template import DictLoader
from tornado import gen
def run_render(mode, word):
    io = tornado.ioloop.IOLoop()
    io.make_current()
    holder = {}

    class _Render(WebSocketHandler):

        def on_message(self, message):
            self.write_message(self.render_string('message.html', message=message))

    class _Echo(WebSocketHandler):

        def on_message(self, message):
            self.write_message(message)
    handler = _Render if mode == 'RENDER' else _Echo

    @gen.coroutine
    def _main():
        app = tornado.web.Application([('/ws', handler)], template_loader=DictLoader({'message.html': '<b>{{ message }}</b>'}))
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        try:
            ws = (yield websocket_connect('ws://127.0.0.1:%d/ws' % port))
            ws.write_message(word)
            msg = (yield ws.read_message())
            holder['out'] = msg if msg is not None else 'ERROR:None'
        except Exception as e:
            holder['out'] = 'ERROR:%s' % type(e).__name__
    io.run_sync(_main)
    return holder['out']



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('<b>ifikwzzvcs</b>', run_render('RENDER', 'ifikwzzvcs'))

    def test_diversity_2(self):
        self.assertEqual('<b>bhek</b>', run_render('RENDER', 'bhek'))

    def test_diversity_3(self):
        self.assertEqual('<b>sdmcsu</b>', run_render('RENDER', 'sdmcsu'))

    def test_diversity_4(self):
        self.assertEqual('<b>uqkhwj</b>', run_render('RENDER', 'uqkhwj'))

    def test_diversity_5(self):
        self.assertEqual('<b>mgouy</b>', run_render('RENDER', 'mgouy'))

    def test_diversity_6(self):
        self.assertEqual('<b>hrxid</b>', run_render('RENDER', 'hrxid'))

    def test_diversity_7(self):
        self.assertEqual('<b>qknwjfehpa</b>', run_render('RENDER', 'qknwjfehpa'))

    def test_diversity_8(self):
        self.assertEqual('<b>mxy</b>', run_render('RENDER', 'mxy'))

    def test_diversity_9(self):
        self.assertEqual('<b>syvl</b>', run_render('RENDER', 'syvl'))

    def test_diversity_10(self):
        self.assertEqual('<b>bfc</b>', run_render('RENDER', 'bfc'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('nribtgn', run_render('ECHO', 'nribtgn'))

    def test_diversity_2(self):
        self.assertEqual('jbwyriej', run_render('ECHO', 'jbwyriej'))

    def test_diversity_3(self):
        self.assertEqual('enfwyt', run_render('ECHO', 'enfwyt'))

    def test_diversity_4(self):
        self.assertEqual('tmlk', run_render('ECHO', 'tmlk'))

    def test_diversity_5(self):
        self.assertEqual('yofve', run_render('ECHO', 'yofve'))

    def test_diversity_6(self):
        self.assertEqual('fpytkik', run_render('ECHO', 'fpytkik'))

    def test_diversity_7(self):
        self.assertEqual('bqvvuxfv', run_render('ECHO', 'bqvvuxfv'))

    def test_diversity_8(self):
        self.assertEqual('ctvrzkxy', run_render('ECHO', 'ctvrzkxy'))

    def test_diversity_9(self):
        self.assertEqual('rfau', run_render('ECHO', 'rfau'))

    def test_diversity_10(self):
        self.assertEqual('hhsgygzyvs', run_render('ECHO', 'hhsgygzyvs'))
