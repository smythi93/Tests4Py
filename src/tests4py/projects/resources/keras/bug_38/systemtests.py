from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'stack 8 16 5 6 5'

    def test_diversity_2(self):
        return 'stack 4 6 3 4 4'

    def test_diversity_3(self):
        return 'stack 5 10 6 2 5'

    def test_diversity_4(self):
        return 'stack 3 7 4 3 6'

    def test_diversity_5(self):
        return 'stack 6 12 8 2 3'

    def test_diversity_6(self):
        return 'stack 8 4 7 3 5'

    def test_diversity_7(self):
        return 'stack 5 5 3 2 7'

    def test_diversity_8(self):
        return 'stack 7 3 5 4 4'

    def test_diversity_9(self):
        return 'stack 2 8 8 3 5'

    def test_diversity_10(self):
        return 'stack 6 9 4 2 6'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'single 8 16 5 6 5'

    def test_diversity_2(self):
        return 'single 4 6 3 4 4'

    def test_diversity_3(self):
        return 'single 5 10 6 2 5'

    def test_diversity_4(self):
        return 'single 3 7 4 3 6'

    def test_diversity_5(self):
        return 'single 6 12 8 2 3'

    def test_diversity_6(self):
        return 'single 8 4 7 3 5'

    def test_diversity_7(self):
        return 'single 5 5 3 2 7'

    def test_diversity_8(self):
        return 'single 7 3 5 4 4'

    def test_diversity_9(self):
        return 'single 2 8 8 3 5'

    def test_diversity_10(self):
        return 'single 6 9 4 2 6'
