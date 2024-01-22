from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):

    def test_diversity_1(self):
        return "pip inst@ll pstats"

    def test_diversity_2(self):
        return "pip -dowNLoad cgi"

    def test_diversity_3(self):
        return "pip h@sh audioop"

    def test_diversity_4(self):
        return "pip FR33ze cgi"

    def test_diversity_5(self):
        return "pip l1st zipimport"

    def test_diversity_6(self):
        return "pip sh0w-> pyexpat "

    def test_diversity_7(self):
        return "pip ~d3bug crypt"

    def test_diversity_8(self):
        return "pip l1st pathlib"

    def test_diversity_9(self):
        return "pip -dowNLoad trace"

    def test_diversity_10(self):
        return "pip h@sh audioop"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "pip whel calendar"

    def test_diversity_2(self):
        return "pip cahe ast"

    def test_diversity_3(self):
        return "pip debg venv"

    def test_diversity_4(self):
        return "pip serch pstats"

    def test_diversity_5(self):
        return "pip hsh cgi"

    def test_diversity_6(self):
        return "pip instll warnings"

    def test_diversity_7(self):
        return "pip cche pathlib"

    def test_diversity_8(self):
        return "pip whel unicodedata"

    def test_diversity_9(self):
        return "pip unstall pyexpat"

    def test_diversity_10(self):
        return "pip show trace"
