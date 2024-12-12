from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "123 123 81"

    def test_diversity_2(self):
        return "66 66 199"

    def test_diversity_3(self):
        return "93 93 445"

    def test_diversity_4(self):
        return "3 3 98"

    def test_diversity_5(self):
        return "45 45 923"

    def test_diversity_6(self):
        return "999 999 32"

    def test_diversity_7(self):
        return "594 594 56"

    def test_diversity_8(self):
        return "948 948 858"

    def test_diversity_9(self):
        return "746 746 4"

    def test_diversity_10(self):
        return "98 98 9"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "135 135 135"

    def test_diversity_2(self):
        return "15 15 15"

    def test_diversity_3(self):
        return "13 13 13"

    def test_diversity_4(self):
        return "5 5 5"

    def test_diversity_5(self):
        return "35 35 35"

    def test_diversity_6(self):
        return "3 3 3"

    def test_diversity_7(self):
        return "33 33 33"

    def test_diversity_8(self):
        return "1 1 1"

    def test_diversity_9(self):
        return "345 345 345"

    def test_diversity_10(self):
        return "76 76 76"
