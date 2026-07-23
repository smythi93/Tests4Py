from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'val 3 2 0'

    def test_diversity_2(self):
        return 'val 4 3 1'

    def test_diversity_3(self):
        return 'val 5 2 2'

    def test_diversity_4(self):
        return 'val 2 4 3'

    def test_diversity_5(self):
        return 'val 6 2 4'

    def test_diversity_6(self):
        return 'val 3 5 5'

    def test_diversity_7(self):
        return 'val 4 2 6'

    def test_diversity_8(self):
        return 'val 5 3 7'

    def test_diversity_9(self):
        return 'val 2 2 8'

    def test_diversity_10(self):
        return 'val 6 4 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'train 3 2 10'

    def test_diversity_2(self):
        return 'train 4 3 11'

    def test_diversity_3(self):
        return 'train 5 2 12'

    def test_diversity_4(self):
        return 'train 2 4 13'

    def test_diversity_5(self):
        return 'train 6 2 14'

    def test_diversity_6(self):
        return 'train 3 5 15'

    def test_diversity_7(self):
        return 'train 4 2 16'

    def test_diversity_8(self):
        return 'train 5 3 17'

    def test_diversity_9(self):
        return 'train 2 2 18'

    def test_diversity_10(self):
        return 'train 6 4 19'
