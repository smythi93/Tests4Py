import unittest
import socket
import tornado.ioloop
from tornado.iostream import IOStream
from tornado.testing import bind_unused_port
from tornado.netutil import add_accept_handler
from tornado.http1connection import HTTP1Connection
from tornado.httputil import RequestStartLine, HTTPHeaders
from tornado.locks import Event
from tornado import gen
def run_write(mode, body):
    io = tornado.ioloop.IOLoop()
    io.make_current()
    holder = {}

    @gen.coroutine
    def _main():
        listener, port = bind_unused_port()
        ev = Event()
        h = {}

        def _accept(conn, addr):
            h['server'] = IOStream(conn)
            ev.set()
        add_accept_handler(listener, _accept)
        client = IOStream(socket.socket())
        yield [client.connect(('127.0.0.1', port)), ev.wait()]
        io.remove_handler(listener)
        listener.close()
        server = h['server']
        conn = HTTP1Connection(client, True)
        headers = HTTPHeaders()
        if mode == 'TE_CHUNKED':
            headers.add('Transfer-Encoding', 'chunked')
        else:
            headers.add('Content-Length', str(len(body)))
        yield conn.write_headers(RequestStartLine('PUT', '/put', 'HTTP/1.1'), headers)
        yield conn.write(body.encode())
        conn.finish()
        data = b''
        while b'\r\n\r\n' not in data:
            data += (yield server.read_bytes(1, partial=True))
        for _ in range(400):
            try:
                chunk = (yield gen.with_timeout(io.time() + 0.5, server.read_bytes(1, partial=True)))
                data += chunk
            except Exception:
                break
        _, _, rest = data.partition(b'\r\n\r\n')
        holder['out'] = 'CHUNKED' if b'0\r\n\r\n' in rest else 'RAW'
    io.run_sync(_main)
    return holder['out']



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'fxtgboumlo'))

    def test_diversity_2(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'jtm'))

    def test_diversity_3(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'mojxfxt'))

    def test_diversity_4(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'kikgnpdndc'))

    def test_diversity_5(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'cipmtwsf'))

    def test_diversity_6(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'wevnihjam'))

    def test_diversity_7(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'zlqjklwtg'))

    def test_diversity_8(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'gjqhknwqy'))

    def test_diversity_9(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'ousyqqhdkn'))

    def test_diversity_10(self):
        self.assertEqual('CHUNKED', run_write('TE_CHUNKED', 'hdlbirv'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'bpnrvnonfy'))

    def test_diversity_2(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'aznookdl'))

    def test_diversity_3(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'atmrjp'))

    def test_diversity_4(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'qnadtohe'))

    def test_diversity_5(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'poba'))

    def test_diversity_6(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'aculepkq'))

    def test_diversity_7(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'xmmlfx'))

    def test_diversity_8(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'uxno'))

    def test_diversity_9(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'qkpmi'))

    def test_diversity_10(self):
        self.assertEqual('RAW', run_write('CONTENT_LENGTH', 'jqxzul'))
