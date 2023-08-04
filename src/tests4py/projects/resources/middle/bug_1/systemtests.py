from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "4\n2\n5"

    def test_diversity_2(self):
        return "64\n63\n125"

    def test_diversity_3(self):
        return "-3\n-45\n12"

    def test_diversity_4(self):
        return "2\n1\n3"

    def test_diversity_5(self):
        return "0\n-1\n1"

    def test_diversity_6(self):
        return "1\n0\n64"

    def test_diversity_7(self):
        return "5\n4\n6"

    def test_diversity_8(self):
        return "0\n-1000\n1000"

    def test_diversity_9(self):
        return "9\n8\n10"

    def test_diversity_10(self):
        return "-5\n-6\n-4"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "2\n4\n5"

    def test_diversity_2(self):
        return "63\n125\n64"

    def test_diversity_3(self):
        return "12\n-3\n-45"

    def test_diversity_4(self):
        return "2\n3\n1"

    def test_diversity_5(self):
        return "0\n1\n-1"

    def test_diversity_6(self):
        return "0\n1\n64"

    def test_diversity_7(self):
        return "4\n6\n5"

    def test_diversity_8(self):
        return "-1000\n0\n1000"

    def test_diversity_9(self):
        return "9\n10\n8"

    def test_diversity_10(self):
        return "-4\n-5\n-6"
