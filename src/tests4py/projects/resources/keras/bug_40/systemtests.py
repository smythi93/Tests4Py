from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '3 6 5 7 seq'

    def test_diversity_2(self):
        return '2 5 4 3 seq'

    def test_diversity_3(self):
        return '6 3 7 4 last'

    def test_diversity_4(self):
        return '4 8 3 5 seq'

    def test_diversity_5(self):
        return '5 2 6 6 last'

    def test_diversity_6(self):
        return '8 4 2 8 seq'

    def test_diversity_7(self):
        return '3 7 5 5 last'

    def test_diversity_8(self):
        return '7 3 4 2 seq'

    def test_diversity_9(self):
        return '2 8 8 3 last'

    def test_diversity_10(self):
        return '6 5 3 6 seq'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '4 4 5 7 seq'

    def test_diversity_2(self):
        return '3 3 4 3 seq'

    def test_diversity_3(self):
        return '5 5 7 4 last'

    def test_diversity_4(self):
        return '6 6 3 5 seq'

    def test_diversity_5(self):
        return '2 2 6 6 last'

    def test_diversity_6(self):
        return '7 7 2 8 seq'

    def test_diversity_7(self):
        return '8 8 5 5 last'

    def test_diversity_8(self):
        return '3 3 4 2 seq'

    def test_diversity_9(self):
        return '4 4 8 3 last'

    def test_diversity_10(self):
        return '5 5 3 6 seq'
