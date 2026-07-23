from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'getnone 1 1 1 1'

    def test_diversity_2(self):
        return 'getnone 2 0 3 0'

    def test_diversity_3(self):
        return 'getnone 0 1 2 0'

    def test_diversity_4(self):
        return 'getnone 3 2 1 0'

    def test_diversity_5(self):
        return 'getnone 2 1 2 1'

    def test_diversity_6(self):
        return 'getx 1 1 1 1'

    def test_diversity_7(self):
        return 'getx 0 2 0 3'

    def test_diversity_8(self):
        return 'getx 2 0 1 2'

    def test_diversity_9(self):
        return 'getx 1 2 2 1'

    def test_diversity_10(self):
        return 'getx 3 1 0 3'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'total 1 1 1 1'

    def test_diversity_2(self):
        return 'total 2 0 3 0'

    def test_diversity_3(self):
        return 'total 0 2 0 3'

    def test_diversity_4(self):
        return 'total 2 1 1 2'

    def test_diversity_5(self):
        return 'total 3 2 1 0'

    def test_diversity_6(self):
        return 'total 1 0 2 1'

    def test_diversity_7(self):
        return 'total 2 2 2 2'

    def test_diversity_8(self):
        return 'total 0 1 1 0'

    def test_diversity_9(self):
        return 'total 3 0 0 3'

    def test_diversity_10(self):
        return 'total 1 3 2 1'
