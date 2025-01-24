from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(6,) 11.0"

    def test_diversity_2(self):
        return "(6, 3, 1) 954.0"

    def test_diversity_3(self):
        return "(6,) 87.0"

    def test_diversity_4(self):
        return "(6,) 9.0"

    def test_diversity_5(self):
        return "(6, 3) 12.0"

    def test_diversity_6(self):
        return "(6,) 67.0"

    def test_diversity_7(self):
        return "(6, 3) 123.0"

    def test_diversity_8(self):
        return "(6, 3, 1) 225.0"

    def test_diversity_9(self):
        return "(6,) 15.0"

    def test_diversity_10(self):
        return "(6, 3, 1) 5.0"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "(6, 3) 99"

    def test_diversity_2(self):
        return "(6,) 653"

    def test_diversity_3(self):
        return "(6, 3, 1) 789"

    def test_diversity_4(self):
        return "(6, 3) 123"

    def test_diversity_5(self):
        return "(6, 3, 1) 654"

    def test_diversity_6(self):
        return "(6,) 3654"

    def test_diversity_7(self):
        return "(6, 3) 67"

    def test_diversity_8(self):
        return "(6,) 5"

    def test_diversity_9(self):
        return "(6, 3) 76"

    def test_diversity_10(self):
        return "(6,) 94"
