from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'diff uniform 1337 4 3'

    def test_diversity_2(self):
        return 'diff normal 7 5 2'

    def test_diversity_3(self):
        return 'diff truncated 42 3 3'

    def test_diversity_4(self):
        return 'diff varscale 100 6 4'

    def test_diversity_5(self):
        return 'diff uniform 555 2 5'

    def test_diversity_6(self):
        return 'diff normal 888 4 4'

    def test_diversity_7(self):
        return 'diff truncated 271 5 5'

    def test_diversity_8(self):
        return 'diff varscale 12 3 6'

    def test_diversity_9(self):
        return 'diff uniform 9001 7 2'

    def test_diversity_10(self):
        return 'diff normal 314 2 8'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'shape uniform 11 4 3'

    def test_diversity_2(self):
        return 'shape normal 22 5 2'

    def test_diversity_3(self):
        return 'shape truncated 33 3 3'

    def test_diversity_4(self):
        return 'shape varscale 44 6 4'

    def test_diversity_5(self):
        return 'shape uniform 55 2 5'

    def test_diversity_6(self):
        return 'shape normal 66 4 4'

    def test_diversity_7(self):
        return 'shape truncated 77 5 5'

    def test_diversity_8(self):
        return 'shape varscale 88 3 6'

    def test_diversity_9(self):
        return 'shape uniform 99 7 2'

    def test_diversity_10(self):
        return 'shape normal 101 2 8'
