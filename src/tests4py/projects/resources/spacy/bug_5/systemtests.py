from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "rtjhiertg"

    def test_diversity_2(self):
        return "hfuhw"

    def test_diversity_3(self):
        return "jhdashjdgasj"

    def test_diversity_4(self):
        return "MDFJBHSS"

    def test_diversity_5(self):
        return "ERKLGEIHGN"

    def test_diversity_6(self):
        return "ERNGKJEG"

    def test_diversity_7(self):
        return "erjkfhwi"

    def test_diversity_8(self):
        return "ewfrwhehbe"

    def test_diversity_9(self):
        return "rthtrhgergw"

    def test_diversity_10(self):
        return "gergrgerw"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "rfgnkwrbkw TypeError"

    def test_diversity_2(self):
        return "jkwehgfuew TypeError"

    def test_diversity_3(self):
        return "wrjkgwhfnw TypeError"

    def test_diversity_4(self):
        return "wfgguwww TypeError"

    def test_diversity_5(self):
        return "ERJHGUgshg TypeError"

    def test_diversity_6(self):
        return "erjghuer TypeError"

    def test_diversity_7(self):
        return "akjsahjDSFSD TypeError"

    def test_diversity_8(self):
        return "KJWEFIW TypeError"

    def test_diversity_9(self):
        return "SDKJFHDSBFK TypeError"

    def test_diversity_10(self):
        return "jehwbfwej TypeError"
