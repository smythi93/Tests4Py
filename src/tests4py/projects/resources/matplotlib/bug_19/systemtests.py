from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'autoscale 3.17 4.07'

    def test_diversity_2(self):
        return 'polar 5.23 7.93'

    def test_diversity_3(self):
        return 'relim 4.14 6.96'

    def test_diversity_4(self):
        return 'relim 6.99 4.93'

    def test_diversity_5(self):
        return 'polar 4.13 3.52'

    def test_diversity_6(self):
        return 'relim 4.75 3.24'

    def test_diversity_7(self):
        return 'relim 4.44 5.36'

    def test_diversity_8(self):
        return 'autoscale 3.22 3.6'

    def test_diversity_9(self):
        return 'polar 6.01 3.95'

    def test_diversity_10(self):
        return 'autoscale 6.38 5.05'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'none 5.19 7.43'

    def test_diversity_2(self):
        return 'draw 6.24 7.4'

    def test_diversity_3(self):
        return 'none 4.91 7.14'

    def test_diversity_4(self):
        return 'draw 6.56 4.48'

    def test_diversity_5(self):
        return 'none 4.04 6.22'

    def test_diversity_6(self):
        return 'none 5.2 5.86'

    def test_diversity_7(self):
        return 'draw 5.51 3.62'

    def test_diversity_8(self):
        return 'draw 6.88 3.75'

    def test_diversity_9(self):
        return 'draw 6.05 3.42'

    def test_diversity_10(self):
        return 'draw 3.17 4.95'
