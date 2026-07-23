from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '4 0.1,0.449,0.235,0.57'

    def test_diversity_2(self):
        return '3 0.74,0.859,0.854'

    def test_diversity_3(self):
        return '4 0.621,0.577,0.415,0.077'

    def test_diversity_4(self):
        return '3 0.296,0.935,0.715'

    def test_diversity_5(self):
        return '3 0.086,0.755,0.94'

    def test_diversity_6(self):
        return '3 0.134,0.397,0.057'

    def test_diversity_7(self):
        return '4 0.39,0.369,0.413,0.522'

    def test_diversity_8(self):
        return '4 0.844,0.559,0.217,0.673'

    def test_diversity_9(self):
        return '4 0.543,0.519,0.948,0.801'

    def test_diversity_10(self):
        return '3 0.525,0.945,0.393'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '4 0.374,0.123,0.806'

    def test_diversity_2(self):
        return '2 0.503,0.508,0.886'

    def test_diversity_3(self):
        return '7 0.381,0.268,0.081,0.122'

    def test_diversity_4(self):
        return '6 0.856,0.783,0.335,0.095'

    def test_diversity_5(self):
        return '6 0.47,0.051,0.465,0.596'

    def test_diversity_6(self):
        return '7 0.492,0.634,0.373'

    def test_diversity_7(self):
        return '4 0.296,0.532,0.617'

    def test_diversity_8(self):
        return '5 0.284,0.127,0.719'

    def test_diversity_9(self):
        return '6 0.904,0.831,0.301'

    def test_diversity_10(self):
        return '2 0.935,0.892,0.394'
