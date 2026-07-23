import unittest
import datetime
from tornado.ioloop import IOLoop
from tornado import gen
def run_wait(scenario, nonce=''):
    io = IOLoop()
    io.make_current()

    @gen.coroutine
    def _main():
        try:
            if scenario == 'WAIT_NOREF':
                yield gen.with_timeout(datetime.timedelta(seconds=0.5), gen.WaitIterator(gen.sleep(0)).next())
            else:
                wi = gen.WaitIterator(gen.sleep(0))
                yield gen.with_timeout(datetime.timedelta(seconds=0.5), wi.next())
            raise gen.Return('OK')
        except gen.TimeoutError:
            raise gen.Return('TIMEOUT')
    try:
        return io.run_sync(_main)
    finally:
        io.close()



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'vigjgbh'))

    def test_diversity_2(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'qpumljek'))

    def test_diversity_3(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'xzzhup'))

    def test_diversity_4(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'mlkw'))

    def test_diversity_5(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'xnfwt'))

    def test_diversity_6(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'torw'))

    def test_diversity_7(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'dzia'))

    def test_diversity_8(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'lfzv'))

    def test_diversity_9(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'tokvtez'))

    def test_diversity_10(self):
        self.assertEqual('OK', run_wait('WAIT_NOREF', 'gdrq'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'xbgpym'))

    def test_diversity_2(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'zviwgx'))

    def test_diversity_3(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'cwkfr'))

    def test_diversity_4(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'cuzjdlkm'))

    def test_diversity_5(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'ahlxnze'))

    def test_diversity_6(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'iuxej'))

    def test_diversity_7(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'djcdnf'))

    def test_diversity_8(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'zxskif'))

    def test_diversity_9(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'elkvoo'))

    def test_diversity_10(self):
        self.assertEqual('OK', run_wait('WAIT_REF', 'acoorj'))
