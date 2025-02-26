from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "7623 0.3"

    def test_diversity_2(self):
        return "6712 0.3"

    def test_diversity_3(self):
        return "123 0.3"

    def test_diversity_4(self):
        return "2345 0.3"

    def test_diversity_5(self):
        return "423 0.3"

    def test_diversity_6(self):
        return "23 0.3"

    def test_diversity_7(self):
        return "5 0.3"

    def test_diversity_8(self):
        return "62 0.3"

    def test_diversity_9(self):
        return "423 0.3"

    def test_diversity_10(self):
        return "543 0.3"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "300 1.0"

    def test_diversity_2(self):
        return "1241 1.0"

    def test_diversity_3(self):
        return "76 1.0"

    def test_diversity_4(self):
        return "5231 1.0"

    def test_diversity_5(self):
        return "34 1.0"

    def test_diversity_6(self):
        return "542 1.0"

    def test_diversity_7(self):
        return "73 1.0"

    def test_diversity_8(self):
        return "763 1.0"

    def test_diversity_9(self):
        return "723 1.0"

    def test_diversity_10(self):
        return "23 1.0"
