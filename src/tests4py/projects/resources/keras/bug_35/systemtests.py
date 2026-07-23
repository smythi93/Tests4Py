from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'pf 1482 2 4 3'

    def test_diversity_2(self):
        return 'pf 497 1 2 4'

    def test_diversity_3(self):
        return 'pf 3484 3 3 2'

    def test_diversity_4(self):
        return 'pf 7510 2 2 3'

    def test_diversity_5(self):
        return 'pf 5078 1 2 3'

    def test_diversity_6(self):
        return 'pf 708 2 4 2'

    def test_diversity_7(self):
        return 'pf 6448 1 4 2'

    def test_diversity_8(self):
        return 'pf 7593 1 5 2'

    def test_diversity_9(self):
        return 'pf 5965 1 2 3'

    def test_diversity_10(self):
        return 'pf 303 3 3 3'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nopf 4186 3 2 4'

    def test_diversity_2(self):
        return 'nopf 5428 3 3 4'

    def test_diversity_3(self):
        return 'nopf 9271 3 4 3'

    def test_diversity_4(self):
        return 'nopf 3820 2 2 3'

    def test_diversity_5(self):
        return 'nopf 195 1 2 2'

    def test_diversity_6(self):
        return 'nopf 4564 3 4 2'

    def test_diversity_7(self):
        return 'nopf 2388 3 5 4'

    def test_diversity_8(self):
        return 'nopf 7258 3 4 3'

    def test_diversity_9(self):
        return 'nopf 7489 3 5 4'

    def test_diversity_10(self):
        return 'nopf 850 2 2 2'
