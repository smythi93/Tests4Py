from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'tight 9 7 100'

    def test_diversity_2(self):
        return 'tight 16 7 100'

    def test_diversity_3(self):
        return 'tight 10 7 100'

    def test_diversity_4(self):
        return 'tight 29 7 100'

    def test_diversity_5(self):
        return 'tight 23 7 100'

    def test_diversity_6(self):
        return 'tight 15 7 100'

    def test_diversity_7(self):
        return 'tight 24 7 100'

    def test_diversity_8(self):
        return 'tight 21 7 100'

    def test_diversity_9(self):
        return 'tight 30 7 100'

    def test_diversity_10(self):
        return 'tight 8 7 100'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'normal 29 20 100'

    def test_diversity_2(self):
        return 'normal 22 9 80'

    def test_diversity_3(self):
        return 'normal 24 8 150'

    def test_diversity_4(self):
        return 'normal 27 9 80'

    def test_diversity_5(self):
        return 'normal 14 18 80'

    def test_diversity_6(self):
        return 'normal 23 17 80'

    def test_diversity_7(self):
        return 'normal 15 16 100'

    def test_diversity_8(self):
        return 'normal 18 6 100'

    def test_diversity_9(self):
        return 'normal 9 11 80'

    def test_diversity_10(self):
        return 'normal 19 15 100'
