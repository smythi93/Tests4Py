from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '99990000000.0'

    def test_diversity_2(self):
        return '999.99'

    def test_diversity_3(self):
        return '999.96'

    def test_diversity_4(self):
        return '99960000000.0'

    def test_diversity_5(self):
        return '999970.0'

    def test_diversity_6(self):
        return '99.98'

    def test_diversity_7(self):
        return '999990000.0'

    def test_diversity_8(self):
        return '99990000.0'

    def test_diversity_9(self):
        return '99.97'

    def test_diversity_10(self):
        return '999960.0'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '1.99'

    def test_diversity_2(self):
        return '3700000000.0'

    def test_diversity_3(self):
        return '7950000.0'

    def test_diversity_4(self):
        return '3500.0'

    def test_diversity_5(self):
        return '6400000000.0'

    def test_diversity_6(self):
        return '3250.0'

    def test_diversity_7(self):
        return '7800000.0'

    def test_diversity_8(self):
        return '7400000000.0'

    def test_diversity_9(self):
        return '7700000000.0'

    def test_diversity_10(self):
        return '2.1'

