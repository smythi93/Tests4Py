from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "30 / (3 - 3)"

    def test_diversity_2(self):
        return "(3 * 5) / 0"

    def test_diversity_3(self):
        return "3 / (4 - 4)"

    def test_diversity_4(self):
        return "7 / (0 * 2)"

    def test_diversity_5(self):
        return "5 / (5 - 5)"

    def test_diversity_6(self):
        return "50 / 0"

    def test_diversity_7(self):
        return "40 / (10 * 0)"

    def test_diversity_8(self):
        return "13 / (0 / 5)"

    def test_diversity_9(self):
        return "(5 + 2) / 0"

    def test_diversity_10(self):
        return "11 / (10 - 10)"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "23 + 45"

    def test_diversity_2(self):
        return "(15 + 30) / 2"

    def test_diversity_3(self):
        return "15 / 3"

    def test_diversity_4(self):
        return "50 - 25"

    def test_diversity_5(self):
        return "27 * (2 - 1)"

    def test_diversity_6(self):
        return "40 - 20"

    def test_diversity_7(self):
        return "80 * 4 / 4"

    def test_diversity_8(self):
        return "(50 + 25) / 3"

    def test_diversity_9(self):
        return "20 + 5 + 5"

    def test_diversity_10(self):
        return "65 + ~ 45 / 9"
