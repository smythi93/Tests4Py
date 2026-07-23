from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '1000 4 13 -31 15 3'

    def test_diversity_2(self):
        return '5000 -26 14 9'

    def test_diversity_3(self):
        return '5000 10 -97 1 13 2'

    def test_diversity_4(self):
        return '5000 15 -100 8 14 8 7'

    def test_diversity_5(self):
        return '1000 -106 14 10'

    def test_diversity_6(self):
        return '1000 -62 4 10'

    def test_diversity_7(self):
        return '10000 -53 5 13 15'

    def test_diversity_8(self):
        return '1000 10 9 13 5 -33 11'

    def test_diversity_9(self):
        return '2000 -90 7 3'

    def test_diversity_10(self):
        return '5000 -73 14 11'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '1000 1 4 40 11 37 36'

    def test_diversity_2(self):
        return '1000 27 31 39 35 36 16'

    def test_diversity_3(self):
        return '1000 22 18 20'

    def test_diversity_4(self):
        return '1000 24 37 24'

    def test_diversity_5(self):
        return '1000 28 18 19 13 13 36'

    def test_diversity_6(self):
        return '5000 27 25 15'

    def test_diversity_7(self):
        return '2000 1 21 7 28'

    def test_diversity_8(self):
        return '2000 7 23 10 5 10'

    def test_diversity_9(self):
        return '10000 1 34 8 20 14'

    def test_diversity_10(self):
        return '2000 36 37 33 4 35 25'
