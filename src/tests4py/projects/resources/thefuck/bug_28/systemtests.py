from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(True, 'ruby a.rb', '', '\\n             a.sh:2: command not found: foo\\n             ')"

    def test_diversity_2(self):
        return "(True, 'make', '', '\\n             Search pattern not terminated at a.pl line 2.\\n             ')"

    def test_diversity_3(self):
        return "(True, 'make', '', '\\n             a.c:3:1: error: expected expression\\n             }\\n             ^\\n             ')"

    def test_diversity_4(self):
        return '(True, \'rustc a.rs\', \'\', "\\n             fish: Unknown command \'foo\'\\n             /tmp/fix-error/a.sh (line 2): foo\\n                                           ^\\n             ")'

    def test_diversity_5(self):
        return "(True, 'node fuck.js asdf qwer', '', '\\n             a.sh: line 2: foo: command not found\\n             ')"

    def test_diversity_6(self):
        return "(True, 'cargo build', '', '\\n             a.sh: line 2: foo: command not found\\n             ')"

    def test_diversity_7(self):
        return '(True, \'cargo build\', \'\', "\\n             lua: a.lua:2: unexpected symbol near \'+\'\\n             ")'

    def test_diversity_8(self):
        return '(True, \'./a\', \'\', "\\n             fish: Unknown command \'foo\'\\n             /tmp/fix-error/a.sh (line 2): foo\\n                                           ^\\n             ")'

    def test_diversity_9(self):
        return "(True, 'rustc a.rs', '', '\\n             syntax error at a.pl line 3, at EOF\\n             Execution of a.pl aborted due to compilation errors.\\n             ')"

    def test_diversity_10(self):
        return '(True, \'llc a.ll\', \'\', "\\n             fish: Unknown command \'foo\'\\n             /tmp/fix-error/a.sh (line 2): foo\\n                                           ^\\n             ")'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "(False, 'python a.py', '', '\\n             a.c:3:1: error: expected expression\\n             }\\n             ^\\n             ')"

    def test_diversity_2(self):
        return '(False, \'zsh a.sh\', \'\', "\\n             bidule\\n             make: bidule: Command not found\\n             Makefile:2: recipe for target \'target\' failed\\n             make: *** [target] Error 127\\n             ")'

    def test_diversity_3(self):
        return '(False, \'perl a.pl\', \'\', \'\\n             Traceback (most recent call last):\\n               File "a.py", line 8, in <module>\\n                 match("foo")\\n               File "a.py", line 5, in match\\n                 m = re.search(None, command)\\n               File "/usr/lib/python3.4/re.py", line 170, in search\\n                 return _compile(pattern, flags).search(string)\\n               File "/usr/lib/python3.4/re.py", line 293, in _compile\\n                 raise TypeError("first argument must be string or compiled pattern")\\n             TypeError: first argument must be string or compiled pattern\\n             \')'

    def test_diversity_4(self):
        return '(False, \'bash a.sh\', \'\', \'\\n             awk: ./a:2: BEGIN { print "Hello, world!" + }\\n             awk: ./a:2:                                 ^ syntax error\\n             \')'

    def test_diversity_5(self):
        return "(False, 'go build a.go', '', '\\n             a.rs:2:5: 2:6 error: unexpected token: `+`\\n             a.rs:2     +\\n                        ^\\n             ')"

    def test_diversity_6(self):
        return '(False, \'python a.py\', \'\', "\\n             a.c: In function \'main\':\\n             a.c:3:1: error: expected expression before \'}\' token\\n              }\\n               ^\\n             ")'

    def test_diversity_7(self):
        return "(False, 'bash a.sh', '', '\\n             a.rs:2:5: 2:6 error: unexpected token: `+`\\n             a.rs:2     +\\n                        ^\\n             ')"

    def test_diversity_8(self):
        return '(False, \'python a.py\', \'\', \'\\n               File "a.py", line 2\\n                   +\\n                       ^\\n             SyntaxError: invalid syntax\\n             \')'

    def test_diversity_9(self):
        return "(False, 'zsh a.sh', '', '\\n                Compiling test v0.1.0 (file:///tmp/fix-error/test)\\n                src/lib.rs:3:5: 3:6 error: unexpected token: `+`\\n                src/lib.rs:3     +\\n                                 ^\\n             Could not compile `test`.\\n     \\n             To learn more, run the command again with --verbose.\\n             ')"

    def test_diversity_10(self):
        return '(False, \'perl a.pl\', \'\', "\\n             a.c: In function \'main\':\\n             a.c:3:1: error: expected expression before \'}\' token\\n              }\\n               ^\\n             ")'
