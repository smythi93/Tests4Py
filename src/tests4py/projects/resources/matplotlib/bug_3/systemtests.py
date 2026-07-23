from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "o none"

    def test_diversity_2(self):
        return "v none"

    def test_diversity_3(self):
        return "^ none"

    def test_diversity_4(self):
        return "8 none"

    def test_diversity_5(self):
        return "s none"

    def test_diversity_6(self):
        return "p none"

    def test_diversity_7(self):
        return "* none"

    def test_diversity_8(self):
        return "h none"

    def test_diversity_9(self):
        return "H none"

    def test_diversity_10(self):
        return "D none"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "o full"

    def test_diversity_2(self):
        return "v full"

    def test_diversity_3(self):
        return "^ full"

    def test_diversity_4(self):
        return "8 full"

    def test_diversity_5(self):
        return "s full"

    def test_diversity_6(self):
        return "p full"

    def test_diversity_7(self):
        return "* full"

    def test_diversity_8(self):
        return "h full"

    def test_diversity_9(self):
        return "H full"

    def test_diversity_10(self):
        return "d full"
