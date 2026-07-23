from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'withstate 5 3 3'

    def test_diversity_2(self):
        return 'withstate 4 4 2'

    def test_diversity_3(self):
        return 'withstate 6 3 5'

    def test_diversity_4(self):
        return 'withstate 3 5 3'

    def test_diversity_5(self):
        return 'withstate 7 2 4'

    def test_diversity_6(self):
        return 'withstate 5 4 6'

    def test_diversity_7(self):
        return 'withstate 4 3 3'

    def test_diversity_8(self):
        return 'withstate 6 5 2'

    def test_diversity_9(self):
        return 'withstate 3 4 5'

    def test_diversity_10(self):
        return 'withstate 8 3 4'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'plain 5 3 3'

    def test_diversity_2(self):
        return 'plain 4 4 2'

    def test_diversity_3(self):
        return 'plain 6 3 5'

    def test_diversity_4(self):
        return 'plain 3 5 3'

    def test_diversity_5(self):
        return 'plain 7 2 4'

    def test_diversity_6(self):
        return 'plain 5 4 6'

    def test_diversity_7(self):
        return 'plain 4 3 3'

    def test_diversity_8(self):
        return 'plain 6 5 2'

    def test_diversity_9(self):
        return 'plain 3 4 5'

    def test_diversity_10(self):
        return 'plain 8 3 4'
