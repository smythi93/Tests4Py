from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'mask 4 5 3 6 0'

    def test_diversity_2(self):
        return 'mask 3 4 2 5 1'

    def test_diversity_3(self):
        return 'mask 5 6 4 7 2'

    def test_diversity_4(self):
        return 'mask 2 3 3 4 3'

    def test_diversity_5(self):
        return 'mask 6 5 2 8 4'

    def test_diversity_6(self):
        return 'mask 4 7 3 5 5'

    def test_diversity_7(self):
        return 'mask 3 5 5 6 6'

    def test_diversity_8(self):
        return 'mask 5 4 2 7 7'

    def test_diversity_9(self):
        return 'mask 2 6 4 5 8'

    def test_diversity_10(self):
        return 'mask 6 3 3 6 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nomask 4 5 3 6 10'

    def test_diversity_2(self):
        return 'nomask 3 4 2 5 11'

    def test_diversity_3(self):
        return 'nomask 5 6 4 7 12'

    def test_diversity_4(self):
        return 'nomask 2 3 3 4 13'

    def test_diversity_5(self):
        return 'nomask 6 5 2 8 14'

    def test_diversity_6(self):
        return 'nomask 4 7 3 5 15'

    def test_diversity_7(self):
        return 'nomask 3 5 5 6 16'

    def test_diversity_8(self):
        return 'nomask 5 4 2 7 17'

    def test_diversity_9(self):
        return 'nomask 2 6 4 5 18'

    def test_diversity_10(self):
        return 'nomask 6 3 3 6 19'
