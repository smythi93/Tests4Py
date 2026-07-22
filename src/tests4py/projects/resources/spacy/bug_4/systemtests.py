from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '_ 2 0 2'

    def test_diversity_2(self):
        return '0 1 _'

    def test_diversity_3(self):
        return '5 0 2 _ 5'

    def test_diversity_4(self):
        return '_ 1 3'

    def test_diversity_5(self):
        return '2 4 _ 1 2 6'

    def test_diversity_6(self):
        return '4 0 4 _'

    def test_diversity_7(self):
        return '4 1 5 4 0 _'

    def test_diversity_8(self):
        return '0 0 3 _ 4 5'

    def test_diversity_9(self):
        return '_ 2 5 4 4 6'

    def test_diversity_10(self):
        return '0 1 0 _ 0'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '5 4 0 1 4 5'

    def test_diversity_2(self):
        return '1 2 3 5 1 6'

    def test_diversity_3(self):
        return '1 4 6 4 5 6'

    def test_diversity_4(self):
        return '1 1 3'

    def test_diversity_5(self):
        return '0 2'

    def test_diversity_6(self):
        return '2 2'

    def test_diversity_7(self):
        return '3 4 0 2'

    def test_diversity_8(self):
        return '0 0 2'

    def test_diversity_9(self):
        return '3 2 5 1 2 0'

    def test_diversity_10(self):
        return '0 1'
