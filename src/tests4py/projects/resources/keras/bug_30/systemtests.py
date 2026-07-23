from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'datatensor 3 4 10 0'

    def test_diversity_2(self):
        return 'datatensor 4 5 8 1'

    def test_diversity_3(self):
        return 'datatensor 5 3 12 2'

    def test_diversity_4(self):
        return 'datatensor 2 6 9 3'

    def test_diversity_5(self):
        return 'datatensor 6 4 7 4'

    def test_diversity_6(self):
        return 'datatensor 3 5 11 5'

    def test_diversity_7(self):
        return 'datatensor 4 3 6 6'

    def test_diversity_8(self):
        return 'datatensor 5 6 10 7'

    def test_diversity_9(self):
        return 'datatensor 2 4 8 8'

    def test_diversity_10(self):
        return 'datatensor 6 5 9 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'normal 3 4 10 10'

    def test_diversity_2(self):
        return 'normal 4 5 8 11'

    def test_diversity_3(self):
        return 'normal 5 3 12 12'

    def test_diversity_4(self):
        return 'normal 2 6 9 13'

    def test_diversity_5(self):
        return 'normal 6 4 7 14'

    def test_diversity_6(self):
        return 'normal 3 5 11 15'

    def test_diversity_7(self):
        return 'normal 4 3 6 16'

    def test_diversity_8(self):
        return 'normal 5 6 10 17'

    def test_diversity_9(self):
        return 'normal 2 4 8 18'

    def test_diversity_10(self):
        return 'normal 6 5 9 19'
