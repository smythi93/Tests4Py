from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "3 612 412"

    def test_diversity_2(self):
        return "1 234 777"

    def test_diversity_3(self):
        return "98 1 23"

    def test_diversity_4(self):
        return "66 8 999"

    def test_diversity_5(self):
        return "32 22 1"

    def test_diversity_6(self):
        return "5 321 1"

    def test_diversity_7(self):
        return "54 1 3"

    def test_diversity_8(self):
        return "22 99 1"

    def test_diversity_9(self):
        return "533 123 33"

    def test_diversity_10(self):
        return "66 12 54"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "32 66"

    def test_diversity_2(self):
        return "412 121"

    def test_diversity_3(self):
        return "166 665"

    def test_diversity_4(self):
        return "433 788"

    def test_diversity_5(self):
        return "5 675"

    def test_diversity_6(self):
        return "645 123"

    def test_diversity_7(self):
        return "26 123"

    def test_diversity_8(self):
        return "132 64"

    def test_diversity_9(self):
        return "12 67"

    def test_diversity_10(self):
        return "11 43"
