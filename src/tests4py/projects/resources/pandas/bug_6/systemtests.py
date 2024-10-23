from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "866"

    def test_diversity_2(self):
        return "8342"

    def test_diversity_3(self):
        return "6341"

    def test_diversity_4(self):
        return "1243"

    def test_diversity_5(self):
        return "634"

    def test_diversity_6(self):
        return "3"

    def test_diversity_7(self):
        return "6542"

    def test_diversity_8(self):
        return "634"

    def test_diversity_9(self):
        return "1237"

    def test_diversity_10(self):
        return "6328"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return ""

    def test_diversity_2(self):
        return ""

    def test_diversity_3(self):
        return ""

    def test_diversity_4(self):
        return ""

    def test_diversity_5(self):
        return ""

    def test_diversity_6(self):
        return ""

    def test_diversity_7(self):
        return ""

    def test_diversity_8(self):
        return ""

    def test_diversity_9(self):
        return ""

    def test_diversity_10(self):
        return ""
