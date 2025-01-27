from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "52 0.5"

    def test_diversity_2(self):
        return "65 0.5"

    def test_diversity_3(self):
        return "652 0.5"

    def test_diversity_4(self):
        return "6 0.5"

    def test_diversity_5(self):
        return "62 0.5"

    def test_diversity_6(self):
        return "14 0.5"

    def test_diversity_7(self):
        return "2 0.5"

    def test_diversity_8(self):
        return "5 0.5"

    def test_diversity_9(self):
        return "1652 0.5"

    def test_diversity_10(self):
        return "6521 0.5"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "781 1.0"

    def test_diversity_2(self):
        return "652 1.0"

    def test_diversity_3(self):
        return "6 1.0"

    def test_diversity_4(self):
        return "52 1.0"

    def test_diversity_5(self):
        return "65 1.0"

    def test_diversity_6(self):
        return "2 1.0"

    def test_diversity_7(self):
        return "5 1.0"

    def test_diversity_8(self):
        return "69 1.0"

    def test_diversity_9(self):
        return "62 1.0"

    def test_diversity_10(self):
        return "752 1.0"
