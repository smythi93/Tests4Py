from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'nostep 3 2 0'

    def test_diversity_2(self):
        return 'nostep 4 3 1'

    def test_diversity_3(self):
        return 'nostep 5 2 2'

    def test_diversity_4(self):
        return 'nostep 2 4 3'

    def test_diversity_5(self):
        return 'nostep 6 2 4'

    def test_diversity_6(self):
        return 'nostep 3 5 5'

    def test_diversity_7(self):
        return 'nostep 4 2 6'

    def test_diversity_8(self):
        return 'nostep 5 3 7'

    def test_diversity_9(self):
        return 'nostep 2 2 8'

    def test_diversity_10(self):
        return 'nostep 6 4 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'withstep 3 2 10'

    def test_diversity_2(self):
        return 'withstep 4 3 11'

    def test_diversity_3(self):
        return 'withstep 5 2 12'

    def test_diversity_4(self):
        return 'withstep 2 4 13'

    def test_diversity_5(self):
        return 'withstep 6 2 14'

    def test_diversity_6(self):
        return 'withstep 3 5 15'

    def test_diversity_7(self):
        return 'withstep 4 2 16'

    def test_diversity_8(self):
        return 'withstep 5 3 17'

    def test_diversity_9(self):
        return 'withstep 2 2 18'

    def test_diversity_10(self):
        return 'withstep 6 4 19'
