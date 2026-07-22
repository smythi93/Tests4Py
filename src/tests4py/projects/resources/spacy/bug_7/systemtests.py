from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '10 4 7 6 9'

    def test_diversity_2(self):
        return '11 0 4 2 6'

    def test_diversity_3(self):
        return '8 2 4 3 5'

    def test_diversity_4(self):
        return '5 0 2 1 3'

    def test_diversity_5(self):
        return '11 1 4 3 6'

    def test_diversity_6(self):
        return '11 5 9 7 11'

    def test_diversity_7(self):
        return '10 4 8 6 10'

    def test_diversity_8(self):
        return '5 1 3 2 4'

    def test_diversity_9(self):
        return '6 2 4 3 5'

    def test_diversity_10(self):
        return '11 1 5 2 6'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '7 1 4 1 3'

    def test_diversity_2(self):
        return '9 2 7 3 5'

    def test_diversity_3(self):
        return '7 1 6 1 5'

    def test_diversity_4(self):
        return '9 5 9 7 8'

    def test_diversity_5(self):
        return '6 3 6 5 6'

    def test_diversity_6(self):
        return '6 2 6 3 6'

    def test_diversity_7(self):
        return '9 0 5 1 2'

    def test_diversity_8(self):
        return '9 5 9 5 8'

    def test_diversity_9(self):
        return '10 4 9 5 8'

    def test_diversity_10(self):
        return '7 3 6 4 6'
