from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'none 10'

    def test_diversity_2(self):
        return 'none 11'

    def test_diversity_3(self):
        return 'none 8'

    def test_diversity_4(self):
        return 'none 16'

    def test_diversity_5(self):
        return 'none 5'

    def test_diversity_6(self):
        return 'none 4'

    def test_diversity_7(self):
        return 'none 6'

    def test_diversity_8(self):
        return 'none 9'

    def test_diversity_9(self):
        return 'none 12'

    def test_diversity_10(self):
        return 'none 3'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'full 13'

    def test_diversity_2(self):
        return 'full 8'

    def test_diversity_3(self):
        return 'full 10'

    def test_diversity_4(self):
        return 'full 2'

    def test_diversity_5(self):
        return 'full 5'

    def test_diversity_6(self):
        return 'full 14'

    def test_diversity_7(self):
        return 'full 11'

    def test_diversity_8(self):
        return 'full 12'

    def test_diversity_9(self):
        return 'full 4'

    def test_diversity_10(self):
        return 'full 6'
