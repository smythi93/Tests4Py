from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '1 1.0 0.0,0.055,0.22 0.181,0.761,0.189 0.319,0.077,0.298 1.0,0.942,0.484'

    def test_diversity_2(self):
        return '1 1.0 0.0,0.246,0.113 0.339,0.768,0.869 0.847,0.733,0.448 1.0,0.908,0.975'

    def test_diversity_3(self):
        return '1 1.0 0.0,0.699,0.826 1.0,0.226,0.727'

    def test_diversity_4(self):
        return '1 1.0 0.0,0.992,0.338 0.483,0.003,0.456 0.845,0.086,0.242 1.0,0.552,0.165'

    def test_diversity_5(self):
        return '1 1.0 0.0,0.26,0.012 0.274,0.996,0.177 0.461,0.018,0.619 1.0,0.094,0.497'

    def test_diversity_6(self):
        return '1 1.0 0.0,0.303,0.02 0.626,0.638,0.988 1.0,0.071,0.882'

    def test_diversity_7(self):
        return '1 1.0 0.0,0.346,0.577 1.0,0.565,0.413'

    def test_diversity_8(self):
        return '1 1.0 0.0,0.745,0.241 0.425,0.49,0.986 0.661,0.959,0.128 1.0,0.829,0.385'

    def test_diversity_9(self):
        return '1 1.0 0.0,0.793,0.633 1.0,0.679,0.994'

    def test_diversity_10(self):
        return '1 1.0 0.0,0.721,0.388 1.0,0.626,0.947'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '2 1.0 0.0,0.963,0.814 1.0,0.29,0.907'

    def test_diversity_2(self):
        return '2 1.0 0.0,0.663,0.209 1.0,0.169,0.051'

    def test_diversity_3(self):
        return '7 1.0 0.0,0.233,0.77 1.0,0.15,0.205'

    def test_diversity_4(self):
        return '4 1.0 0.0,0.205,0.032 0.171,0.718,0.426 1.0,0.05,0.575'

    def test_diversity_5(self):
        return '3 1.0 0.0,0.906,0.705 1.0,0.929,0.138'

    def test_diversity_6(self):
        return '7 1.0 0.0,0.783,0.608 0.211,0.292,0.001 0.537,0.367,0.155 1.0,0.483,0.245'

    def test_diversity_7(self):
        return '5 1.0 0.0,0.467,0.112 0.216,0.942,0.277 1.0,0.555,0.223'

    def test_diversity_8(self):
        return '7 1.0 0.0,0.975,0.526 1.0,0.057,0.68'

    def test_diversity_9(self):
        return '6 1.0 0.0,0.297,0.986 0.19,0.959,0.714 1.0,0.034,0.123'

    def test_diversity_10(self):
        return '3 1.0 0.0,0.512,0.587 0.476,0.366,0.761 1.0,0.189,0.041'
