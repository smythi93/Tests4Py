from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '2 6 9 3 2 last'

    def test_diversity_2(self):
        return '3 6 9 3 2 last'

    def test_diversity_3(self):
        return '2 4 8 2 2 last'

    def test_diversity_4(self):
        return '2 6 9 3 2 first'

    def test_diversity_5(self):
        return '3 5 10 3 2 first'

    def test_diversity_6(self):
        return '2 8 7 4 3 last'

    def test_diversity_7(self):
        return '3 6 12 3 2 last'

    def test_diversity_8(self):
        return '2 5 9 3 2 first'

    def test_diversity_9(self):
        return '2 6 11 2 2 last'

    def test_diversity_10(self):
        return '3 7 8 3 2 first'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '1 6 9 3 2 last'

    def test_diversity_2(self):
        return '1 6 9 3 2 first'

    def test_diversity_3(self):
        return '1 4 8 2 2 last'

    def test_diversity_4(self):
        return '1 5 10 3 2 first'

    def test_diversity_5(self):
        return '1 8 7 4 3 last'

    def test_diversity_6(self):
        return '1 6 12 3 2 last'

    def test_diversity_7(self):
        return '1 5 9 3 2 first'

    def test_diversity_8(self):
        return '1 6 11 2 2 last'

    def test_diversity_9(self):
        return '1 7 8 3 2 first'

    def test_diversity_10(self):
        return '1 3 9 3 2 last'
