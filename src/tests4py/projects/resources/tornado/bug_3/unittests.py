import unittest
import subprocess
import sys
_T4P_BUG3_SNIPPETS = {'LAMBDA': 'from tornado.httpclient import HTTPClient; f = lambda: None; c = HTTPClient()', 'INT': 'from tornado.httpclient import HTTPClient; f = 5; c = HTTPClient()'}
def run_destructor(mode, nonce=''):
    proc = subprocess.run([sys.executable, '-c', _T4P_BUG3_SNIPPETS[mode]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return 'OUTPUT' if proc.stdout.strip() else 'CLEAN'



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'fbwbrs'))

    def test_diversity_2(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'ssbupj'))

    def test_diversity_3(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'wtxj'))

    def test_diversity_4(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'uffdvakd'))

    def test_diversity_5(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'dkhzel'))

    def test_diversity_6(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'azeliit'))

    def test_diversity_7(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'szhow'))

    def test_diversity_8(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'rcewontc'))

    def test_diversity_9(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'xmewa'))

    def test_diversity_10(self):
        self.assertEqual('CLEAN', run_destructor('LAMBDA', 'pkve'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'rioqig'))

    def test_diversity_2(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'jvswob'))

    def test_diversity_3(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'gqypnem'))

    def test_diversity_4(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'gfvd'))

    def test_diversity_5(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'brojo'))

    def test_diversity_6(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'iczvqu'))

    def test_diversity_7(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'hcfed'))

    def test_diversity_8(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'nlba'))

    def test_diversity_9(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'tety'))

    def test_diversity_10(self):
        self.assertEqual('CLEAN', run_destructor('INT', 'skeudd'))
