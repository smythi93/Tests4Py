from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'both 9895 4 2'

    def test_diversity_2(self):
        return 'both 6729 6 5'

    def test_diversity_3(self):
        return 'both 2692 4 5'

    def test_diversity_4(self):
        return 'both 3347 3 4'

    def test_diversity_5(self):
        return 'both 4406 7 3'

    def test_diversity_6(self):
        return 'both 6421 6 4'

    def test_diversity_7(self):
        return 'both 8496 3 2'

    def test_diversity_8(self):
        return 'both 8643 7 4'

    def test_diversity_9(self):
        return 'both 2429 4 3'

    def test_diversity_10(self):
        return 'both 416 4 5'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'onlysw 1754 8 2'

    def test_diversity_2(self):
        return 'onlysw 459 3 2'

    def test_diversity_3(self):
        return 'onlysw 9901 7 2'

    def test_diversity_4(self):
        return 'onlysw 4616 4 3'

    def test_diversity_5(self):
        return 'onlysw 1031 4 4'

    def test_diversity_6(self):
        return 'onlysw 9321 5 3'

    def test_diversity_7(self):
        return 'onlysw 8669 4 4'

    def test_diversity_8(self):
        return 'onlysw 2295 5 2'

    def test_diversity_9(self):
        return 'onlysw 7874 6 5'

    def test_diversity_10(self):
        return 'onlysw 652 5 3'
