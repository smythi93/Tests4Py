from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1.0 0.0 0.3 0.7"

    def test_diversity_2(self):
        return "1.0 0.0 0.2 0.8"

    def test_diversity_3(self):
        return "2.0 0.0 0.5 1.5"

    def test_diversity_4(self):
        return "5.0 1.0 2.0 4.0"

    def test_diversity_5(self):
        return "10.0 0.0 3.0 7.0"

    def test_diversity_6(self):
        return "1.0 -1.0 -0.5 0.5"

    def test_diversity_7(self):
        return "0.0 -2.0 -1.5 -0.5"

    def test_diversity_8(self):
        return "100.0 50.0 60.0 90.0"

    def test_diversity_9(self):
        return "3.0 2.0 2.3 2.7"

    def test_diversity_10(self):
        return "1.0 0.0 0.4 0.6"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "0.0 1.0 0.3 0.7"

    def test_diversity_2(self):
        return "0.0 2.0 0.5 1.5"

    def test_diversity_3(self):
        return "-1.0 1.0 -0.5 0.5"

    def test_diversity_4(self):
        return "1.0 5.0 2.0 4.0"

    def test_diversity_5(self):
        return "0.0 10.0 3.0 7.0"

    def test_diversity_6(self):
        return "-2.0 0.0 -1.5 -0.5"

    def test_diversity_7(self):
        return "50.0 100.0 60.0 90.0"

    def test_diversity_8(self):
        return "2.0 3.0 2.3 2.7"

    def test_diversity_9(self):
        return "0.0 1.0 0.4 0.6"

    def test_diversity_10(self):
        return "-5.0 5.0 -1.0 1.0"

