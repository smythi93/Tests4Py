from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return './a' '' '\n             a.sh: line 2: foo: command not found\n             '

    def test_diversity_2(self):
        return 'XoomWEoiOEpov a.sh' '' '\n             /Users/pablo/Workspace/barebones/fuck.js:2\n             conole.log(arg);  // this should read console.log(arg);\n             ^\n             ReferenceError: conole is not defined\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\n                 at Array.forEach (native)\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\n                 at Module._compile (module.js:460:26)\n                 at Object.Module._extensions..js (module.js:478:10)\n                 at Module.load (module.js:355:32)\n                 at Function.Module._load (module.js:310:12)\n                 at Function.Module.runMain (module.js:501:10)\n                 at startup (node.js:129:16)\n                 at node.js:814:3\n             '

    def test_diversity_3(self):
        return 'wqMhyDDUAaPL a.sh' '' '\n             a.rs:2:5: 2:6 error: unexpected token: `+`\n             a.rs:2     +\n                        ^\n             '

    def test_diversity_4(self):
        return 'GndbnBDvy' '' "\n             lua: a.lua:2: unexpected symbol near '+'\n             "

    def test_diversity_5(self):
        return 'SfcTJKYNmb a.sh' '' '\n             /Users/pablo/Workspace/barebones/fuck.js:2\n             conole.log(arg);  // this should read console.log(arg);\n             ^\n             ReferenceError: conole is not defined\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\n                 at Array.forEach (native)\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\n                 at Module._compile (module.js:460:26)\n                 at Object.Module._extensions..js (module.js:478:10)\n                 at Module.load (module.js:355:32)\n                 at Function.Module._load (module.js:310:12)\n                 at Function.Module.runMain (module.js:501:10)\n                 at startup (node.js:129:16)\n                 at node.js:814:3\n             '

    def test_diversity_6(self):
        return 'cRGuAuNVaNFxY st' '' '\n             a.sh: line 2: foo: command not found\n             '

    def test_diversity_7(self):
        return 'RsbVho a.py' '' '\n             Traceback (most recent call last):\n               File "a.py", line 8, in <module>\n                 match("foo")\n               File "a.py", line 5, in match\n                 m = re.search(None, command)\n               File "/usr/lib/python3.4/re.py", line 170, in search\n                 return _compile(pattern, flags).search(string)\n               File "/usr/lib/python3.4/re.py", line 293, in _compile\n                 raise TypeError("first argument must be string or compiled pattern")\n             TypeError: first argument must be string or compiled pattern\n             '

    def test_diversity_8(self):
        return 'bGRFpS a.py' '' '\n             awk: ./a:2: BEGIN { print "Hello, world!" + }\n             awk: ./a:2:                                 ^ syntax error\n             '

    def test_diversity_9(self):
        return 'bsPMWpQSnNPcjs' '' "\n             fish: Unknown command 'foo'\n             /tmp/fix-error/a.sh (line 2): foo\n                                           ^\n             "

    def test_diversity_10(self):
        return 'NvSGPxUeaa' '' '\n             Traceback (most recent call last):\n               File "a.py", line 8, in <module>\n                 match("foo")\n               File "a.py", line 5, in match\n                 m = re.search(None, command)\n               File "/usr/lib/python3.4/re.py", line 170, in search\n                 return _compile(pattern, flags).search(string)\n               File "/usr/lib/python3.4/re.py", line 293, in _compile\n                 raise TypeError("first argument must be string or compiled pattern")\n             TypeError: first argument must be string or compiled pattern\n             '


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'MxAwmG a.sh', '', '\n             syntax error at a.pl line 3, at EOF\n             Execution of a.pl aborted due to compilation errors.\n             '

    def test_diversity_2(self):
        return './a' '' '\n             a.c:3:1: error: expected expression\n             }\n             ^\n             '

    def test_diversity_3(self):
        return 'vcSJZUkyiL a.lua' '' '\n             a.rs:2:5: 2:6 error: unexpected token: `+`\n             a.rs:2     +\n                        ^\n             '

    def test_diversity_4(self):
        return 'xnBoc a.sh' '' '\n             a.sh: line 2: foo: command not found\n             '

    def test_diversity_5(self):
        return 'cwjupvbTy' '' '\n               File "a.py", line 2\n                   +\n                       ^\n             SyntaxError: invalid syntax\n             '

    def test_diversity_6(self):
        return 'DNxhpBXI a.py' '' '\n             a.c:3:1: error: expected expression\n             }\n             ^\n             '

    def test_diversity_7(self):
        return 'KtFwvFRXxKvql a.sh' '' '\n             /Users/pablo/Workspace/barebones/fuck.js:2\n             conole.log(arg);  // this should read console.log(arg);\n             ^\n             ReferenceError: conole is not defined\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\n                 at Array.forEach (native)\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\n                 at Module._compile (module.js:460:26)\n                 at Object.Module._extensions..js (module.js:478:10)\n                 at Module.load (module.js:355:32)\n                 at Function.Module._load (module.js:310:12)\n                 at Function.Module.runMain (module.js:501:10)\n                 at startup (node.js:129:16)\n                 at node.js:814:3\n             '

    def test_diversity_8(self):
        return './a' '' '\n               File "a.py", line 2\n                   +\n                       ^\n             SyntaxError: invalid syntax\n             '

    def test_diversity_9(self):
        return 'VmjmfnoNSrL a.sh' '' '\n             syntax error at a.pl line 3, at EOF\n             Execution of a.pl aborted due to compilation errors.\n             '

    def test_diversity_10(self):
        return 'fWOqBJHORCq a.py' '' '\n                Compiling test v0.1.0 (file:///tmp/fix-error/test)\n                src/lib.rs:3:5: 3:6 error: unexpected token: `+`\n                src/lib.rs:3     +\n                                 ^\n             Could not compile `test`.\n\n             To learn more, run the command again with --verbose.\n             '
