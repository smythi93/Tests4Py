from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'masked 5 4 3'

    def test_diversity_2(self):
        return 'masked 6 3 4'

    def test_diversity_3(self):
        return 'masked 4 5 2'

    def test_diversity_4(self):
        return 'masked 3 4 5'

    def test_diversity_5(self):
        return 'masked 7 2 3'

    def test_diversity_6(self):
        return 'masked 5 6 4'

    def test_diversity_7(self):
        return 'masked 8 3 2'

    def test_diversity_8(self):
        return 'masked 4 4 6'

    def test_diversity_9(self):
        return 'masked 6 5 3'

    def test_diversity_10(self):
        return 'masked 3 3 4'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nomask 5 4 3'

    def test_diversity_2(self):
        return 'nomask 6 3 4'

    def test_diversity_3(self):
        return 'nomask 4 5 2'

    def test_diversity_4(self):
        return 'nomask 3 4 5'

    def test_diversity_5(self):
        return 'nomask 7 2 3'

    def test_diversity_6(self):
        return 'nomask 5 6 4'

    def test_diversity_7(self):
        return 'nomask 8 3 2'

    def test_diversity_8(self):
        return 'nomask 4 4 6'

    def test_diversity_9(self):
        return 'nomask 6 5 3'

    def test_diversity_10(self):
        return 'nomask 3 3 4'
