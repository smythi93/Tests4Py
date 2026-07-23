import unittest
from thefuck.rules.fix_file import match
from thefuck.types import Command
from thefuck.types import Settings
import os
os.environ['EDITOR'] = 'vim'


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'okkbzcvpzz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_2(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'kwdnjzyezz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_3(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'zhdjwtlrzz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_4(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'klkwtcozzz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_5(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'zivzgxthzz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_6(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'rzgwikgwzz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_7(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'arqirznjzz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_8(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'vkyvzggazz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_9(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'pyyomxguzz.py:3:'), Settings()) else 'Result is not correct'))

    def test_diversity_10(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'rqhixjukzz.py:3:'), Settings()) else 'Result is not correct'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text shkrvpi with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_2(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text nhewkwwt with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_3(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text hylqj with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_4(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text vewcq with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_5(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text yexqwymq with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_6(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text zmgjfah with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_7(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text doiqzlfast with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_8(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text hjgzjchxxv with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_9(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text guwwagss with no file pattern'), Settings()) else 'Result is not correct'))

    def test_diversity_10(self):
        self.assertEqual('False', ('False' if not match(Command('fix', '', 'just some text vcogxkbiu with no file pattern'), Settings()) else 'Result is not correct'))
