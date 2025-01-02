from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1253"

    def test_diversity_2(self):
        return "241"

    def test_diversity_3(self):
        return "36"

    def test_diversity_4(self):
        return "7457"

    def test_diversity_5(self):
        return "453"

    def test_diversity_6(self):
        return "765"

    def test_diversity_7(self):
        return "532"

    def test_diversity_8(self):
        return "3"

    def test_diversity_9(self):
        return "3242"

    def test_diversity_10(self):
        return "11"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "123 'param'"

    def test_diversity_2(self):
        return "5325 'param'"

    def test_diversity_3(self):
        return "645 'param'"

    def test_diversity_4(self):
        return "4234 'param'"

    def test_diversity_5(self):
        return "111 'param'"

    def test_diversity_6(self):
        return "33 'param'"

    def test_diversity_7(self):
        return "4 'param'"

    def test_diversity_8(self):
        return "546 'param'"

    def test_diversity_9(self):
        return "1242 'param'"

    def test_diversity_10(self):
        return "6765 'param'"
