from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "2 float"

    def test_diversity_2(self):
        return "222 float64"

    def test_diversity_3(self):
        return "498 float64"

    def test_diversity_4(self):
        return "129 float64"

    def test_diversity_5(self):
        return "163 float"

    def test_diversity_6(self):
        return "345 float"

    def test_diversity_7(self):
        return "16 float64"

    def test_diversity_8(self):
        return "197 float"

    def test_diversity_9(self):
        return "19 float"

    def test_diversity_10(self):
        return "173 float64"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "477 boolean"

    def test_diversity_2(self):
        return "423 int64"

    def test_diversity_3(self):
        return "216 boolean"

    def test_diversity_4(self):
        return "378 boolean"

    def test_diversity_5(self):
        return "471 Int64"

    def test_diversity_6(self):
        return "3 int64"

    def test_diversity_7(self):
        return "61 boolean"

    def test_diversity_8(self):
        return "10 Int64"

    def test_diversity_9(self):
        return "35 int64"

    def test_diversity_10(self):
        return "42 boolean"
