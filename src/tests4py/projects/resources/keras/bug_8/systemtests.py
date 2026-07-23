from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'shared 12 2 0'

    def test_diversity_2(self):
        return 'shared 8 3 1'

    def test_diversity_3(self):
        return 'shared 10 2 2'

    def test_diversity_4(self):
        return 'shared 6 4 3'

    def test_diversity_5(self):
        return 'shared 14 2 4'

    def test_diversity_6(self):
        return 'shared 9 5 5'

    def test_diversity_7(self):
        return 'shared 7 3 6'

    def test_diversity_8(self):
        return 'shared 16 2 7'

    def test_diversity_9(self):
        return 'shared 11 4 8'

    def test_diversity_10(self):
        return 'shared 13 3 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'simple 12 2 10'

    def test_diversity_2(self):
        return 'simple 8 3 11'

    def test_diversity_3(self):
        return 'simple 10 2 12'

    def test_diversity_4(self):
        return 'simple 6 4 13'

    def test_diversity_5(self):
        return 'simple 14 2 14'

    def test_diversity_6(self):
        return 'simple 9 5 15'

    def test_diversity_7(self):
        return 'simple 7 3 16'

    def test_diversity_8(self):
        return 'simple 16 2 17'

    def test_diversity_9(self):
        return 'simple 11 4 18'

    def test_diversity_10(self):
        return 'simple 13 3 19'
