import unittest
import logging
logging.disable(logging.CRITICAL)
from sanic.server import AsyncioServer

class _FakeServer:

    def __init__(self, token):
        self.token = token

    def start_serving(self):
        return 'start_serving:' + self.token

    def serve_forever(self):
        return 'serve_forever:' + self.token

    def is_serving(self):
        return 'is_serving:' + self.token

    def wait_closed(self):
        return 'wait_closed:' + self.token

def run_asyncio_server_method(method, token):
    srv = AsyncioServer(None, None, set(), None, None, None)
    srv.server = _FakeServer(token)
    return getattr(srv, method)()

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('start_serving:shtlmcnm', run_asyncio_server_method('start_serving', 'shtlmcnm'))

    def test_diversity_2(self):
        self.assertEqual('serve_forever:gyfw', run_asyncio_server_method('serve_forever', 'gyfw'))

    def test_diversity_3(self):
        self.assertEqual('serve_forever:ndxn', run_asyncio_server_method('serve_forever', 'ndxn'))

    def test_diversity_4(self):
        self.assertEqual('serve_forever:izpkfnvi', run_asyncio_server_method('serve_forever', 'izpkfnvi'))

    def test_diversity_5(self):
        self.assertEqual('start_serving:tjpupwh', run_asyncio_server_method('start_serving', 'tjpupwh'))

    def test_diversity_6(self):
        self.assertEqual('serve_forever:xskgtr', run_asyncio_server_method('serve_forever', 'xskgtr'))

    def test_diversity_7(self):
        self.assertEqual('serve_forever:fnzcdmg', run_asyncio_server_method('serve_forever', 'fnzcdmg'))

    def test_diversity_8(self):
        self.assertEqual('start_serving:ffjsbncq', run_asyncio_server_method('start_serving', 'ffjsbncq'))

    def test_diversity_9(self):
        self.assertEqual('start_serving:rupymlhz', run_asyncio_server_method('start_serving', 'rupymlhz'))

    def test_diversity_10(self):
        self.assertEqual('serve_forever:xtvhq', run_asyncio_server_method('serve_forever', 'xtvhq'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('is_serving:dfiljth', run_asyncio_server_method('is_serving', 'dfiljth'))

    def test_diversity_2(self):
        self.assertEqual('wait_closed:rytacsnq', run_asyncio_server_method('wait_closed', 'rytacsnq'))

    def test_diversity_3(self):
        self.assertEqual('is_serving:jtdzcsg', run_asyncio_server_method('is_serving', 'jtdzcsg'))

    def test_diversity_4(self):
        self.assertEqual('wait_closed:jdeo', run_asyncio_server_method('wait_closed', 'jdeo'))

    def test_diversity_5(self):
        self.assertEqual('wait_closed:saubxbf', run_asyncio_server_method('wait_closed', 'saubxbf'))

    def test_diversity_6(self):
        self.assertEqual('is_serving:wnrnjrp', run_asyncio_server_method('is_serving', 'wnrnjrp'))

    def test_diversity_7(self):
        self.assertEqual('wait_closed:wszwzlbx', run_asyncio_server_method('wait_closed', 'wszwzlbx'))

    def test_diversity_8(self):
        self.assertEqual('is_serving:uzlf', run_asyncio_server_method('is_serving', 'uzlf'))

    def test_diversity_9(self):
        self.assertEqual('is_serving:otjkyh', run_asyncio_server_method('is_serving', 'otjkyh'))

    def test_diversity_10(self):
        self.assertEqual('wait_closed:ogaer', run_asyncio_server_method('wait_closed', 'ogaer'))
