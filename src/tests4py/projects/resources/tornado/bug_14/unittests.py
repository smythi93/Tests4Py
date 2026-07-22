import unittest
from tornado.ioloop import IOLoop
def run_ioloop(scenario, nonce=''):
    IOLoop.clear_current()
    loops = []
    raised = False
    try:
        if scenario == 'SINGLE_TRUE':
            loops.append(IOLoop(make_current=True))
        elif scenario == 'DEFAULT_THEN_TRUE':
            loops.append(IOLoop())
            loops.append(IOLoop(make_current=True))
        elif scenario == 'MC_FALSE':
            loops.append(IOLoop(make_current=False))
        elif scenario == 'DEFAULT':
            loops.append(IOLoop())
        elif scenario == 'DOUBLE_DEFAULT':
            loops.append(IOLoop())
            loops.append(IOLoop())
    except RuntimeError:
        raised = True
    finally:
        for _loop in loops:
            try:
                _loop.close()
            except Exception:
                pass
        IOLoop.clear_current()
    return 'RAISED' if raised else 'OK'



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('OK', run_ioloop('SINGLE_TRUE', 'ppwe'))

    def test_diversity_2(self):
        self.assertEqual('OK', run_ioloop('SINGLE_TRUE', 'nnxwmx'))

    def test_diversity_3(self):
        self.assertEqual('RAISED', run_ioloop('DEFAULT_THEN_TRUE', 'xpclw'))

    def test_diversity_4(self):
        self.assertEqual('RAISED', run_ioloop('DEFAULT_THEN_TRUE', 'qyux'))

    def test_diversity_5(self):
        self.assertEqual('OK', run_ioloop('SINGLE_TRUE', 'moxzhkr'))

    def test_diversity_6(self):
        self.assertEqual('OK', run_ioloop('SINGLE_TRUE', 'juszljpi'))

    def test_diversity_7(self):
        self.assertEqual('OK', run_ioloop('SINGLE_TRUE', 'gngm'))

    def test_diversity_8(self):
        self.assertEqual('RAISED', run_ioloop('DEFAULT_THEN_TRUE', 'rbwnhwm'))

    def test_diversity_9(self):
        self.assertEqual('RAISED', run_ioloop('DEFAULT_THEN_TRUE', 'olxxfnjm'))

    def test_diversity_10(self):
        self.assertEqual('RAISED', run_ioloop('DEFAULT_THEN_TRUE', 'yqfbxcvw'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('OK', run_ioloop('MC_FALSE', 'ylcix'))

    def test_diversity_2(self):
        self.assertEqual('OK', run_ioloop('DOUBLE_DEFAULT', 'hfinobd'))

    def test_diversity_3(self):
        self.assertEqual('OK', run_ioloop('DOUBLE_DEFAULT', 'vngjb'))

    def test_diversity_4(self):
        self.assertEqual('OK', run_ioloop('MC_FALSE', 'mnex'))

    def test_diversity_5(self):
        self.assertEqual('OK', run_ioloop('DOUBLE_DEFAULT', 'veparo'))

    def test_diversity_6(self):
        self.assertEqual('OK', run_ioloop('DEFAULT', 'yyuu'))

    def test_diversity_7(self):
        self.assertEqual('OK', run_ioloop('DOUBLE_DEFAULT', 'lgxryhn'))

    def test_diversity_8(self):
        self.assertEqual('OK', run_ioloop('DOUBLE_DEFAULT', 'hnbggklo'))

    def test_diversity_9(self):
        self.assertEqual('OK', run_ioloop('DEFAULT', 'fpix'))

    def test_diversity_10(self):
        self.assertEqual('OK', run_ioloop('MC_FALSE', 'pwwqqhv'))
