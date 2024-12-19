from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1 3 7 5 3 [0, 1, 0, 0, 2]"

    def test_diversity_2(self):
        return "23 45 89 43 21 [0, 1, 0, 0, 2]"

    def test_diversity_3(self):
        return "13 35 79 53 31 [0, 1, 0, 0, 2]"

    def test_diversity_4(self):
        return "12 34 78 54 32 [0, 1, 0, 0, 2]"

    def test_diversity_5(self):
        return "3 5 9 3 1 [0, 1, 0, 0, 2]"

    def test_diversity_6(self):
        return "2 4 8 4 2 [0, 1, 0, 0, 2]"

    def test_diversity_7(self):
        return "123 35 79 54 31 [0, 1, 0, 0, 2]"

    def test_diversity_8(self):
        return "12 34 78 53 321 [0, 1, 0, 0, 2]"

    def test_diversity_9(self):
        return "3 35 79 54 32 [0, 1, 0, 0, 2]"

    def test_diversity_10(self):
        return "12 34 78 43 31 [0, 1, 0, 0, 2]"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "12 34 78 54 32 [[0], [1], [2], [3], [4]]"

    def test_diversity_2(self):
        return "23 45 89 43 21 [[0], [1], [2], [3], [4]]"

    def test_diversity_3(self):
        return "13 35 79 53 21 [[0], [1], [2], [3], [4]]"

    def test_diversity_4(self):
        return "1 3 7 5 1 [[0], [1], [2], [3], [4]]"

    def test_diversity_5(self):
        return "3 3 9 53 31 [[0], [1], [2], [3], [4]]"

    def test_diversity_6(self):
        return "13 35 78 53 1 [[0], [1], [2], [3], [4]]"

    def test_diversity_7(self):
        return "3 35 7 54 31 [[0], [1], [2], [3], [4]]"

    def test_diversity_8(self):
        return "23 45 79 53 21 [[0], [1], [2], [3], [4]]"

    def test_diversity_9(self):
        return "3 3 9 3 3 [[0], [1], [2], [3], [4]]"

    def test_diversity_10(self):
        return "137 354 79 53 321 [[0], [1], [2], [3], [4]]"
