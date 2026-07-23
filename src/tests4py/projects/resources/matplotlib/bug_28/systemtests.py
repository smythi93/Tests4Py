from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'x -5.42 39.96'

    def test_diversity_2(self):
        return 'x -3.77 25.99'

    def test_diversity_3(self):
        return 'x -1.12 47.19'

    def test_diversity_4(self):
        return 'x -4.59 85.13'

    def test_diversity_5(self):
        return 'x -9.76 12.14'

    def test_diversity_6(self):
        return 'x -2.33 65.19'

    def test_diversity_7(self):
        return 'x -0.78 87.44'

    def test_diversity_8(self):
        return 'x -0.8 57.73'

    def test_diversity_9(self):
        return 'x -9.24 11.5'

    def test_diversity_10(self):
        return 'x -6.89 89.38'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'x 0.38 9.88'

    def test_diversity_2(self):
        return 'x 3.09 15.21'

    def test_diversity_3(self):
        return 'x 2.68 39.39'

    def test_diversity_4(self):
        return 'x 4.17 11.27'

    def test_diversity_5(self):
        return 'x 1.98 28.72'

    def test_diversity_6(self):
        return 'x 0.67 10.4'

    def test_diversity_7(self):
        return 'x 2.34 16.5'

    def test_diversity_8(self):
        return 'x 3.75 41.31'

    def test_diversity_9(self):
        return 'x 4.9 13.07'

    def test_diversity_10(self):
        return 'x 1.43 25.93'
