from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1.5 3.0 3.5 4.0 5.0 1.5 3.5 3.0 4.0"

    def test_diversity_2(self):
        return "1.51 3.01 3.51 4.01 5.01 1.51 3.51 3.01 4.01"

    def test_diversity_3(self):
        return "1.52 3.02 3.52 4.02 5.02 1.52 3.52 3.02 4.02"

    def test_diversity_4(self):
        return "1.53 3.03 3.53 4.03 5.03 1.53 3.53 3.03 4.03"

    def test_diversity_5(self):
        return "1.54 3.04 3.54 4.04 5.04 1.54 3.54 3.04 4.04"

    def test_diversity_6(self):
        return "1.55 3.05 3.55 4.05 5.05 1.55 3.55 3.05 4.05"

    def test_diversity_7(self):
        return "1.56 3.06 3.56 4.06 5.06 1.56 3.56 3.06 4.06"

    def test_diversity_8(self):
        return "1.57 3.07 3.57 4.07 5.07 1.57 3.57 3.07 4.07"

    def test_diversity_9(self):
        return "1.58 3.08 3.58 4.08 5.08 1.58 3.58 3.08 4.08"

    def test_diversity_10(self):
        return "1.59 3.09 3.59 4.09 5.09 1.59 3.59 3.09 4.09"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "1.5 3.0 3.5 4.0 5.0 1.5 3.5 3.0 5.0"

    def test_diversity_2(self):
        return "1.51 3.01 3.51 4.01 5.01 1.51 3.51 3.01 5.01"

    def test_diversity_3(self):
        return "1.52 3.02 3.52 4.02 5.02 1.52 3.52 3.02 5.02"

    def test_diversity_4(self):
        return "1.53 3.03 3.53 4.03 5.03 1.53 3.53 3.03 5.03"

    def test_diversity_5(self):
        return "1.54 3.04 3.54 4.04 5.04 1.54 3.54 3.04 5.04"

    def test_diversity_6(self):
        return "1.55 3.05 3.55 4.05 5.05 1.55 3.55 3.05 5.05"

    def test_diversity_7(self):
        return "1.56 3.06 3.56 4.06 5.06 1.56 3.56 3.06 5.06"

    def test_diversity_8(self):
        return "1.57 3.07 3.57 4.07 5.07 1.57 3.57 3.07 5.07"

    def test_diversity_9(self):
        return "1.58 3.08 3.58 4.08 5.08 1.58 3.58 3.08 5.08"

    def test_diversity_10(self):
        return "1.59 3.09 3.59 4.09 5.09 1.59 3.59 3.09 5.09"
