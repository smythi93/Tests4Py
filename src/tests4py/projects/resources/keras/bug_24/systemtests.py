from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'hist 4 2 5 0'

    def test_diversity_2(self):
        return 'hist 5 3 6 1'

    def test_diversity_3(self):
        return 'hist 3 2 4 2'

    def test_diversity_4(self):
        return 'hist 6 2 5 3'

    def test_diversity_5(self):
        return 'hist 4 3 7 4'

    def test_diversity_6(self):
        return 'hist 5 2 4 5'

    def test_diversity_7(self):
        return 'hist 3 3 6 6'

    def test_diversity_8(self):
        return 'hist 6 2 5 7'

    def test_diversity_9(self):
        return 'hist 4 2 8 8'

    def test_diversity_10(self):
        return 'hist 5 3 5 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nohist 4 2 5 10'

    def test_diversity_2(self):
        return 'nohist 5 3 6 11'

    def test_diversity_3(self):
        return 'nohist 3 2 4 12'

    def test_diversity_4(self):
        return 'nohist 6 2 5 13'

    def test_diversity_5(self):
        return 'nohist 4 3 7 14'

    def test_diversity_6(self):
        return 'nohist 5 2 4 15'

    def test_diversity_7(self):
        return 'nohist 3 3 6 16'

    def test_diversity_8(self):
        return 'nohist 6 2 5 17'

    def test_diversity_9(self):
        return 'nohist 4 2 8 18'

    def test_diversity_10(self):
        return 'nohist 5 3 5 19'
