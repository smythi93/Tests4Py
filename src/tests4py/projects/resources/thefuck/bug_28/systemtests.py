from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'fish a.sh' '' '\n             a.sh: line 2: foo: command not found\n             '

    def test_diversity_2(self):
        return 'lua a.lua' '' '\n             awk: ./a:2: BEGIN { print "Hello, world!" + }\n             awk: ./a:2:                                 ^ syntax error\n             '

    def test_diversity_3(self):
        return 'bash a.sh' '' '\n             a.sh: line 2: foo: command not found\n             '

    def test_diversity_4(self):
        return 'lua a.lua' '' '\n                Compiling test v0.1.0 (file:///tmp/fix-error/test)\n                src/lib.rs:3:5: 3:6 error: unexpected token: `+`\n                src/lib.rs:3     +\n                                 ^\n             Could not compile `test`.\n     \n             To learn more, run the command again with --verbose.\n             '

    def test_diversity_5(self):
        return 'llc a.ll' '' '\n             a.sh: line 2: foo: command not found\n             '

    def test_diversity_6(self):
        return 'python a.py' '' '\n             llc: a.ll:1:2: error: expected top-level entity\n             +\n             ^\n             '

    def test_diversity_7(self):
        return 'cargo build' '' "\n             fish: Unknown command 'foo'\n             /tmp/fix-error/a.sh (line 2): foo\n                                           ^\n             "

    def test_diversity_8(self):
        return 'python a.py' '' '\n             a.rs:2:5: 2:6 error: unexpected token: `+`\n             a.rs:2     +\n                        ^\n             '

    def test_diversity_9(self):
        return 'perl a.pl' '' "\n             a.c: In function 'main':\n             a.c:3:1: error: expected expression before '}' token\n              }\n               ^\n             "

    def test_diversity_10(self):
        return 'cargo build' '' '\n             /Users/pablo/Workspace/barebones/fuck.js:2\n             conole.log(arg);  // this should read console.log(arg);\n             ^\n             ReferenceError: conole is not defined\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\n                 at Array.forEach (native)\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\n                 at Module._compile (module.js:460:26)\n                 at Object.Module._extensions..js (module.js:478:10)\n                 at Module.load (module.js:355:32)\n                 at Function.Module._load (module.js:310:12)\n                 at Function.Module.runMain (module.js:501:10)\n                 at startup (node.js:129:16)\n                 at node.js:814:3\n             '


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return './a' '' '\n             llc: a.ll:1:2: error: expected top-level entity\n             +\n             ^\n             '

    def test_diversity_2(self):
        return 'sh a.sh' '' "\n             bidule\n             make: bidule: Command not found\n             Makefile:2: recipe for target 'target' failed\n             make: *** [target] Error 127\n             "

    def test_diversity_3(self):
        return 'ruby a.rb' '' '\n             a.rs:2:5: 2:6 error: unexpected token: `+`\n             a.rs:2     +\n                        ^\n             '

    def test_diversity_4(self):
        return 'perl a.pl' '' '\n               File "a.py", line 2\n                   +\n                       ^\n             SyntaxError: invalid syntax\n             '

    def test_diversity_5(self):
        return 'gcc a.c' '' '\n             syntax error at a.pl line 3, at EOF\n             Execution of a.pl aborted due to compilation errors.\n             '

    def test_diversity_6(self):
        return 'lua a.lua' '' '\n             Search pattern not terminated at a.pl line 2.\n             '

    def test_diversity_7(self):
        return 'perl a.pl' '' "\n             lua: a.lua:2: unexpected symbol near '+'\n             "

    def test_diversity_8(self):
        return 'cargo build' '' '\n                Compiling test v0.1.0 (file:///tmp/fix-error/test)\n                src/lib.rs:3:5: 3:6 error: unexpected token: `+`\n                src/lib.rs:3     +\n                                 ^\n             Could not compile `test`.\n     \n             To learn more, run the command again with --verbose.\n             '

    def test_diversity_9(self):
        return 'sh a.sh' '' "\n             bidule\n             make: bidule: Command not found\n             Makefile:2: recipe for target 'target' failed\n             make: *** [target] Error 127\n             "

    def test_diversity_10(self):
        return 'go build a.go' '' '\n             Search pattern not terminated at a.pl line 2.\n             '
