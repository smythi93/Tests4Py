from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '1 6 2 5 0'

    def test_diversity_2(self):
        return '1 7 3 6 1'

    def test_diversity_3(self):
        return '1 8 2 4 2'

    def test_diversity_4(self):
        return '1 5 2 5 3'

    def test_diversity_5(self):
        return '1 9 4 7 4'

    def test_diversity_6(self):
        return '1 6 3 6 5'

    def test_diversity_7(self):
        return '1 10 2 5 6'

    def test_diversity_8(self):
        return '1 7 2 4 7'

    def test_diversity_9(self):
        return '1 8 3 6 8'

    def test_diversity_10(self):
        return '1 6 2 7 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '2 6 2 5 10'

    def test_diversity_2(self):
        return '3 7 3 6 11'

    def test_diversity_3(self):
        return '2 8 2 4 12'

    def test_diversity_4(self):
        return '4 5 2 5 13'

    def test_diversity_5(self):
        return '2 9 4 7 14'

    def test_diversity_6(self):
        return '3 6 3 6 15'

    def test_diversity_7(self):
        return '2 10 2 5 16'

    def test_diversity_8(self):
        return '5 7 2 4 17'

    def test_diversity_9(self):
        return '2 8 3 6 18'

    def test_diversity_10(self):
        return '3 6 2 7 19'
