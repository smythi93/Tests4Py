from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'flat 2277 7'

    def test_diversity_2(self):
        return 'flat 3370 2'

    def test_diversity_3(self):
        return 'flat 7689 2'

    def test_diversity_4(self):
        return 'flat 3805 5'

    def test_diversity_5(self):
        return 'flat 5949 4'

    def test_diversity_6(self):
        return 'flat 7831 2'

    def test_diversity_7(self):
        return 'flat 6049 2'

    def test_diversity_8(self):
        return 'flat 1965 7'

    def test_diversity_9(self):
        return 'flat 9158 4'

    def test_diversity_10(self):
        return 'flat 571 2'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'col 6133 6'

    def test_diversity_2(self):
        return 'col 4975 8'

    def test_diversity_3(self):
        return 'col 6024 4'

    def test_diversity_4(self):
        return 'col 7853 2'

    def test_diversity_5(self):
        return 'col 7849 3'

    def test_diversity_6(self):
        return 'col 2153 6'

    def test_diversity_7(self):
        return 'col 6299 8'

    def test_diversity_8(self):
        return 'col 3233 3'

    def test_diversity_9(self):
        return 'col 1359 2'

    def test_diversity_10(self):
        return 'col 8940 3'
