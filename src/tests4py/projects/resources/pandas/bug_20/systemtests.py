from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "32 11/4/1500"

    def test_diversity_2(self):
        return "66 2/5/1500"

    def test_diversity_3(self):
        return "433 1/7/1500"

    def test_diversity_4(self):
        return "987 7/11/1500"

    def test_diversity_5(self):
        return "777 6/13/1500"

    def test_diversity_6(self):
        return "75 3/14/1500"

    def test_diversity_7(self):
        return "64 2/21/1500"

    def test_diversity_8(self):
        return "23 8/22/1500"

    def test_diversity_9(self):
        return "534 9/26/1500"

    def test_diversity_10(self):
        return "54 10/27/1500"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "3 11/27/2000"

    def test_diversity_2(self):
        return "54 10/1/2000"

    def test_diversity_3(self):
        return "874 11/1/2000"

    def test_diversity_4(self):
        return "848 11/17/2000"

    def test_diversity_5(self):
        return "86 10/20/2000"

    def test_diversity_6(self):
        return "46 5/5/2000"

    def test_diversity_7(self):
        return "23 1/21/2000"

    def test_diversity_8(self):
        return "1467 11/11/2000"

    def test_diversity_9(self):
        return "2716 2/10/2000"

    def test_diversity_10(self):
        return "6512 7/27/2000"
