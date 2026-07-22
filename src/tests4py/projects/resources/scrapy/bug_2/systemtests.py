from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'none 17'

    def test_diversity_2(self):
        return 'none 4'

    def test_diversity_3(self):
        return 'none 27'

    def test_diversity_4(self):
        return 'none 5'

    def test_diversity_5(self):
        return 'none 12'

    def test_diversity_6(self):
        return 'none 24'

    def test_diversity_7(self):
        return 'none 8'

    def test_diversity_8(self):
        return 'none 3'

    def test_diversity_9(self):
        return 'none 38'

    def test_diversity_10(self):
        return 'none 32'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '11 27'

    def test_diversity_2(self):
        return '21 15'

    def test_diversity_3(self):
        return '14 28'

    def test_diversity_4(self):
        return '16 11'

    def test_diversity_5(self):
        return '16 1'

    def test_diversity_6(self):
        return '5 35'

    def test_diversity_7(self):
        return '6 29'

    def test_diversity_8(self):
        return '9 17'

    def test_diversity_9(self):
        return '20 14'

    def test_diversity_10(self):
        return '19 22'
