from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'response 10'

    def test_diversity_2(self):
        return 'response 6'

    def test_diversity_3(self):
        return 'response 16'

    def test_diversity_4(self):
        return 'response 5'

    def test_diversity_5(self):
        return 'response 11'

    def test_diversity_6(self):
        return 'response 13'

    def test_diversity_7(self):
        return 'response 4'

    def test_diversity_8(self):
        return 'response 3'

    def test_diversity_9(self):
        return 'response 20'

    def test_diversity_10(self):
        return 'response 2'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'request 15'

    def test_diversity_2(self):
        return 'request 10'

    def test_diversity_3(self):
        return 'request 19'

    def test_diversity_4(self):
        return 'response 1'

    def test_diversity_5(self):
        return 'request 7'

    def test_diversity_6(self):
        return 'request 17'

    def test_diversity_7(self):
        return 'request 3'

    def test_diversity_8(self):
        return 'response 0'

    def test_diversity_9(self):
        return 'request 13'

    def test_diversity_10(self):
        return 'request 2'
