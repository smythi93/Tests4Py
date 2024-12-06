from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "79 4 1"

    def test_diversity_2(self):
        return "78 65 1"

    def test_diversity_3(self):
        return "789 654 1"

    def test_diversity_4(self):
        return "79 64 1"

    def test_diversity_5(self):
        return "9 4 1"

    def test_diversity_6(self):
        return "789 4 1"

    def test_diversity_7(self):
        return "7 654 1"

    def test_diversity_8(self):
        return "789 54 1"

    def test_diversity_9(self):
        return "89 654 1"

    def test_diversity_10(self):
        return "44 64 1"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "2 8 0"

    def test_diversity_2(self):
        return "33 65 0"

    def test_diversity_3(self):
        return "2 865 0"

    def test_diversity_4(self):
        return "233 8 0"

    def test_diversity_5(self):
        return "23 65 0"

    def test_diversity_6(self):
        return "3 85 0"

    def test_diversity_7(self):
        return "23 6 0"

    def test_diversity_8(self):
        return "123 15 0"

    def test_diversity_9(self):
        return "66 742 0"

    def test_diversity_10(self):
        return "84 33 0"
