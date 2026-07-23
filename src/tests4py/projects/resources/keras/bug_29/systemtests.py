from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'dict 200 0'

    def test_diversity_2(self):
        return 'dict 250 1'

    def test_diversity_3(self):
        return 'dict 180 2'

    def test_diversity_4(self):
        return 'dict 300 3'

    def test_diversity_5(self):
        return 'dict 160 4'

    def test_diversity_6(self):
        return 'dict 220 5'

    def test_diversity_7(self):
        return 'dict 190 6'

    def test_diversity_8(self):
        return 'dict 270 7'

    def test_diversity_9(self):
        return 'dict 150 8'

    def test_diversity_10(self):
        return 'dict 240 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'list 200 10'

    def test_diversity_2(self):
        return 'list 250 11'

    def test_diversity_3(self):
        return 'list 180 12'

    def test_diversity_4(self):
        return 'list 300 13'

    def test_diversity_5(self):
        return 'list 160 14'

    def test_diversity_6(self):
        return 'list 220 15'

    def test_diversity_7(self):
        return 'list 190 16'

    def test_diversity_8(self):
        return 'list 270 17'

    def test_diversity_9(self):
        return 'list 150 18'

    def test_diversity_10(self):
        return 'list 240 19'
