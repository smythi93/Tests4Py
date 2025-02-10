from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "453 None"

    def test_diversity_2(self):
        return "527 None"

    def test_diversity_3(self):
        return "65 None"

    def test_diversity_4(self):
        return "90 None"

    def test_diversity_5(self):
        return "179 None"

    def test_diversity_6(self):
        return "33 None"

    def test_diversity_7(self):
        return "2 None"

    def test_diversity_8(self):
        return "443 None"

    def test_diversity_9(self):
        return "953 None"

    def test_diversity_10(self):
        return "9 None"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "876 1"

    def test_diversity_2(self):
        return "700 1"

    def test_diversity_3(self):
        return "543 1"

    def test_diversity_4(self):
        return "11 1"

    def test_diversity_5(self):
        return "877 1"

    def test_diversity_6(self):
        return "4321 1"

    def test_diversity_7(self):
        return "14 1"

    def test_diversity_8(self):
        return "43 1"

    def test_diversity_9(self):
        return "5412 1"

    def test_diversity_10(self):
        return "761 1"
