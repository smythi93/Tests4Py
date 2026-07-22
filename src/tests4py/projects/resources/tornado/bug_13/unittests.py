import unittest
import socket
import tornado.ioloop
from tornado.iostream import IOStream
from tornado.testing import bind_unused_port
from tornado.netutil import add_accept_handler
from tornado.http1connection import HTTP1Connection
from tornado.httputil import HTTPMessageDelegate
from tornado.locks import Event
from tornado import gen
def run_response(mode, body):
    io = tornado.ioloop.IOLoop()
    io.make_current()
    result = {}

    @gen.coroutine
    def _main():
        listener, port = bind_unused_port()
        ev = Event()
        holder = {}

        def _accept(conn, addr):
            holder['server'] = IOStream(conn)
            ev.set()
        add_accept_handler(listener, _accept, io_loop=io)
        client = IOStream(socket.socket())
        yield [client.connect(('127.0.0.1', port)), ev.wait()]
        io.remove_handler(listener)
        listener.close()
        server = holder['server']
        conn = HTTP1Connection(client, True)
        b = body.encode()
        if mode == 'HTTP10_NOCL':
            server.write(b'HTTP/1.0 200 OK\r\n\r\n' + b)
        elif mode == 'HTTP11_CL':
            server.write(b'HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n' % len(b) + b)
        elif mode == 'HTTP10_CL':
            server.write(b'HTTP/1.0 200 OK\r\nContent-Length: %d\r\n\r\n' % len(b) + b)
        server.close()
        code = [None]
        got = []
        done = Event()

        class _D(HTTPMessageDelegate):

            def headers_received(self, start_line, headers):
                code[0] = start_line.code

            def data_received(self, data):
                got.append(data)

            def finish(self):
                done.set()
        try:
            yield conn.read_response(_D())
            yield done.wait()
            result['out'] = '%s,%s' % (code[0], b''.join(got).decode())
        except Exception as e:
            result['out'] = 'ERROR:%s' % type(e).__name__
    io.run_sync(_main)
    return result['out']



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('200,erypbh', run_response('HTTP10_NOCL', 'erypbh'))

    def test_diversity_2(self):
        self.assertEqual('200,ioinwfwi', run_response('HTTP10_NOCL', 'ioinwfwi'))

    def test_diversity_3(self):
        self.assertEqual('200,zlozevq', run_response('HTTP10_NOCL', 'zlozevq'))

    def test_diversity_4(self):
        self.assertEqual('200,dsa', run_response('HTTP10_NOCL', 'dsa'))

    def test_diversity_5(self):
        self.assertEqual('200,dmxfj', run_response('HTTP10_NOCL', 'dmxfj'))

    def test_diversity_6(self):
        self.assertEqual('200,liioto', run_response('HTTP10_NOCL', 'liioto'))

    def test_diversity_7(self):
        self.assertEqual('200,npwgpzw', run_response('HTTP10_NOCL', 'npwgpzw'))

    def test_diversity_8(self):
        self.assertEqual('200,cpcisbwn', run_response('HTTP10_NOCL', 'cpcisbwn'))

    def test_diversity_9(self):
        self.assertEqual('200,fxyx', run_response('HTTP10_NOCL', 'fxyx'))

    def test_diversity_10(self):
        self.assertEqual('200,sobxf', run_response('HTTP10_NOCL', 'sobxf'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('200,vrbwxhax', run_response('HTTP11_CL', 'vrbwxhax'))

    def test_diversity_2(self):
        self.assertEqual('200,theb', run_response('HTTP11_CL', 'theb'))

    def test_diversity_3(self):
        self.assertEqual('200,yezhcevw', run_response('HTTP11_CL', 'yezhcevw'))

    def test_diversity_4(self):
        self.assertEqual('200,mhjiwbzy', run_response('HTTP11_CL', 'mhjiwbzy'))

    def test_diversity_5(self):
        self.assertEqual('200,lhosao', run_response('HTTP11_CL', 'lhosao'))

    def test_diversity_6(self):
        self.assertEqual('200,hkbctwg', run_response('HTTP11_CL', 'hkbctwg'))

    def test_diversity_7(self):
        self.assertEqual('200,yfybwhfn', run_response('HTTP11_CL', 'yfybwhfn'))

    def test_diversity_8(self):
        self.assertEqual('200,wovpihvl', run_response('HTTP11_CL', 'wovpihvl'))

    def test_diversity_9(self):
        self.assertEqual('200,gdungmvt', run_response('HTTP10_CL', 'gdungmvt'))

    def test_diversity_10(self):
        self.assertEqual('200,oulpdjkl', run_response('HTTP11_CL', 'oulpdjkl'))
