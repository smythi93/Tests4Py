from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'x false false 15 3'

    def test_diversity_2(self):
        return 'y false false 13 6'

    def test_diversity_3(self):
        return 'x false false 9 6'

    def test_diversity_4(self):
        return 'x false false 8 5'

    def test_diversity_5(self):
        return 'y false false 9 6'

    def test_diversity_6(self):
        return 'y false false 12 3'

    def test_diversity_7(self):
        return 'x false false 15 5'

    def test_diversity_8(self):
        return 'x false false 9 4'

    def test_diversity_9(self):
        return 'x false false 10 6'

    def test_diversity_10(self):
        return 'x false false 7 3'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'x true false 7 5'

    def test_diversity_2(self):
        return 'x true false 8 4'

    def test_diversity_3(self):
        return 'y true true 11 4'

    def test_diversity_4(self):
        return 'x true true 12 4'

    def test_diversity_5(self):
        return 'x false true 14 6'

    def test_diversity_6(self):
        return 'x false true 12 4'

    def test_diversity_7(self):
        return 'x true false 14 5'

    def test_diversity_8(self):
        return 'x true false 7 6'

    def test_diversity_9(self):
        return 'x true false 8 6'

    def test_diversity_10(self):
        return 'y false true 7 5'
