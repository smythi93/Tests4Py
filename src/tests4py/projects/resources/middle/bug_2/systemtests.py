from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "7\n5\n10"

    def test_diversity_2(self):
        return "77\n32\n93"

    def test_diversity_3(self):
        return "-3\n-5\n-2"

    def test_diversity_4(self):
        return "-8\n-10\n-6"

    def test_diversity_5(self):
        return "0\n-1\n1"

    def test_diversity_6(self):
        return "-2\n-3\n-1"

    def test_diversity_7(self):
        return "21\n12\n121"

    def test_diversity_8(self):
        return "0\n-1000\n1000"

    def test_diversity_9(self):
        return "111\n11\n1111"

    def test_diversity_10(self):
        return "5\n3\n7"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "10\n7\n5"

    def test_diversity_2(self):
        return "32\n77\n93"

    def test_diversity_3(self):
        return "-5\n-3\n-2"

    def test_diversity_4(self):
        return "-17\n-10\n-8"

    def test_diversity_5(self):
        return "-1\n0\n1"

    def test_diversity_6(self):
        return "0\n11\n22"

    def test_diversity_7(self):
        return "61\n147\n245"

    def test_diversity_8(self):
        return "-1000\n0\n1000"

    def test_diversity_9(self):
        return "3\n6\n7"

    def test_diversity_10(self):
        return "-2\n-4\n-6"
