import unittest
import os
import tempfile
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.testing import bind_unused_port
def run_range(size, range_header):
    tmpdir = tempfile.mkdtemp()
    with open(os.path.join(tmpdir, 'f.txt'), 'wb') as fp:
        fp.write(b'A' * size)

    async def _run():
        app = tornado.web.Application([('/static/(.*)', tornado.web.StaticFileHandler, {'path': tmpdir})])
        sock, port = bind_unused_port()
        server = tornado.httpserver.HTTPServer(app)
        server.add_socket(sock)
        client = AsyncHTTPClient()
        req = HTTPRequest('http://127.0.0.1:%d/static/f.txt' % port, method='GET', headers={'Range': range_header})
        resp = await client.fetch(req, raise_error=False)
        server.stop()
        return resp.code
    return tornado.ioloop.IOLoop.current().run_sync(_run)



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(200, run_range(10, 'bytes=-600837'))

    def test_diversity_2(self):
        self.assertEqual(200, run_range(80, 'bytes=-727289'))

    def test_diversity_3(self):
        self.assertEqual(200, run_range(19, 'bytes=-215377'))

    def test_diversity_4(self):
        self.assertEqual(200, run_range(160, 'bytes=-160596'))

    def test_diversity_5(self):
        self.assertEqual(200, run_range(32, 'bytes=-106295'))

    def test_diversity_6(self):
        self.assertEqual(200, run_range(14, 'bytes=-288380'))

    def test_diversity_7(self):
        self.assertEqual(416, run_range(111, 'bytes=58-42'))

    def test_diversity_8(self):
        self.assertEqual(416, run_range(156, 'bytes=97-65'))

    def test_diversity_9(self):
        self.assertEqual(200, run_range(141, 'bytes=-846412'))

    def test_diversity_10(self):
        self.assertEqual(416, run_range(91, 'bytes=76-17'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(206, run_range(84, 'bytes=-71'))

    def test_diversity_2(self):
        self.assertEqual(206, run_range(173, 'bytes=166-171'))

    def test_diversity_3(self):
        self.assertEqual(206, run_range(34, 'bytes=7-8'))

    def test_diversity_4(self):
        self.assertEqual(206, run_range(37, 'bytes=-5'))

    def test_diversity_5(self):
        self.assertEqual(206, run_range(47, 'bytes=-11'))

    def test_diversity_6(self):
        self.assertEqual(206, run_range(95, 'bytes=-44'))

    def test_diversity_7(self):
        self.assertEqual(206, run_range(148, 'bytes=-80'))

    def test_diversity_8(self):
        self.assertEqual(206, run_range(129, 'bytes=-79'))

    def test_diversity_9(self):
        self.assertEqual(206, run_range(65, 'bytes=5-59'))

    def test_diversity_10(self):
        self.assertEqual(206, run_range(54, 'bytes=-29'))
