from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'x true -1.87 12.47'

    def test_diversity_2(self):
        return 'y true 2.39 14.03'

    def test_diversity_3(self):
        return 'y true 6.53 12.42'

    def test_diversity_4(self):
        return 'x true -9.61 9.7'

    def test_diversity_5(self):
        return 'y true -11.78 -5.59'

    def test_diversity_6(self):
        return 'x true -10.27 -0.7'

    def test_diversity_7(self):
        return 'y true 6.28 11.04'

    def test_diversity_8(self):
        return 'x true 9.65 27.84'

    def test_diversity_9(self):
        return 'x true -9.81 -8.28'

    def test_diversity_10(self):
        return 'y true -0.03 12.32'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'x false -4.1 13.35'

    def test_diversity_2(self):
        return 'x false -15.93 -10.16'

    def test_diversity_3(self):
        return 'x false 9.74 15.69'

    def test_diversity_4(self):
        return 'x false 5.88 25.54'

    def test_diversity_5(self):
        return 'x false 6.49 24.6'

    def test_diversity_6(self):
        return 'x false -9.19 9.59'

    def test_diversity_7(self):
        return 'x false -19.14 -8.07'

    def test_diversity_8(self):
        return 'y false -1.19 3.94'

    def test_diversity_9(self):
        return 'y false -14.4 2.15'

    def test_diversity_10(self):
        return 'y false 7.58 12.99'
