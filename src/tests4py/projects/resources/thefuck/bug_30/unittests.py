import unittest
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.fix_file import match


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('fyfSndHQmE a.rb', '',
                                             "\n             can't load package:\n             a.go:1:1: expected 'package', found '+'\n             "),
                                     Settings()))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('LZOrjBsiof a.c', '',
                                             "\n             fish: Unknown command 'foo'\n             /tmp/fix-error/a.sh (line 2): foo\n                                           ^\n             "),
                                     Settings()))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('ImIGecvveKv a.sh', '',
                                             "\n             can't load package:\n             a.go:1:1: expected 'package', found '+'\n             "),
                                     Settings()))

    def test_diversity_4(self):
        self.assertEqual(True, match(
            Command('XbESAxScK a.sh', '', "\n             lua: a.lua:2: unexpected symbol near '+'\n             "),
            Settings()))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('HCXoAYXDCM a.py', '',
                                             "\n             a.c: In function 'main':\n             a.c:3:1: error: expected expression before '}' token\n              }\n               ^\n             "),
                                     Settings()))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('./a', '',
                                             "\n             bidule\n             make: bidule: Command not found\n             Makefile:2: recipe for target 'target' failed\n             make: *** [target] Error 127\n             "),
                                     Settings()))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('KtzKZ a.rs', '',
                                             '\n             fatal: bad config file line 1 in /home/martin/.config/git/config\n             '),
                                     Settings()))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('tlPRZL', '',
                                             "\n             a.c: In function 'main':\n             a.c:3:1: error: expected expression before '}' token\n              }\n               ^\n             "),
                                     Settings()))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('aNxUXTsq fuck.js asdf qwer', '',
                                             '\n             a.sh: line 2: foo: command not found\n             '),
                                     Settings()))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('./a', '',
                                             "\n             a.c: In function 'main':\n             a.c:3:1: error: expected expression before '}' token\n              }\n               ^\n             "),
                                     Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(
            Command('VBcEWEvMsy', '', '\n             a.sh:2: command not found: foo\n             '), Settings()))

    def test_diversity_2(self):
        self.assertEqual(False, match(
            Command('bUcmHiOxZjij a.sh', '',
                    '\n             llc: a.ll:1:1: error: expected top-level entity\n             +\n             ^\n             '),
            Settings()))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('QKkovPpvyib st', '',
                                              '\n             llc: a.ll:1:1: error: expected top-level entity\n             +\n             ^\n             '),
                                      Settings()))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('wyueZbPsyPYCjbd a.c', '',
                                              '\n             llc: a.ll:1:1: error: expected top-level entity\n             +\n             ^\n             '),
                                      Settings()))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('qRGIbHKKw a.pl', '',
                                              '\n             fatal: bad config file line 1 in /home/martin/.config/git/config\n             '),
                                      Settings()))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('kdChaPmsq a.c', '',
                                              '\n             awk: ./a:2: BEGIN { print "Hello, world!" + }\n             awk: ./a:2:                                 ^ syntax error\n             '),
                                      Settings()))

    def test_diversity_7(self):
        self.assertEqual(False, match(
            Command('hxIkaFfWx a.sh', '',
                    "\n             fish: Unknown command 'foo'\n             /tmp/fix-error/a.sh (line 2): foo\n                                           ^\n             "),
            Settings()))

    def test_diversity_8(self):
        self.assertEqual(False, match(
            Command('kdChaPmsq a.c', '',
                    '\n             awk: ./a:2: BEGIN { print "Hello, world!" + }\n             awk: ./a:2:                                 ^ syntax error\n             '),
            Settings()))

    def test_diversity_9(self):
        self.assertEqual(False, match(
            Command('qVrkvYSBFYlK a.py', '', '\n             a.sh: line 2: foo: command not found\n             '),
            Settings()))

    def test_diversity_10(self):
        self.assertEqual(False, match(
            Command('fUJbAAYY a.ll', '', '\n             a.rb:3: syntax error, unexpected keyword_end\n             '),
            Settings()))
