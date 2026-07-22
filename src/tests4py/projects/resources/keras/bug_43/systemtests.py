from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'col 10 8 8 4 7 7 0'

    def test_diversity_2(self):
        return 'col 5 1 3 0 0'

    def test_diversity_3(self):
        return 'col 7 0 5 1 0 3'

    def test_diversity_4(self):
        return 'col 2 1 0 1 1'

    def test_diversity_5(self):
        return 'col 7 5 2 2 4 3 4 4'

    def test_diversity_6(self):
        return 'col 9 3 6 4 5 2 3'

    def test_diversity_7(self):
        return 'col 2 0 0'

    def test_diversity_8(self):
        return 'col 5 1 4 1 4 3'

    def test_diversity_9(self):
        return 'col 12 9 8 2'

    def test_diversity_10(self):
        return 'col 7 0 0 3 5 2 0 0 2'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'flat 11 3 0 2 8 0 4'

    def test_diversity_2(self):
        return 'flat 2 0 0 1 0 1 0 1 0'

    def test_diversity_3(self):
        return 'flat 4 0 2 3 1 3'

    def test_diversity_4(self):
        return 'flat 4 1 0 0 0 1 3 0'

    def test_diversity_5(self):
        return 'flat 10 4 8 8 6 9 8 4 8'

    def test_diversity_6(self):
        return 'flat 3 2 2 0 1 0 2 2 2'

    def test_diversity_7(self):
        return 'flat 12 6 7'

    def test_diversity_8(self):
        return 'flat 6 3 4 4 2 3'

    def test_diversity_9(self):
        return 'flat 4 3 3 3 3 1 0'

    def test_diversity_10(self):
        return 'flat 11 2 1 10 0 0 8 7 6'
