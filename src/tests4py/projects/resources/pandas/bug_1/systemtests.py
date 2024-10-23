from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "123"

    def test_diversity_2(self):
        return "321"

    def test_diversity_3(self):
        return "65"

    def test_diversity_4(self):
        return "77"

    def test_diversity_5(self):
        return "232"

    def test_diversity_6(self):
        return "545"

    def test_diversity_7(self):
        return "2131"

    def test_diversity_8(self):
        return "5345"

    def test_diversity_9(self):
        return "3628"

    def test_diversity_10(self):
        return "544"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-9695D"

    def test_diversity_2(self):
        return "-4405A"

    def test_diversity_3(self):
        return "3088A"

    def test_diversity_4(self):
        return "3030H"

    def test_diversity_5(self):
        return "2125A"

    def test_diversity_6(self):
        return "7980A"

    def test_diversity_7(self):
        return "2772S"

    def test_diversity_8(self):
        return "7834T"

    def test_diversity_9(self):
        return "8521S"

    def test_diversity_10(self):
        return "-9922W"
