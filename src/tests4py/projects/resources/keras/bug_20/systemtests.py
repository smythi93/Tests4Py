from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'dil 11 3 2 full 1 3'

    def test_diversity_2(self):
        return 'dil 7 2 5 same 1 2'

    def test_diversity_3(self):
        return 'dil 5 2 2 full none 3'

    def test_diversity_4(self):
        return 'dil 3 3 2 valid 2 4'

    def test_diversity_5(self):
        return 'dil 9 1 4 same 0 2'

    def test_diversity_6(self):
        return 'dil 3 3 1 full none 2'

    def test_diversity_7(self):
        return 'dil 2 3 5 valid none 3'

    def test_diversity_8(self):
        return 'dil 10 3 4 same 2 4'

    def test_diversity_9(self):
        return 'dil 11 3 2 full none 3'

    def test_diversity_10(self):
        return 'dil 6 1 4 valid 0 2'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nodil 9 2 1 same 0 1'

    def test_diversity_2(self):
        return 'nodil 10 3 5 full none 1'

    def test_diversity_3(self):
        return 'nodil 3 1 1 valid none 1'

    def test_diversity_4(self):
        return 'nodil 10 2 1 valid 0 1'

    def test_diversity_5(self):
        return 'nodil 9 2 4 same none 1'

    def test_diversity_6(self):
        return 'nodil 7 1 5 valid 0 1'

    def test_diversity_7(self):
        return 'nodil 8 3 3 full 0 1'

    def test_diversity_8(self):
        return 'nodil 7 1 4 full 0 1'

    def test_diversity_9(self):
        return 'nodil 5 3 1 valid 0 1'

    def test_diversity_10(self):
        return 'nodil 6 3 3 full none 1'
