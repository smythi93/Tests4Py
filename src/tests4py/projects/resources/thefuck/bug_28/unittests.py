import unittest
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.fix_file import get_new_command
from thefuck.rules.fix_file import match


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('', get_new_command(Command('python a.py', '',
                                                     '\n             fatal: bad config file line 1 in /home/martin/.config/git/config\n             '),
                                             Settings()))

    def test_diversity_2(self):
        self.assertEqual('', get_new_command(
            Command('perl a.pl', '', '\n             a.sh: line 2: foo: command not found\n             '), Settings()))

    def test_diversity_3(self):
        self.assertEqual('', get_new_command(Command('pep8', '',
                                                     '\n             Traceback (most recent call last):\n               File "a.py", line 8, in <module>\n                 match("foo")\n               File "a.py", line 5, in match\n                 m = re.search(None, command)\n               File "/usr/lib/python3.4/re.py", line 170, in search\n                 return _compile(pattern, flags).search(string)\n               File "/usr/lib/python3.4/re.py", line 293, in _compile\n                 raise TypeError("first argument must be string or compiled pattern")\n             TypeError: first argument must be string or compiled pattern\n             '),
                                             Settings()))

    def test_diversity_4(self):
        self.assertEqual('', get_new_command(Command('node fuck.js asdf qwer', '',
                                                     '\n                Compiling test v0.1.0 (file:///tmp/fix-error/test)\n                src/lib.rs:3:5: 3:6 error: unexpected token: `+`\n                src/lib.rs:3     +\n                                 ^\n             Could not compile `test`.\n     \n             To learn more, run the command again with --verbose.\n             '),
                                             Settings()))

    def test_diversity_5(self):
        self.assertEqual('', get_new_command(Command('./a', '',
                                                     '\n             /Users/pablo/Workspace/barebones/fuck.js:2\n             conole.log(arg);  // this should read console.log(arg);\n             ^\n             ReferenceError: conole is not defined\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\n                 at Array.forEach (native)\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\n                 at Module._compile (module.js:460:26)\n                 at Object.Module._extensions..js (module.js:478:10)\n                 at Module.load (module.js:355:32)\n                 at Function.Module._load (module.js:310:12)\n                 at Function.Module.runMain (module.js:501:10)\n                 at startup (node.js:129:16)\n                 at node.js:814:3\n             '),
                                             Settings()))

    def test_diversity_6(self):
        self.assertEqual('', get_new_command(
            Command('llc a.ll', '', '\n             a.sh:2: command not found: foo\n             '), Settings()))

    def test_diversity_7(self):
        self.assertEqual('', get_new_command(Command('lua a.lua', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('', get_new_command(Command('go build a.go', '',
                                                     '\n             /Users/pablo/Workspace/barebones/fuck.js:2\n             conole.log(arg);  // this should read console.log(arg);\n             ^\n             ReferenceError: conole is not defined\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\n                 at Array.forEach (native)\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\n                 at Module._compile (module.js:460:26)\n                 at Object.Module._extensions..js (module.js:478:10)\n                 at Module.load (module.js:355:32)\n                 at Function.Module._load (module.js:310:12)\n                 at Function.Module.runMain (module.js:501:10)\n                 at startup (node.js:129:16)\n                 at node.js:814:3\n             '),
                                             Settings()))

    def test_diversity_9(self):
        self.assertEqual('', get_new_command(
            Command('./a', '', '\n             a.rb:3: syntax error, unexpected keyword_end\n             '),
            Settings()))

    def test_diversity_10(self):
        self.assertEqual('', get_new_command(Command('git st', '', ''), Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(Command('ruby a.rb', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual(False,
                         match(Command('clang a.c', '', '\n             a.sh:2: command not found: foo\n             '),
                               Settings()))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('./a', '',
                                              "\n             can't load package:\n             a.go:1:2: expected 'package', found '+'\n             "),
                                      Settings()))

    def test_diversity_4(self):
        self.assertEqual(False, match(
            Command('make', '', '\n             a.rb:3: syntax error, unexpected keyword_end\n             '),
            Settings()))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('perl a.pl', '',
                                              '\n             fatal: bad config file line 1 in /home/martin/.config/git/config\n             '),
                                      Settings()))

    def test_diversity_6(self):
        self.assertEqual(False, match(
            Command('perl a.pl', '', '\n             Search pattern not terminated at a.pl line 2.\n             '),
            Settings()))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('fish a.sh', '',
                                              '\n             a.c:3:1: error: expected expression\n             }\n             ^\n             '),
                                      Settings()))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('python a.py', '',
                                              "\n             bidule\n             make: bidule: Command not found\n             Makefile:2: recipe for target 'target' failed\n             make: *** [target] Error 127\n             "),
                                      Settings()))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('llc a.ll', '',
                                              '\n               File "a.py", line 2\n                   +\n                       ^\n             SyntaxError: invalid syntax\n             '),
                                      Settings()))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('go build a.go', '',
                                              "\n             can't load package:\n             a.go:1:2: expected 'package', found '+'\n             "),
                                      Settings()))
