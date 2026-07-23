import unittest
import asyncio
from tornado.ioloop import IOLoop
from tornado.platform.asyncio import AsyncIOLoop
def run_leak(scenario, n):
    AsyncIOLoop().close()
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    orig = len(IOLoop._ioloop_for_asyncio)
    if scenario == 'IOLOOP_CLOSE':
        for _ in range(n):
            loop = AsyncIOLoop()
            loop.close()
        return len(IOLoop._ioloop_for_asyncio) - orig
    if scenario == 'ASYNCIO_CLOSE':
        for _ in range(n):
            loop = asyncio.new_event_loop()
            loop.call_soon(IOLoop.current)
            loop.call_soon(loop.stop)
            loop.run_forever()
            loop.close()
        return len(IOLoop._ioloop_for_asyncio) - orig
    loops = []
    for _ in range(n):
        loops.append(AsyncIOLoop())
    count = len(IOLoop._ioloop_for_asyncio) - orig
    for loop in loops:
        loop.close()
    return count



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 15))

    def test_diversity_2(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 18))

    def test_diversity_3(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 19))

    def test_diversity_4(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 14))

    def test_diversity_5(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 13))

    def test_diversity_6(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 3))

    def test_diversity_7(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 12))

    def test_diversity_8(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 17))

    def test_diversity_9(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 11))

    def test_diversity_10(self):
        self.assertEqual(0, run_leak('IOLOOP_CLOSE', 16))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(15, run_leak('KEEP', 15))

    def test_diversity_2(self):
        self.assertEqual(12, run_leak('KEEP', 12))

    def test_diversity_3(self):
        self.assertEqual(2, run_leak('KEEP', 2))

    def test_diversity_4(self):
        self.assertEqual(8, run_leak('KEEP', 8))

    def test_diversity_5(self):
        self.assertEqual(1, run_leak('KEEP', 1))

    def test_diversity_6(self):
        self.assertEqual(14, run_leak('KEEP', 14))

    def test_diversity_7(self):
        self.assertEqual(3, run_leak('KEEP', 3))

    def test_diversity_8(self):
        self.assertEqual(18, run_leak('KEEP', 18))

    def test_diversity_9(self):
        self.assertEqual(16, run_leak('KEEP', 16))

    def test_diversity_10(self):
        self.assertEqual(11, run_leak('KEEP', 11))
