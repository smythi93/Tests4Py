from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'vlines -6.83,-1.93,2.11,-3.11,3.02,nan'

    def test_diversity_2(self):
        return 'vlines -1.69,nan,8.4,-0.46,7.83,9.14,nan'

    def test_diversity_3(self):
        return 'hlines 7.68,1.2,-7.48,2.76,0.86,-5.49,nan'

    def test_diversity_4(self):
        return 'vlines 0.22,nan,0.07,-2.69'

    def test_diversity_5(self):
        return 'vlines 5.71,0.07,7.39,nan,nan'

    def test_diversity_6(self):
        return 'vlines 5.8,nan,-6.95,5.89,4.07,-9.44'

    def test_diversity_7(self):
        return 'hlines nan,6.86,nan,8.08'

    def test_diversity_8(self):
        return 'hlines -7.99,nan,nan,-3.71'

    def test_diversity_9(self):
        return 'hlines -6.81,-3.98,1.87,4.81,9.5,nan,9.53'

    def test_diversity_10(self):
        return 'hlines -1.0,nan,nan,9.87'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'hlines 9.91,4.1,1.56'

    def test_diversity_2(self):
        return 'hlines -0.42,-1.07,-3.45,-2.89,3.46,-1.66,6.5'

    def test_diversity_3(self):
        return 'vlines -9.73,-6.26'

    def test_diversity_4(self):
        return 'vlines 7.04,1.18,-3.92,-3.36,3.62,5.93,7.6'

    def test_diversity_5(self):
        return 'hlines -4.95,-4.67,-0.15,-5.01,1.12,-2.69'

    def test_diversity_6(self):
        return 'vlines -6.37,-8.92,-4.83,7.67,-4.93'

    def test_diversity_7(self):
        return 'vlines -8.94,-9.3,-7.02,-6.0,-4.79'

    def test_diversity_8(self):
        return 'hlines 1.09,2.58,-4.91,-9.51,5.13,-0.04,-1.58'

    def test_diversity_9(self):
        return 'vlines 5.05,-2.44,1.75'

    def test_diversity_10(self):
        return 'hlines 6.19,-2.4,-2.85,8.3,-5.88,-3.91'
