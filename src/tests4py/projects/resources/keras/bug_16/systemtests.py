from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'cfgtype 1 4 3'

    def test_diversity_2(self):
        return 'cfgtype 2 5 4'

    def test_diversity_3(self):
        return 'cfgtype 3 4 2'

    def test_diversity_4(self):
        return 'cfgtype 1 6 5'

    def test_diversity_5(self):
        return 'cfgtype 2 3 3'

    def test_diversity_6(self):
        return 'cfgtype 3 7 4'

    def test_diversity_7(self):
        return 'cfgtype 1 4 6'

    def test_diversity_8(self):
        return 'cfgtype 2 5 2'

    def test_diversity_9(self):
        return 'cfgtype 3 6 3'

    def test_diversity_10(self):
        return 'cfgtype 1 8 4'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nlayers 1 4 3'

    def test_diversity_2(self):
        return 'nlayers 2 5 4'

    def test_diversity_3(self):
        return 'nlayers 3 4 2'

    def test_diversity_4(self):
        return 'nlayers 1 6 5'

    def test_diversity_5(self):
        return 'nlayers 2 3 3'

    def test_diversity_6(self):
        return 'nlayers 3 7 4'

    def test_diversity_7(self):
        return 'nlayers 1 4 6'

    def test_diversity_8(self):
        return 'nlayers 2 5 2'

    def test_diversity_9(self):
        return 'nlayers 3 6 3'

    def test_diversity_10(self):
        return 'nlayers 1 8 4'
