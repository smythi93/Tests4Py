from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'multi 4 0'

    def test_diversity_2(self):
        return 'multi 5 1'

    def test_diversity_3(self):
        return 'multi 3 2'

    def test_diversity_4(self):
        return 'multi 6 3'

    def test_diversity_5(self):
        return 'multi 4 4'

    def test_diversity_6(self):
        return 'multi 7 5'

    def test_diversity_7(self):
        return 'multi 5 6'

    def test_diversity_8(self):
        return 'multi 3 7'

    def test_diversity_9(self):
        return 'multi 8 8'

    def test_diversity_10(self):
        return 'multi 6 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'single 4 10'

    def test_diversity_2(self):
        return 'single 5 11'

    def test_diversity_3(self):
        return 'single 3 12'

    def test_diversity_4(self):
        return 'single 6 13'

    def test_diversity_5(self):
        return 'single 4 14'

    def test_diversity_6(self):
        return 'single 7 15'

    def test_diversity_7(self):
        return 'single 5 16'

    def test_diversity_8(self):
        return 'single 3 17'

    def test_diversity_9(self):
        return 'single 8 18'

    def test_diversity_10(self):
        return 'single 6 19'
