from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1 2 alpha7"

    def test_diversity_2(self):
        return "1 3 bravo12"

    def test_diversity_3(self):
        return "1 4 charlie3"

    def test_diversity_4(self):
        return "1 5 delta9"

    def test_diversity_5(self):
        return "1 6 echo1"

    def test_diversity_6(self):
        return "1 7 foxtrot4"

    def test_diversity_7(self):
        return "1 8 golf6"

    def test_diversity_8(self):
        return "1 9 hotel2"

    def test_diversity_9(self):
        return "1 10 india8"

    def test_diversity_10(self):
        return "1 11 juliet5"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "2 2 kilo3"

    def test_diversity_2(self):
        return "3 4 lima9"

    def test_diversity_3(self):
        return "4 3 mike1"

    def test_diversity_4(self):
        return "5 5 november7"

    def test_diversity_5(self):
        return "6 6 oscar2"

    def test_diversity_6(self):
        return "7 4 papa8"

    def test_diversity_7(self):
        return "8 7 quebec4"

    def test_diversity_8(self):
        return "9 5 romeo6"

    def test_diversity_9(self):
        return "10 8 sierra1"

    def test_diversity_10(self):
        return "12 6 tango3"
