import unittest
import socket
import threading
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.testing import bind_unused_port
from tornado.web import RequestHandler
from tornado.escape import recursive_unicode
class _T4PEcho(RequestHandler):

    def post(self):
        self.write(recursive_unicode(self.request.arguments))
def run_chunked(te_casing, key, value):
    holder = {}
    started = threading.Event()

    def _serve():
        io = tornado.ioloop.IOLoop()
        io.make_current()
        app = tornado.web.Application([('/echo', _T4PEcho)])
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        holder['port'] = port
        holder['io'] = io
        started.set()
        io.start()
    t = threading.Thread(target=_serve, daemon=True)
    t.start()
    started.wait(10)
    try:
        body = '%s=%s' % (key, value)
        chunk = '%x\r\n%s\r\n0\r\n\r\n' % (len(body), body)
        req = 'POST /echo HTTP/1.1\r\nTransfer-Encoding: %s\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n%s' % (te_casing, chunk)
        s = socket.create_connection(('127.0.0.1', holder['port']), timeout=10)
        s.settimeout(10)
        s.sendall(req.encode())
        data = b''
        while b'\r\n\r\n' not in data:
            data += s.recv(4096)
        header, _, rest = data.partition(b'\r\n\r\n')
        cl = 0
        for line in header.split(b'\r\n'):
            if line.lower().startswith(b'content-length:'):
                cl = int(line.split(b':')[1].strip())
        body_bytes = rest
        while len(body_bytes) < cl:
            body_bytes += s.recv(4096)
        s.close()
        return body_bytes[:cl].decode()
    finally:
        holder['io'].add_callback(holder['io'].stop)
        t.join(10)



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('{"qiray": ["htwpx"]}', run_chunked('chUNKeD', 'qiray', 'htwpx'))

    def test_diversity_2(self):
        self.assertEqual('{"cofou": ["rcu"]}', run_chunked('chUNkeD', 'cofou', 'rcu'))

    def test_diversity_3(self):
        self.assertEqual('{"kep": ["jpz"]}', run_chunked('CHunKeD', 'kep', 'jpz'))

    def test_diversity_4(self):
        self.assertEqual('{"cikyp": ["luv"]}', run_chunked('cHuNKED', 'cikyp', 'luv'))

    def test_diversity_5(self):
        self.assertEqual('{"jjw": ["rzt"]}', run_chunked('ChUnKeD', 'jjw', 'rzt'))

    def test_diversity_6(self):
        self.assertEqual('{"yucwu": ["gnq"]}', run_chunked('cHunKeD', 'yucwu', 'gnq'))

    def test_diversity_7(self):
        self.assertEqual('{"zfkud": ["vmc"]}', run_chunked('ChUNKeD', 'zfkud', 'vmc'))

    def test_diversity_8(self):
        self.assertEqual('{"sycqn": ["pkm"]}', run_chunked('CHunKed', 'sycqn', 'pkm'))

    def test_diversity_9(self):
        self.assertEqual('{"uvnf": ["nwt"]}', run_chunked('ChUnKed', 'uvnf', 'nwt'))

    def test_diversity_10(self):
        self.assertEqual('{"yqe": ["ybhcq"]}', run_chunked('chUNked', 'yqe', 'ybhcq'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('{"lyhins": ["ihl"]}', run_chunked('chunked', 'lyhins', 'ihl'))

    def test_diversity_2(self):
        self.assertEqual('{"pibg": ["gic"]}', run_chunked('chunked', 'pibg', 'gic'))

    def test_diversity_3(self):
        self.assertEqual('{"eipxu": ["jcp"]}', run_chunked('chunked', 'eipxu', 'jcp'))

    def test_diversity_4(self):
        self.assertEqual('{"udyh": ["qsoj"]}', run_chunked('chunked', 'udyh', 'qsoj'))

    def test_diversity_5(self):
        self.assertEqual('{"lwd": ["yyyffo"]}', run_chunked('chunked', 'lwd', 'yyyffo'))

    def test_diversity_6(self):
        self.assertEqual('{"jwaq": ["aezq"]}', run_chunked('chunked', 'jwaq', 'aezq'))

    def test_diversity_7(self):
        self.assertEqual('{"uwgh": ["bmtwu"]}', run_chunked('chunked', 'uwgh', 'bmtwu'))

    def test_diversity_8(self):
        self.assertEqual('{"wfu": ["clos"]}', run_chunked('chunked', 'wfu', 'clos'))

    def test_diversity_9(self):
        self.assertEqual('{"inawtw": ["lqpekj"]}', run_chunked('chunked', 'inawtw', 'lqpekj'))

    def test_diversity_10(self):
        self.assertEqual('{"gag": ["ycl"]}', run_chunked('chunked', 'gag', 'ycl'))
