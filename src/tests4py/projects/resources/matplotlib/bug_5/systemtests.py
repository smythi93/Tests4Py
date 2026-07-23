from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '2 7.5'

    def test_diversity_2(self):
        return '2 5.8'

    def test_diversity_3(self):
        return '3 6.5'

    def test_diversity_4(self):
        return '1 4.5'

    def test_diversity_5(self):
        return '4 3.3'

    def test_diversity_6(self):
        return 'x 6.0'

    def test_diversity_7(self):
        return '1 4.6'

    def test_diversity_8(self):
        return '+ 7.7'

    def test_diversity_9(self):
        return '4 6.7'

    def test_diversity_10(self):
        return 'x 4.1'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'o 4.4'

    def test_diversity_2(self):
        return 'o 3.9'

    def test_diversity_3(self):
        return 'o 4.1'

    def test_diversity_4(self):
        return 'o 8.2'

    def test_diversity_5(self):
        return 's 8.1'

    def test_diversity_6(self):
        return 'v 8.2'

    def test_diversity_7(self):
        return '^ 8.6'

    def test_diversity_8(self):
        return 'p 8.3'

    def test_diversity_9(self):
        return 'p 6.7'

    def test_diversity_10(self):
        return '^ 4.9'
