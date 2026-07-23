from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'false 151.8 227.1'

    def test_diversity_2(self):
        return 'false 286.5 131.1'

    def test_diversity_3(self):
        return 'false 459.0 274.4'

    def test_diversity_4(self):
        return 'false 267.7 247.2'

    def test_diversity_5(self):
        return 'false 226.8 174.4'

    def test_diversity_6(self):
        return 'false 288.4 222.5'

    def test_diversity_7(self):
        return 'false 120.8 323.1'

    def test_diversity_8(self):
        return 'false 184.7 269.3'

    def test_diversity_9(self):
        return 'false 157.4 122.1'

    def test_diversity_10(self):
        return 'false 459.4 248.3'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'true 388.3 70.0'

    def test_diversity_2(self):
        return 'true 282.7 129.7'

    def test_diversity_3(self):
        return 'true 150.8 371.7'

    def test_diversity_4(self):
        return 'true 472.7 382.8'

    def test_diversity_5(self):
        return 'true 206.6 196.7'

    def test_diversity_6(self):
        return 'true 501.9 254.9'

    def test_diversity_7(self):
        return 'true 189.2 100.3'

    def test_diversity_8(self):
        return 'true 340.1 273.1'

    def test_diversity_9(self):
        return 'true 182.4 405.9'

    def test_diversity_10(self):
        return 'true 536.6 375.9'
