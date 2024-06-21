from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "190 191 [True, True, True]"

    def test_diversity_2(self):
        return "190 191 [True, True, True]"

    def test_diversity_3(self):
        return "190 191 [True, True, True]"

    def test_diversity_4(self):
        return "190 191 [True, True, True]"

    def test_diversity_5(self):
        return "190 191 [True, True, True]"

    def test_diversity_6(self):
        return "190 191 [True, True, True]"

    def test_diversity_7(self):
        return "190 191 [True, True, True]"

    def test_diversity_8(self):
        return "190 191 [True, True, True]"

    def test_diversity_9(self):
        return "190 191 [True, True, True]"

    def test_diversity_10(self):
        return "190 191 [True, True, True]"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "190 191 [False, False, False]"

    def test_diversity_2(self):
        return "190 191 [False, False, False]"

    def test_diversity_3(self):
        return "190 191 [False, False, False]"

    def test_diversity_4(self):
        return "190 191 [False, False, False]"

    def test_diversity_5(self):
        return "190 191 [False, False, False]"

    def test_diversity_6(self):
        return "190 191 [False, False, False]"

    def test_diversity_7(self):
        return "190 191 [False, False, False]"

    def test_diversity_8(self):
        return "190 191 [False, False, False]"

    def test_diversity_9(self):
        return "190 191 [False, False, False]"

    def test_diversity_10(self):
        return "190 191 [False, False, False]"
