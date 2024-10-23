from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "[1, 2, 765] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_2(self):
        return "[1, 2, 2] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_3(self):
        return "[1, 2, 222] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_4(self):
        return "[1, 2, 645] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_5(self):
        return "[1, 2, 867] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_6(self):
        return "[1, 2, 765] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_7(self):
        return "[1, 2, 534] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_8(self):
        return "[1, 2, 3123] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_9(self):
        return "[1, 2, 543] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_10(self):
        return "[1, 2, 63] [0, 1, 0, 1, 0, 1, 0, 1] [0, 1, 0, 1, 0, 1, 0, 1]"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "[1, 2, 623] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_2(self):
        return "[1, 2, 65] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_3(self):
        return "[1, 2, 5555] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_4(self):
        return "[1, 2, 232] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_5(self):
        return "[1, 2, 654] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_6(self):
        return "[1, 2, 111] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_7(self):
        return "[1, 2, 444] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_8(self):
        return "[1, 2, 76] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_9(self):
        return "[1, 2, 124] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"

    def test_diversity_10(self):
        return "[1, 2, 7654] [1, 2, 5, 6, 9, 10, 13, 14] [0, 1, 0, 1, 0, 1, 0, 1]"
