from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'strict 2 5 3 0'

    def test_diversity_2(self):
        return 'strict 3 6 4 1'

    def test_diversity_3(self):
        return 'strict 4 4 2 2'

    def test_diversity_4(self):
        return 'strict 2 8 5 3'

    def test_diversity_5(self):
        return 'strict 5 5 3 4'

    def test_diversity_6(self):
        return 'strict 3 4 4 5'

    def test_diversity_7(self):
        return 'strict 2 6 2 6'

    def test_diversity_8(self):
        return 'strict 4 7 3 7'

    def test_diversity_9(self):
        return 'strict 3 5 5 8'

    def test_diversity_10(self):
        return 'strict 5 4 2 9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'lenient 2 5 3 10'

    def test_diversity_2(self):
        return 'lenient 3 6 4 11'

    def test_diversity_3(self):
        return 'lenient 4 4 2 12'

    def test_diversity_4(self):
        return 'lenient 2 8 5 13'

    def test_diversity_5(self):
        return 'lenient 5 5 3 14'

    def test_diversity_6(self):
        return 'lenient 3 4 4 15'

    def test_diversity_7(self):
        return 'lenient 2 6 2 16'

    def test_diversity_8(self):
        return 'lenient 4 7 3 17'

    def test_diversity_9(self):
        return 'lenient 3 5 5 18'

    def test_diversity_10(self):
        return 'lenient 5 4 2 19'
