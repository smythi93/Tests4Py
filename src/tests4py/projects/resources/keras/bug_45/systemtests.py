from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '3 5 4 2 nobias'

    def test_diversity_2(self):
        return '4 6 3 2 nobias'

    def test_diversity_3(self):
        return '5 4 6 3 nobias'

    def test_diversity_4(self):
        return '2 7 5 2 nobias'

    def test_diversity_5(self):
        return '6 3 4 2 nobias'

    def test_diversity_6(self):
        return '4 5 7 3 nobias'

    def test_diversity_7(self):
        return '3 6 3 2 nobias'

    def test_diversity_8(self):
        return '5 5 5 2 nobias'

    def test_diversity_9(self):
        return '2 4 8 3 nobias'

    def test_diversity_10(self):
        return '6 7 2 2 nobias'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '3 5 4 2 bias'

    def test_diversity_2(self):
        return '4 6 3 2 bias'

    def test_diversity_3(self):
        return '5 4 6 3 bias'

    def test_diversity_4(self):
        return '2 7 5 2 bias'

    def test_diversity_5(self):
        return '6 3 4 2 bias'

    def test_diversity_6(self):
        return '4 5 7 3 bias'

    def test_diversity_7(self):
        return '3 6 3 2 bias'

    def test_diversity_8(self):
        return '5 5 5 2 bias'

    def test_diversity_9(self):
        return '2 4 8 3 bias'

    def test_diversity_10(self):
        return '6 7 2 2 bias'
