from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'int 7394267'

    def test_diversity_2(self):
        return 'int 1'

    def test_diversity_3(self):
        return 'int 10'

    def test_diversity_4(self):
        return 'int 2'

    def test_diversity_5(self):
        return 'int 6'

    def test_diversity_6(self):
        return 'int 3'

    def test_diversity_7(self):
        return 'int 664'

    def test_diversity_8(self):
        return 'int 63472'

    def test_diversity_9(self):
        return 'int 60759'

    def test_diversity_10(self):
        return 'int 12'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'str 94,508'

    def test_diversity_2(self):
        return 'str 9.242'

    def test_diversity_3(self):
        return 'str 9.462'

    def test_diversity_4(self):
        return 'str 2,457'

    def test_diversity_5(self):
        return 'str 865,426'

    def test_diversity_6(self):
        return 'str 505.403'

    def test_diversity_7(self):
        return 'str 262,254'

    def test_diversity_8(self):
        return 'str 8,895,629'

    def test_diversity_9(self):
        return 'str 9,475,206'

    def test_diversity_10(self):
        return 'str 151.752'
