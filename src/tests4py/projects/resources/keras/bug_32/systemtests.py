from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'reduce 1 1'

    def test_diversity_2(self):
        return 'reduce 1 6'

    def test_diversity_3(self):
        return 'reduce 5 6'

    def test_diversity_4(self):
        return 'reduce 4 6'

    def test_diversity_5(self):
        return 'reduce 2 2'

    def test_diversity_6(self):
        return 'reduce 3 5'

    def test_diversity_7(self):
        return 'reduce 2 1'

    def test_diversity_8(self):
        return 'reduce 6 3'

    def test_diversity_9(self):
        return 'reduce 1 2'

    def test_diversity_10(self):
        return 'reduce 4 1'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'noreduce 3 6'

    def test_diversity_2(self):
        return 'noreduce 2 2'

    def test_diversity_3(self):
        return 'noreduce 6 6'

    def test_diversity_4(self):
        return 'noreduce 5 2'

    def test_diversity_5(self):
        return 'noreduce 1 5'

    def test_diversity_6(self):
        return 'noreduce 3 2'

    def test_diversity_7(self):
        return 'noreduce 5 5'

    def test_diversity_8(self):
        return 'noreduce 4 6'

    def test_diversity_9(self):
        return 'noreduce 5 6'

    def test_diversity_10(self):
        return 'noreduce 5 3'
