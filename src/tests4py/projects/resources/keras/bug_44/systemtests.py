from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'simple 5 4 frozen'

    def test_diversity_2(self):
        return 'gru 6 3 frozen'

    def test_diversity_3(self):
        return 'lstm 4 5 frozen'

    def test_diversity_4(self):
        return 'simple 7 2 frozen'

    def test_diversity_5(self):
        return 'gru 3 6 frozen'

    def test_diversity_6(self):
        return 'lstm 8 3 frozen'

    def test_diversity_7(self):
        return 'simple 4 7 frozen'

    def test_diversity_8(self):
        return 'gru 5 5 frozen'

    def test_diversity_9(self):
        return 'lstm 6 4 frozen'

    def test_diversity_10(self):
        return 'simple 3 8 frozen'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'simple 5 4 trainable'

    def test_diversity_2(self):
        return 'gru 6 3 trainable'

    def test_diversity_3(self):
        return 'lstm 4 5 trainable'

    def test_diversity_4(self):
        return 'simple 7 2 trainable'

    def test_diversity_5(self):
        return 'gru 3 6 trainable'

    def test_diversity_6(self):
        return 'lstm 8 3 trainable'

    def test_diversity_7(self):
        return 'simple 4 7 trainable'

    def test_diversity_8(self):
        return 'gru 5 5 trainable'

    def test_diversity_9(self):
        return 'lstm 6 4 trainable'

    def test_diversity_10(self):
        return 'simple 3 8 trainable'
