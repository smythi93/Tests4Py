from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'mask0 924 4 5'

    def test_diversity_2(self):
        return 'mask0 5738 3 5'

    def test_diversity_3(self):
        return 'mask0 7776 5 3'

    def test_diversity_4(self):
        return 'mask0 2944 4 2'

    def test_diversity_5(self):
        return 'mask0 5452 5 4'

    def test_diversity_6(self):
        return 'mask0 1592 5 2'

    def test_diversity_7(self):
        return 'mask0 6801 2 5'

    def test_diversity_8(self):
        return 'mask0 3512 2 3'

    def test_diversity_9(self):
        return 'mask0 2355 5 5'

    def test_diversity_10(self):
        return 'mask0 5305 3 5'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nomask 9434 2 2'

    def test_diversity_2(self):
        return 'nomask 2917 5 2'

    def test_diversity_3(self):
        return 'nomask 5957 4 2'

    def test_diversity_4(self):
        return 'nomask 5886 2 2'

    def test_diversity_5(self):
        return 'nomask 5314 4 3'

    def test_diversity_6(self):
        return 'nomask 5321 4 3'

    def test_diversity_7(self):
        return 'nomask 8164 3 4'

    def test_diversity_8(self):
        return 'nomask 1559 5 5'

    def test_diversity_9(self):
        return 'nomask 8225 2 2'

    def test_diversity_10(self):
        return 'nomask 918 2 5'
