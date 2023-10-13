from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(3-1)*(5*2)"

    def test_diversity_2(self):
        return "(3-1)*(5*2)"

    def test_diversity_3(self):
        return "(3-1)*(5*2)"

    def test_diversity_4(self):
        return "(3-1)*(5*2)"

    def test_diversity_5(self):
        return "(3-1)*(5*2)"

    def test_diversity_6(self):
        return "(3-1)*(5*2)"

    def test_diversity_7(self):
        return "(3-1)*(5*2)"

    def test_diversity_8(self):
        return "(3-1)*(5*2)"

    def test_diversity_9(self):
        return "(3-1)*(5*2)"

    def test_diversity_10(self):
        return "(3-1)*(5*2)"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_2(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_3(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_4(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_5(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_6(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_7(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_8(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_9(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "

    def test_diversity_10(self):
        return " ( 30 / 5 ) / ( 3 + 3 ) "
