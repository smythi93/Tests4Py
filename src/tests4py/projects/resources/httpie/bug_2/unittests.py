import unittest
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from httpie.context import Environment
from httpie.core import main

class _RedirectHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            n = int(self.path.rstrip('/').split('/')[-1])
        except ValueError:
            n = 0
        if n > 0:
            self.send_response(302)
            self.send_header('Location', '/redirect/%d' % (n - 1))
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'done')

    def log_message(self, *args):
        pass

def run_redirects(max_redirects, chain_length):
    server = HTTPServer(('127.0.0.1', 0), _RedirectHandler)
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    env = Environment(stdout=tempfile.TemporaryFile('w+b'), stderr=tempfile.TemporaryFile('w+t'), stdin_isatty=True, stdout_isatty=False, colors=0, config_dir=tempfile.mkdtemp())
    try:
        return main(['--max-redirects=%d' % max_redirects, '--follow', 'http://127.0.0.1:%d/redirect/%d' % (port, chain_length)], env=env)
    finally:
        server.shutdown()

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(6, run_redirects(0, 1))

    def test_diversity_2(self):
        self.assertEqual(6, run_redirects(3, 7))

    def test_diversity_3(self):
        self.assertEqual(6, run_redirects(1, 3))

    def test_diversity_4(self):
        self.assertEqual(6, run_redirects(2, 5))

    def test_diversity_5(self):
        self.assertEqual(6, run_redirects(0, 2))

    def test_diversity_6(self):
        self.assertEqual(6, run_redirects(3, 4))

    def test_diversity_7(self):
        self.assertEqual(6, run_redirects(2, 3))

    def test_diversity_8(self):
        self.assertEqual(6, run_redirects(0, 4))

    def test_diversity_9(self):
        self.assertEqual(6, run_redirects(2, 6))

    def test_diversity_10(self):
        self.assertEqual(6, run_redirects(0, 3))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(0, run_redirects(2, 2))

    def test_diversity_2(self):
        self.assertEqual(0, run_redirects(5, 1))

    def test_diversity_3(self):
        self.assertEqual(0, run_redirects(3, 2))

    def test_diversity_4(self):
        self.assertEqual(0, run_redirects(4, 2))

    def test_diversity_5(self):
        self.assertEqual(0, run_redirects(3, 1))

    def test_diversity_6(self):
        self.assertEqual(0, run_redirects(5, 0))

    def test_diversity_7(self):
        self.assertEqual(0, run_redirects(5, 2))

    def test_diversity_8(self):
        self.assertEqual(0, run_redirects(4, 3))

    def test_diversity_9(self):
        self.assertEqual(0, run_redirects(6, 1))

    def test_diversity_10(self):
        self.assertEqual(0, run_redirects(6, 3))