from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'duck 3 2 0'

    def test_diversity_2(self):
        return 'duck 4 3 1'

    def test_diversity_3(self):
        return 'duck 5 2 2'

    def test_diversity_4(self):
        return 'duck 2 4 3'

    def test_diversity_5(self):
        return 'duck 6 2 4'

    def test_diversity_6(self):
        return 'duck 3 5 5'

    def test_diversity_7(self):
        return 'duck 4 2 6'

    def test_diversity_8(self):
        return 'duck 5 3 7'

    def test_diversity_9(self):
        return 'duck 2 2 8'

    def test_diversity_10(self):
        return 'duck 6 4 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'real 3 2 10'

    def test_diversity_2(self):
        return 'real 4 3 11'

    def test_diversity_3(self):
        return 'real 5 2 12'

    def test_diversity_4(self):
        return 'real 2 4 13'

    def test_diversity_5(self):
        return 'real 6 2 14'

    def test_diversity_6(self):
        return 'real 3 5 15'

    def test_diversity_7(self):
        return 'real 4 2 16'

    def test_diversity_8(self):
        return 'real 5 3 17'

    def test_diversity_9(self):
        return 'real 2 2 18'

    def test_diversity_10(self):
        return 'real 6 4 19'
