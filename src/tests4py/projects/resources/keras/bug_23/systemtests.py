from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'deferred 3 5 4 0'

    def test_diversity_2(self):
        return 'deferred 4 6 3 1'

    def test_diversity_3(self):
        return 'deferred 5 4 2 2'

    def test_diversity_4(self):
        return 'deferred 2 7 5 3'

    def test_diversity_5(self):
        return 'deferred 6 3 4 4'

    def test_diversity_6(self):
        return 'deferred 3 5 6 5'

    def test_diversity_7(self):
        return 'deferred 4 4 3 6'

    def test_diversity_8(self):
        return 'deferred 5 6 2 7'

    def test_diversity_9(self):
        return 'deferred 2 3 5 8'

    def test_diversity_10(self):
        return 'deferred 6 5 4 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'explicit 3 5 4 10'

    def test_diversity_2(self):
        return 'explicit 4 6 3 11'

    def test_diversity_3(self):
        return 'explicit 5 4 2 12'

    def test_diversity_4(self):
        return 'explicit 2 7 5 13'

    def test_diversity_5(self):
        return 'explicit 6 3 4 14'

    def test_diversity_6(self):
        return 'explicit 3 5 6 15'

    def test_diversity_7(self):
        return 'explicit 4 4 3 16'

    def test_diversity_8(self):
        return 'explicit 5 6 2 17'

    def test_diversity_9(self):
        return 'explicit 2 3 5 18'

    def test_diversity_10(self):
        return 'explicit 6 5 4 19'
