from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'IOLOOP_CLOSE 15'

    def test_diversity_2(self):
        return 'IOLOOP_CLOSE 19'

    def test_diversity_3(self):
        return 'IOLOOP_CLOSE 18'

    def test_diversity_4(self):
        return 'IOLOOP_CLOSE 6'

    def test_diversity_5(self):
        return 'IOLOOP_CLOSE 12'

    def test_diversity_6(self):
        return 'IOLOOP_CLOSE 7'

    def test_diversity_7(self):
        return 'IOLOOP_CLOSE 4'

    def test_diversity_8(self):
        return 'IOLOOP_CLOSE 8'

    def test_diversity_9(self):
        return 'IOLOOP_CLOSE 5'

    def test_diversity_10(self):
        return 'IOLOOP_CLOSE 14'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'KEEP 15'

    def test_diversity_2(self):
        return 'KEEP 11'

    def test_diversity_3(self):
        return 'KEEP 3'

    def test_diversity_4(self):
        return 'KEEP 16'

    def test_diversity_5(self):
        return 'KEEP 17'

    def test_diversity_6(self):
        return 'KEEP 2'

    def test_diversity_7(self):
        return 'KEEP 19'

    def test_diversity_8(self):
        return 'KEEP 8'

    def test_diversity_9(self):
        return 'KEEP 4'

    def test_diversity_10(self):
        return 'KEEP 7'
