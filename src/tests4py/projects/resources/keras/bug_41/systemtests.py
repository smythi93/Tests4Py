from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'fault 21590'

    def test_diversity_2(self):
        return 'fault 17826'

    def test_diversity_3(self):
        return 'fault 46368'

    def test_diversity_4(self):
        return 'fault 91507'

    def test_diversity_5(self):
        return 'fault 53642'

    def test_diversity_6(self):
        return 'fault 47174'

    def test_diversity_7(self):
        return 'fault 36256'

    def test_diversity_8(self):
        return 'fault 82052'

    def test_diversity_9(self):
        return 'fault 67721'

    def test_diversity_10(self):
        return 'fault 32767'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'good 46184'

    def test_diversity_2(self):
        return 'good 3782'

    def test_diversity_3(self):
        return 'good 2394'

    def test_diversity_4(self):
        return 'good 98366'

    def test_diversity_5(self):
        return 'good 75860'

    def test_diversity_6(self):
        return 'good 7766'

    def test_diversity_7(self):
        return 'good 25220'

    def test_diversity_8(self):
        return 'good 29324'

    def test_diversity_9(self):
        return 'good 39993'

    def test_diversity_10(self):
        return 'good 86039'
