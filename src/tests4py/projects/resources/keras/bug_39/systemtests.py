from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'none 13 12 1'

    def test_diversity_2(self):
        return 'none 14 4 5'

    def test_diversity_3(self):
        return 'none 10'

    def test_diversity_4(self):
        return 'none 11 1 17 6'

    def test_diversity_5(self):
        return 'none 20'

    def test_diversity_6(self):
        return 'none 20 3 13'

    def test_diversity_7(self):
        return 'none 19 5 13'

    def test_diversity_8(self):
        return 'none 1 8'

    def test_diversity_9(self):
        return 'none 7 16 4 4'

    def test_diversity_10(self):
        return 'none 7 17 10'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '7 0 11 14'

    def test_diversity_2(self):
        return '6 12 18 11 12'

    def test_diversity_3(self):
        return '4 4 10 9 13'

    def test_diversity_4(self):
        return '6 6 7 16'

    def test_diversity_5(self):
        return '4 9 7 4 8'

    def test_diversity_6(self):
        return '13 17 14'

    def test_diversity_7(self):
        return '13 0 15 5'

    def test_diversity_8(self):
        return '18 13 17'

    def test_diversity_9(self):
        return '3 17'

    def test_diversity_10(self):
        return '19 16 1 16 5'
