from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'polar 4.97 6.86'

    def test_diversity_2(self):
        return 'polar 3.5 4.1'

    def test_diversity_3(self):
        return 'autoscale 4.58 6.68'

    def test_diversity_4(self):
        return 'relim 7.51 6.61'

    def test_diversity_5(self):
        return 'autoscale 4.08 6.76'

    def test_diversity_6(self):
        return 'relim 7.54 6.53'

    def test_diversity_7(self):
        return 'autoscale 6.88 6.36'

    def test_diversity_8(self):
        return 'relim 5.93 3.26'

    def test_diversity_9(self):
        return 'relim 7.81 5.97'

    def test_diversity_10(self):
        return 'autoscale 4.82 7.68'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'draw 3.26 6.11'

    def test_diversity_2(self):
        return 'draw 5.43 4.29'

    def test_diversity_3(self):
        return 'none 7.2 3.75'

    def test_diversity_4(self):
        return 'none 7.55 3.61'

    def test_diversity_5(self):
        return 'none 5.92 6.36'

    def test_diversity_6(self):
        return 'none 3.34 5.6'

    def test_diversity_7(self):
        return 'draw 5.01 3.13'

    def test_diversity_8(self):
        return 'none 6.47 3.84'

    def test_diversity_9(self):
        return 'draw 3.18 4.05'

    def test_diversity_10(self):
        return 'none 4.45 7.51'
