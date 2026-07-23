from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'torch int 4 3'

    def test_diversity_2(self):
        return 'torch int 5 3'

    def test_diversity_3(self):
        return 'torch int 2 3'

    def test_diversity_4(self):
        return 'caffe int 6 2'

    def test_diversity_5(self):
        return 'tf int 2 4'

    def test_diversity_6(self):
        return 'tf int 4 3'

    def test_diversity_7(self):
        return 'tf int 5 4'

    def test_diversity_8(self):
        return 'caffe int 2 4'

    def test_diversity_9(self):
        return 'tf int 2 6'

    def test_diversity_10(self):
        return 'tf int 3 6'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'torch float 5 6'

    def test_diversity_2(self):
        return 'tf float 6 2'

    def test_diversity_3(self):
        return 'torch float 3 6'

    def test_diversity_4(self):
        return 'tf float 3 3'

    def test_diversity_5(self):
        return 'torch float 4 6'

    def test_diversity_6(self):
        return 'caffe float 3 3'

    def test_diversity_7(self):
        return 'torch float 6 3'

    def test_diversity_8(self):
        return 'tf float 3 4'

    def test_diversity_9(self):
        return 'torch float 5 2'

    def test_diversity_10(self):
        return 'caffe float 4 2'
