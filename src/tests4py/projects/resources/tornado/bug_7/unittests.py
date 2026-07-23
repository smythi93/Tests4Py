import unittest
from tornado.ioloop import IOLoop
def run_executor(mode, word):
    io = IOLoop()
    io.make_current()

    async def _run():
        if mode == 'EXECUTOR':
            return str(await io.run_in_executor(None, len, word))
        return word
    try:
        return io.run_sync(_run)
    finally:
        io.close()



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('6', run_executor('EXECUTOR', 'otkcyj'))

    def test_diversity_2(self):
        self.assertEqual('5', run_executor('EXECUTOR', 'rwflz'))

    def test_diversity_3(self):
        self.assertEqual('5', run_executor('EXECUTOR', 'xgmjl'))

    def test_diversity_4(self):
        self.assertEqual('7', run_executor('EXECUTOR', 'mzeqcvt'))

    def test_diversity_5(self):
        self.assertEqual('9', run_executor('EXECUTOR', 'xhpfdsldc'))

    def test_diversity_6(self):
        self.assertEqual('6', run_executor('EXECUTOR', 'oyfjbv'))

    def test_diversity_7(self):
        self.assertEqual('6', run_executor('EXECUTOR', 'kqphwr'))

    def test_diversity_8(self):
        self.assertEqual('7', run_executor('EXECUTOR', 'nmbkvzd'))

    def test_diversity_9(self):
        self.assertEqual('10', run_executor('EXECUTOR', 'fndycpmoao'))

    def test_diversity_10(self):
        self.assertEqual('4', run_executor('EXECUTOR', 'iagl'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('ktwohkna', run_executor('DIRECT', 'ktwohkna'))

    def test_diversity_2(self):
        self.assertEqual('fivydudlfh', run_executor('DIRECT', 'fivydudlfh'))

    def test_diversity_3(self):
        self.assertEqual('nfunxppk', run_executor('DIRECT', 'nfunxppk'))

    def test_diversity_4(self):
        self.assertEqual('ucerkqwn', run_executor('DIRECT', 'ucerkqwn'))

    def test_diversity_5(self):
        self.assertEqual('bfgvv', run_executor('DIRECT', 'bfgvv'))

    def test_diversity_6(self):
        self.assertEqual('byvebz', run_executor('DIRECT', 'byvebz'))

    def test_diversity_7(self):
        self.assertEqual('oxy', run_executor('DIRECT', 'oxy'))

    def test_diversity_8(self):
        self.assertEqual('pgtofkb', run_executor('DIRECT', 'pgtofkb'))

    def test_diversity_9(self):
        self.assertEqual('criapgg', run_executor('DIRECT', 'criapgg'))

    def test_diversity_10(self):
        self.assertEqual('wmgjrgzjl', run_executor('DIRECT', 'wmgjrgzjl'))
