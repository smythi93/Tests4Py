from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '717 None 93.15 890.9'

    def test_diversity_2(self):
        return '766 None 68.2 97.0'

    def test_diversity_3(self):
        return '3245 None 96.46 23.3'

    def test_diversity_4(self):
        return '3933 None 9.16 9.57'

    def test_diversity_5(self):
        return '4798 None 99.25 663.0'

    def test_diversity_6(self):
        return '1158 None 91.71 731.2'

    def test_diversity_7(self):
        return '3346 None 74.49 557.1'

    def test_diversity_8(self):
        return '2783 None 93.43 890.9'

    def test_diversity_9(self):
        return '1706 None 7.56 273.7'

    def test_diversity_10(self):
        return '3610 None 76.23 603.03'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '3169 4072 50.78 216.11'

    def test_diversity_2(self):
        return '2425 2667 73.08 321.76'

    def test_diversity_3(self):
        return '2063 3676 41.91 808.4'

    def test_diversity_4(self):
        return '1964 5543 25.91 507.0'

    def test_diversity_5(self):
        return '4283 4633 14.37 76.0'

    def test_diversity_6(self):
        return '3954 7521 11.46 514.87'

    def test_diversity_7(self):
        return '346 2572 55.19 569.6'

    def test_diversity_8(self):
        return '1643 5478 1.84 686.43'

    def test_diversity_9(self):
        return '702 5220 9.17 264.0'

    def test_diversity_10(self):
        return '2075 3066 40.9 981.0'

