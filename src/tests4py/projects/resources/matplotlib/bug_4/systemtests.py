from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'vlines cyan -0.79 -0.12 3.95'

    def test_diversity_2(self):
        return 'vlines pink -1.58 -4.7 0.15'

    def test_diversity_3(self):
        return 'vlines teal -1.3 -2.47 2.13'

    def test_diversity_4(self):
        return 'hlines orange -4.73 -4.23 0.95'

    def test_diversity_5(self):
        return 'vlines magenta -1.97 -4.41 -2.81'

    def test_diversity_6(self):
        return 'hlines magenta 0.52 -3.76 -2.68'

    def test_diversity_7(self):
        return 'hlines orange 4.48 -4.71 0.28'

    def test_diversity_8(self):
        return 'vlines purple -0.09 -1.41 1.79'

    def test_diversity_9(self):
        return 'vlines purple -3.68 -2.64 2.04'

    def test_diversity_10(self):
        return 'vlines pink -3.46 -0.41 3.25'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'hlines k -1.75 -3.44 0.83'

    def test_diversity_2(self):
        return 'hlines #000000 1.56 -0.41 3.02'

    def test_diversity_3(self):
        return 'hlines #000000 -4.01 -2.81 0.24'

    def test_diversity_4(self):
        return 'hlines #000000 2.42 -4.28 -1.49'

    def test_diversity_5(self):
        return 'vlines #000000 -4.46 -3.91 -2.36'

    def test_diversity_6(self):
        return 'hlines k -4.17 -0.73 4.46'

    def test_diversity_7(self):
        return 'vlines k 2.51 -1.41 3.42'

    def test_diversity_8(self):
        return 'hlines #000000 4.48 -0.5 1.0'

    def test_diversity_9(self):
        return 'hlines #000000 -2.91 -0.76 0.38'

    def test_diversity_10(self):
        return 'vlines k 0.18 -2.54 2.4'
