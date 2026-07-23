from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('True', 'git commit ubogcrkgs', 'error: pathspec ubogcrkgs did not match any file(s) known to git.')"

    def test_diversity_2(self):
        return "('True', 'git commit dnjzyez', 'error: pathspec dnjzyez did not match any file(s) known to git.')"

    def test_diversity_3(self):
        return "('True', 'git commit ujzzyzu', 'error: pathspec ujzzyzu did not match any file(s) known to git.')"

    def test_diversity_4(self):
        return "('True', 'git commit lkwtcozzi', 'error: pathspec lkwtcozzi did not match any file(s) known to git.')"

    def test_diversity_5(self):
        return "('True', 'git commit zgxthrzgwi', 'error: pathspec zgxthrzgwi did not match any file(s) known to git.')"

    def test_diversity_6(self):
        return "('True', 'git commit hmbxmqhj', 'error: pathspec hmbxmqhj did not match any file(s) known to git.')"

    def test_diversity_7(self):
        return "('True', 'git commit gihzekpvb', 'error: pathspec gihzekpvb did not match any file(s) known to git.')"

    def test_diversity_8(self):
        return "('True', 'git commit dmohflhdh', 'error: pathspec dmohflhdh did not match any file(s) known to git.')"

    def test_diversity_9(self):
        return "('True', 'git commit hixjuk', 'error: pathspec hixjuk did not match any file(s) known to git.')"

    def test_diversity_10(self):
        return "('True', 'git commit yyyes', 'error: pathspec yyyes did not match any file(s) known to git.')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '(\'True\', \'git commit qjbzpwr\', "error: pathspec qjbzpwr did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_2(self):
        return '(\'True\', \'git commit mbddhpzysz\', "error: pathspec mbddhpzysz did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_3(self):
        return '(\'True\', \'git commit vpxgdrqm\', "error: pathspec vpxgdrqm did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_4(self):
        return '(\'True\', \'git commit iqzlfast\', "error: pathspec iqzlfast did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_5(self):
        return '(\'True\', \'git commit hjgzjchxxv\', "error: pathspec hjgzjchxxv did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_6(self):
        return '(\'True\', \'git commit guwwagss\', "error: pathspec guwwagss did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_7(self):
        return '(\'True\', \'git commit vcogxkbiu\', "error: pathspec vcogxkbiu did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_8(self):
        return '(\'True\', \'git commit brtbetubq\', "error: pathspec brtbetubq did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_9(self):
        return '(\'True\', \'git commit ydxrn\', "error: pathspec ydxrn did not match any file(s) known to git. Did you forget to \'git add\'?")'

    def test_diversity_10(self):
        return '(\'True\', \'git commit zynnitmggx\', "error: pathspec zynnitmggx did not match any file(s) known to git. Did you forget to \'git add\'?")'
