from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return main("sqrt(-81)")

    def test_diversity_2(self):
        return main("sqrt(-81)")

    def test_diversity_3(self):
        return main("sqrt(-81)")

    def test_diversity_4(self):
        return main("sqrt(-81)")

    def test_diversity_5(self):
        return main("sqrt(-81)")

    def test_diversity_6(self):
        return main("sqrt(-81)")

    def test_diversity_7(self):
        return main("sqrt(-81)")

    def test_diversity_8(self):
        return main("sqrt(-81)")

    def test_diversity_9(self):
        return main("sqrt(-81)")

    def test_diversity_10(self):
        return main("sqrt(-81)")


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return main("sqrt(81)")

    def test_diversity_2(self):
        return main("sqrt(81)")

    def test_diversity_3(self):
        return main("sqrt(81)")

    def test_diversity_4(self):
        return main("sqrt(81)")

    def test_diversity_5(self):
        return main("sqrt(81)")

    def test_diversity_6(self):
        return main("sqrt(81)")

    def test_diversity_7(self):
        return main("sqrt(81)")

    def test_diversity_8(self):
        return main("sqrt(81)")

    def test_diversity_9(self):
        return main("sqrt(81)")

    def test_diversity_10(self):
        return main("sqrt(81)")
