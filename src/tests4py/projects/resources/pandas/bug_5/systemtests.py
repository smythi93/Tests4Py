from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "[131, 132] [133, 134]] ['a', 'b'] ['c', 'd']"

    def test_diversity_2(self):
        return "[99, 100] [101, 102]] ['a', 'b'] ['c', 'd']"

    def test_diversity_3(self):
        return "[1110, 1111] [1112, 1113]] ['a', 'b'] ['c', 'd']"

    def test_diversity_4(self):
        return "[70, 71] [72, 73]] ['a', 'b'] ['c', 'd']"

    def test_diversity_5(self):
        return "[4312, 4313] [4314, 4315]] ['a', 'b'] ['c', 'd']"

    def test_diversity_6(self):
        return "[5678, 5679] [5680, 5681]] ['a', 'b'] ['c', 'd']"

    def test_diversity_7(self):
        return "[838, 839] [840, 841]] ['a', 'b'] ['c', 'd']"

    def test_diversity_8(self):
        return "[1010, 1011] [1012, 1013]] ['a', 'b'] ['c', 'd']"

    def test_diversity_9(self):
        return "[9, 10] [11, 12]] ['a', 'b'] ['c', 'd']"

    def test_diversity_10(self):
        return "[67, 68] [69, 70]] ['a', 'b'] ['c', 'd']"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "[131, 132] [133, 134]] ['a', 'b'] ['a', 'b']"

    def test_diversity_2(self):
        return "[99, 100] [101, 102]] ['a', 'b'] ['a', 'b']"

    def test_diversity_3(self):
        return "[1110, 1111] [1112, 1113]] ['a', 'b'] ['a', 'b']"

    def test_diversity_4(self):
        return "[70, 71] [72, 73]] ['a', 'b'] ['a', 'b']"

    def test_diversity_5(self):
        return "[4312, 4313] [4314, 4315]] ['a', 'b'] ['a', 'b']"

    def test_diversity_6(self):
        return "[5678, 5679] [5680, 5681]] ['a', 'b'] ['a', 'b']"

    def test_diversity_7(self):
        return "[838, 839] [840, 841]] ['a', 'b'] ['a', 'b']"

    def test_diversity_8(self):
        return "[1010, 1011] [1012, 1013]] ['a', 'b'] ['a', 'b']"

    def test_diversity_9(self):
        return "[9, 10] [11, 12]] ['a', 'b'] ['a', 'b']"

    def test_diversity_10(self):
        return "[67, 68] [69, 70]] ['a', 'b'] ['a', 'b']"
