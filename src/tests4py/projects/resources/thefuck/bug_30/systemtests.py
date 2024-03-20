from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return """
Traceback (most recent call last):
  File "a.py", line 8, in <module>
    match("foo")
  File "a.py", line 5, in match
    m = re.search(None, command)
  File "/usr/lib/python3.4/re.py", line 170, in search
    return _compile(pattern, flags).search(string)
  File "/usr/lib/python3.4/re.py", line 293, in _compile
    raise TypeError("first argument must be string or compiled pattern")
TypeError: first argument must be string or compiled pattern
"""

    def test_diversity_2(self):
        return """
   Compiling test v0.1.0 (file:///tmp/fix-error/test)
   src/lib.rs:3:5: 3:6 error: unexpected token: `+`
   src/lib.rs:3     +
                    ^
Could not compile `test`.

To learn more, run the command again with --verbose.
"""

    def test_diversity_3(self):
        return """
a.c: In function 'main':
a.c:3:1: error: expected expression before '}' token
 }
  ^
"""

    def test_diversity_4(self):
        return """
  File "a.py", line 2
      +
          ^
SyntaxError: invalid syntax
"""

    def test_diversity_5(self):
        return """
/Users/pablo/Workspace/barebones/fuck.js:2
conole.log(arg);  // this should read console.log(arg);
^
ReferenceError: conole is not defined
    at /Users/pablo/Workspace/barebones/fuck.js:2:5
    at Array.forEach (native)
    at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)
    at Module._compile (module.js:460:26)
    at Object.Module._extensions..js (module.js:478:10)
    at Module.load (module.js:355:32)
    at Function.Module._load (module.js:310:12)
    at Function.Module.runMain (module.js:501:10)
    at startup (node.js:129:16)
    at node.js:814:3
"""

    def test_diversity_6(self):
        return """
fish: Unknown command 'foo'
/tmp/fix-error/a.sh (line 2): foo
                              ^
"""

    def test_diversity_7(self):
        return """
monkeypatch = <_pytest.monkeypatch.monkeypatch object at 0x7fdb76a25b38>
test = ('fish a.sh', '/tmp/fix-error/a.sh', 2, None, '', "\\nfish: Unknown command 'foo'\\n/tmp/fix-error/a.sh (line 2): foo\\n                              ^\\n")

    @pytest.mark.parametrize('test', tests)
    @pytest.mark.usefixtures('no_memoize')
    def test_get_new_command(monkeypatch, test):
>       mocker.patch('os.path.isfile', return_value=True)
E       NameError: name 'mocker' is not defined

/home/thefuck/tests/rules/test_fix_file.py:218: NameError
"""

    def test_diversity_8(self):
        return """
awk: ./a:2: BEGIN { print "Hello, world!" + }
awk: ./a:2:                                 ^ syntax error
"""

    def test_diversity_9(self):
        return """
bidule
make: bidule: Command not found
Makefile:2: recipe for target 'target' failed
make: *** [target] Error 127
"""

    def test_diversity_10(self):
        return """
Search pattern not terminated at a.pl line 2.
"""


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return """
lua: a.lua:2: unexpected symbol near '+'
"""

    def test_diversity_2(self):
        return """
/Users/pablo/Workspace/barebones/fuck.js:2
conole.log(arg);  // this should read console.log(arg);
^
ReferenceError: conole is not defined
    at /Users/pablo/Workspace/barebones/fuck.js:2:5
    at Array.forEach (native)
    at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)
    at Module._compile (module.js:460:26)
    at Object.Module._extensions..js (module.js:478:10)
    at Module.load (module.js:355:32)
    at Function.Module._load (module.js:310:12)
    at Function.Module.runMain (module.js:501:10)
    at startup (node.js:129:16)
    at node.js:814:3
"""

    def test_diversity_3(self):
        return """
monkeypatch = <_pytest.monkeypatch.monkeypatch object at 0x7fdb76a25b38>
test = ('fish a.sh', '/tmp/fix-error/a.sh', 2, None, '', "\\nfish: Unknown command 'foo'\\n/tmp/fix-error/a.sh (line 2): foo\\n                              ^\\n")

    @pytest.mark.parametrize('test', tests)
    @pytest.mark.usefixtures('no_memoize')
    def test_get_new_command(monkeypatch, test):
>       mocker.patch('os.path.isfile', return_value=True)
E       NameError: name 'mocker' is not defined

/home/thefuck/tests/rules/test_fix_file.py:218: NameError
"""

    def test_diversity_4(self):
        return """
bidule
make: bidule: Command not found
Makefile:2: recipe for target 'target' failed
make: *** [target] Error 127
"""

    def test_diversity_5(self):
        return """
syntax error at a.pl line 3, at EOF
Execution of a.pl aborted due to compilation errors.
"""

    def test_diversity_6(self):
        return """
   Compiling test v0.1.0 (file:///tmp/fix-error/test)
   src/lib.rs:3:5: 3:6 error: unexpected token: `+`
   src/lib.rs:3     +
                    ^
Could not compile `test`.

To learn more, run the command again with --verbose.
"""

    def test_diversity_7(self):
        return """
Search pattern not terminated at a.pl line 2.
"""

    def test_diversity_8(self):
        return """
a.c: In function 'main':
a.c:3:1: error: expected expression before '}' token
 }
  ^
"""

    def test_diversity_9(self):
        return """
Traceback (most recent call last):
  File "a.py", line 8, in <module>
    match("foo")
  File "a.py", line 5, in match
    m = re.search(None, command)
  File "/usr/lib/python3.4/re.py", line 170, in search
    return _compile(pattern, flags).search(string)
  File "/usr/lib/python3.4/re.py", line 293, in _compile
    raise TypeError("first argument must be string or compiled pattern")
TypeError: first argument must be string or compiled pattern
"""

    def test_diversity_10(self):
        return """
awk: ./a:2: BEGIN { print "Hello, world!" + }
awk: ./a:2:                                 ^ syntax error
"""
