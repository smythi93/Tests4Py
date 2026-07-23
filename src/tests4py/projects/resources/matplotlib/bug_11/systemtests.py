from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '5.669 EMPTY'

    def test_diversity_2(self):
        return '2.308 EMPTY'

    def test_diversity_3(self):
        return '3.775 EMPTY'

    def test_diversity_4(self):
        return '6.421 EMPTY'

    def test_diversity_5(self):
        return '9.839 EMPTY'

    def test_diversity_6(self):
        return '6.427 EMPTY'

    def test_diversity_7(self):
        return '7.053 EMPTY'

    def test_diversity_8(self):
        return '3.784 EMPTY'

    def test_diversity_9(self):
        return '6.653 EMPTY'

    def test_diversity_10(self):
        return '4.966 EMPTY'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '9.962 tdlgcn'

    def test_diversity_2(self):
        return '10.223 papfr'

    def test_diversity_3(self):
        return '2.064 qrfwx'

    def test_diversity_4(self):
        return '2.965 hipyep'

    def test_diversity_5(self):
        return '9.116 eng'

    def test_diversity_6(self):
        return '4.54 dqyv'

    def test_diversity_7(self):
        return '6.702 ffl'

    def test_diversity_8(self):
        return '3.334 lebg'

    def test_diversity_9(self):
        return '4.758 sgixb'

    def test_diversity_10(self):
        return '4.583 hgy'
