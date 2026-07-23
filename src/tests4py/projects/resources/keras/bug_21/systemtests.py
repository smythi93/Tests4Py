from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'restore 283 1'

    def test_diversity_2(self):
        return 'restore 881 3'

    def test_diversity_3(self):
        return 'restore 519 1'

    def test_diversity_4(self):
        return 'restore 482 2'

    def test_diversity_5(self):
        return 'restore 559 1'

    def test_diversity_6(self):
        return 'restore 123 2'

    def test_diversity_7(self):
        return 'restore 830 1'

    def test_diversity_8(self):
        return 'restore 825 3'

    def test_diversity_9(self):
        return 'restore 140 2'

    def test_diversity_10(self):
        return 'restore 193 4'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'default 874 5'

    def test_diversity_2(self):
        return 'default 620 3'

    def test_diversity_3(self):
        return 'default 437 5'

    def test_diversity_4(self):
        return 'default 334 1'

    def test_diversity_5(self):
        return 'default 149 3'

    def test_diversity_6(self):
        return 'default 166 3'

    def test_diversity_7(self):
        return 'default 522 2'

    def test_diversity_8(self):
        return 'default 204 5'

    def test_diversity_9(self):
        return 'default 387 2'

    def test_diversity_10(self):
        return 'default 688 3'
