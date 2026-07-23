from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '14 5 1 1'

    def test_diversity_2(self):
        return '9 2 1 1'

    def test_diversity_3(self):
        return '10 4 1 1'

    def test_diversity_4(self):
        return '8 2 1 1'

    def test_diversity_5(self):
        return '10 3 1 1'

    def test_diversity_6(self):
        return '17 5 1 1'

    def test_diversity_7(self):
        return '8 6 1 1'

    def test_diversity_8(self):
        return '10 5 1 1'

    def test_diversity_9(self):
        return '9 6 1 1'

    def test_diversity_10(self):
        return '14 2 1 1'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '9 6 4 3'

    def test_diversity_2(self):
        return '11 2 2 3'

    def test_diversity_3(self):
        return '4 2 3 1'

    def test_diversity_4(self):
        return '10 2 3 2'

    def test_diversity_5(self):
        return '15 3 3 1'

    def test_diversity_6(self):
        return '10 4 4 1'

    def test_diversity_7(self):
        return '17 3 2 1'

    def test_diversity_8(self):
        return '8 4 4 3'

    def test_diversity_9(self):
        return '5 2 3 3'

    def test_diversity_10(self):
        return '13 6 4 3'
