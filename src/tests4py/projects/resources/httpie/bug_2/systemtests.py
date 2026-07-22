from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '0 4'

    def test_diversity_2(self):
        return '2 4'

    def test_diversity_3(self):
        return '1 5'

    def test_diversity_4(self):
        return '0 2'

    def test_diversity_5(self):
        return '2 5'

    def test_diversity_6(self):
        return '0 1'

    def test_diversity_7(self):
        return '3 4'

    def test_diversity_8(self):
        return '1 3'

    def test_diversity_9(self):
        return '0 3'

    def test_diversity_10(self):
        return '1 4'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '6 0'

    def test_diversity_2(self):
        return '3 2'

    def test_diversity_3(self):
        return '5 5'

    def test_diversity_4(self):
        return '5 1'

    def test_diversity_5(self):
        return '4 3'

    def test_diversity_6(self):
        return '6 3'

    def test_diversity_7(self):
        return '3 1'

    def test_diversity_8(self):
        return '4 1'

    def test_diversity_9(self):
        return '4 2'

    def test_diversity_10(self):
        return '3 0'
