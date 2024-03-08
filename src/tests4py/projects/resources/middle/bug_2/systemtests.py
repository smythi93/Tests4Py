from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "4 2 5"

    def test_diversity_2(self):
        return "64 63 125"

    def test_diversity_3(self):
        return "-3 -45 12"

    def test_diversity_4(self):
        return "2 1 3"

    def test_diversity_5(self):
        return "0 -1 1"

    def test_diversity_6(self):
        return "1 0 64"

    def test_diversity_7(self):
        return "5 4 6"

    def test_diversity_8(self):
        return "0 -1000 1000"

    def test_diversity_9(self):
        return "9 8 10"

    def test_diversity_10(self):
        return "-5 -6 -4"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "2 4 5"

    def test_diversity_2(self):
        return "63 125 64"

    def test_diversity_3(self):
        return "12 -3 -45"

    def test_diversity_4(self):
        return "2 3 1"

    def test_diversity_5(self):
        return "0 1 -1"

    def test_diversity_6(self):
        return "0 1 64"

    def test_diversity_7(self):
        return "4 6 5"

    def test_diversity_8(self):
        return "-1000 0 1000"

    def test_diversity_9(self):
        return "9 10 8"

    def test_diversity_10(self):
        return "-4 -5 -6"
