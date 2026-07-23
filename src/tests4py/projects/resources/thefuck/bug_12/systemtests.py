from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "'False' 'git ubogcrkgs' 'git: not found'"

    def test_diversity_2(self):
        return "'False' 'ls dnjzyez' 'ls: not found'"

    def test_diversity_3(self):
        return "'False' 'cat ujzzyzu' 'cat: not found'"

    def test_diversity_4(self):
        return "'False' 'echo lkwtcozzi' 'echo: not found'"

    def test_diversity_5(self):
        return "'False' 'cp zgxthrzgwi' 'cp: not found'"

    def test_diversity_6(self):
        return "'False' 'mv hmbxmqhj' 'mv: not found'"

    def test_diversity_7(self):
        return "'False' 'rm gihzekpvb' 'rm: not found'"

    def test_diversity_8(self):
        return "'False' 'date dmohflhdh' 'date: not found'"

    def test_diversity_9(self):
        return "'False' 'grep hixjuk' 'grep: not found'"

    def test_diversity_10(self):
        return "'False' 'sort yyyes' 'sort: not found'"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "'True' 'gitt xeptudhdh' 'gitt: not found'"

    def test_diversity_2(self):
        return "'True' 'lss yftbvuydd' 'lss: not found'"

    def test_diversity_3(self):
        return "'True' 'catt vrvzfbe' 'catt: not found'"

    def test_diversity_4(self):
        return "'True' 'echoo gpsfujk' 'echoo: not found'"

    def test_diversity_5(self):
        return "'True' 'rmm gjundkdo' 'rmm: not found'"

    def test_diversity_6(self):
        return "'True' 'datee dkkbw' 'datee: not found'"

    def test_diversity_7(self):
        return "'True' 'grepp vzynonqnv' 'grepp: not found'"

    def test_diversity_8(self):
        return "'True' 'sortt nbgosppu' 'sortt: not found'"

    def test_diversity_9(self):
        return "'True' 'headd euhutgtge' 'headd: not found'"

    def test_diversity_10(self):
        return "'True' 'taill mjsnwcsuc' 'taill: not found'"
