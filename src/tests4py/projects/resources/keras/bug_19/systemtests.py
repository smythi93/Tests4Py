from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '3 6'

    def test_diversity_2(self):
        return '2 5'

    def test_diversity_3(self):
        return '6 3'

    def test_diversity_4(self):
        return '4 8'

    def test_diversity_5(self):
        return '5 2'

    def test_diversity_6(self):
        return '8 4'

    def test_diversity_7(self):
        return '3 7'

    def test_diversity_8(self):
        return '7 3'

    def test_diversity_9(self):
        return '2 8'

    def test_diversity_10(self):
        return '6 5'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '2 2'

    def test_diversity_2(self):
        return '3 3'

    def test_diversity_3(self):
        return '4 4'

    def test_diversity_4(self):
        return '5 5'

    def test_diversity_5(self):
        return '6 6'

    def test_diversity_6(self):
        return '7 7'

    def test_diversity_7(self):
        return '8 8'

    def test_diversity_8(self):
        return '9 9'

    def test_diversity_9(self):
        return '10 10'

    def test_diversity_10(self):
        return '11 11'
