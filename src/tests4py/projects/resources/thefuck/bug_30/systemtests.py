from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('xOKkyHfhPzlC a.c', '\\n             a.sh:2: command not found: foo\\n             ', True)"

    def test_diversity_2(self):
        return '(\'vHKFvYDhERnU fuck.js asdf qwer\', "\\n             a.c: In function \'main\':\\n             a.c:3:1: error: expected expression before \'}\' token\\n              }\\n               ^\\n             ", True)'

    def test_diversity_3(self):
        return '(\'TgJWQCWA a.c\', \'\\n             awk: ./a:2: BEGIN { print "Hello, world!" + }\\n             awk: ./a:2:                                 ^ syntax error\\n             \', True)'

    def test_diversity_4(self):
        return "('WnNGIut a.py', '\\n             a.rb:3: syntax error, unexpected keyword_end\\n             ', True)"

    def test_diversity_5(self):
        return "('aWFhYElTwa a.rs', '\\n             a.c:3:1: error: expected expression\\n             }\\n             ^\\n             ', True)"

    def test_diversity_6(self):
        return "('kNpysMVDPjWB a.c', '\\n             syntax error at a.pl line 3, at EOF\\n             Execution of a.pl aborted due to compilation errors.\\n             ', True)"

    def test_diversity_7(self):
        return '(\'./a\', "\\n             a.c: In function \'main\':\\n             a.c:3:1: error: expected expression before \'}\' token\\n              }\\n               ^\\n             ", True)'

    def test_diversity_8(self):
        return '(\'OKUejDyOPT a.pl\', "\\n             can\'t load package:\\n             a.go:1:1: expected \'package\', found \'+\'\\n             ", True)'

    def test_diversity_9(self):
        return '(\'cFwBKWBRWZsReqy a.py\', "\\n             lua: a.lua:2: unexpected symbol near \'+\'\\n             ", True)'

    def test_diversity_10(self):
        return '(\'hGqkuZBnR a.lua\', "\\n             lua: a.lua:2: unexpected symbol near \'+\'\\n             ", True)'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('VZKrGIFvzbRXKzD a.sh', '\\n             /Users/pablo/Workspace/barebones/fuck.js:2\\n             conole.log(arg);  // this should read console.log(arg);\\n             ^\\n             ReferenceError: conole is not defined\\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\\n                 at Array.forEach (native)\\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\\n                 at Module._compile (module.js:460:26)\\n                 at Object.Module._extensions..js (module.js:478:10)\\n                 at Module.load (module.js:355:32)\\n                 at Function.Module._load (module.js:310:12)\\n                 at Function.Module.runMain (module.js:501:10)\\n                 at startup (node.js:129:16)\\n                 at node.js:814:3\\n             ', False)"

    def test_diversity_2(self):
        return '(\'PSigYqtMF a.pl\', "\\n             fish: Unknown command \'foo\'\\n             /tmp/fix-error/a.sh (line 2): foo\\n                                           ^\\n             ", False)'

    def test_diversity_3(self):
        return "('gnttyxJnqkS a.c', '\\n             llc: a.ll:1:1: error: expected top-level entity\\n             +\\n             ^\\n             ', False)"

    def test_diversity_4(self):
        return "('PwRGLyNUP a.sh', '\\n             /Users/pablo/Workspace/barebones/fuck.js:2\\n             conole.log(arg);  // this should read console.log(arg);\\n             ^\\n             ReferenceError: conole is not defined\\n                 at /Users/pablo/Workspace/barebones/fuck.js:2:5\\n                 at Array.forEach (native)\\n                 at Object.<anonymous> (/Users/pablo/Workspace/barebones/fuck.js:1:85)\\n                 at Module._compile (module.js:460:26)\\n                 at Object.Module._extensions..js (module.js:478:10)\\n                 at Module.load (module.js:355:32)\\n                 at Function.Module._load (module.js:310:12)\\n                 at Function.Module.runMain (module.js:501:10)\\n                 at startup (node.js:129:16)\\n                 at node.js:814:3\\n             ', False)"

    def test_diversity_5(self):
        return '(\'SiwgDdsRjMYFO a.sh\', "\\n             lua: a.lua:2: unexpected symbol near \'+\'\\n             ", False)'

    def test_diversity_6(self):
        return "('AMWzB build a.go', '\\n             a.sh: line 2: foo: command not found\\n             ', False)"

    def test_diversity_7(self):
        return "('XSKGThseVSCet a.sh', '\\n             Search pattern not terminated at a.pl line 2.\\n             ', False)"

    def test_diversity_8(self):
        return '(\'jHnJhUJfA a.rs\', \'\\n               File "a.py", line 2\\n                   +\\n                       ^\\n             SyntaxError: invalid syntax\\n             \', False)'

    def test_diversity_9(self):
        return "('UzrBjuZrwEHquMz a.pl', '\\n             llc: a.ll:1:1: error: expected top-level entity\\n             +\\n             ^\\n             ', False)"

    def test_diversity_10(self):
        return "('DVcmwX a.lua', '\\n             a.c:3:1: error: expected expression\\n             }\\n             ^\\n             ', False)"
