from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '340'

    def test_diversity_2(self):
        return '238'

    def test_diversity_3(self):
        return '418'

    def test_diversity_4(self):
        return '242'

    def test_diversity_5(self):
        return '538'

    def test_diversity_6(self):
        return '397'

    def test_diversity_7(self):
        return '268'

    def test_diversity_8(self):
        return '555'

    def test_diversity_9(self):
        return '231'

    def test_diversity_10(self):
        return '237'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '404'

    def test_diversity_2(self):
        return '303'

    def test_diversity_3(self):
        return '401'

    def test_diversity_4(self):
        return '409'

    def test_diversity_5(self):
        return '301'

    def test_diversity_6(self):
        return '400'

    def test_diversity_7(self):
        return '500'

    def test_diversity_8(self):
        return '505'

    def test_diversity_9(self):
        return '403'

    def test_diversity_10(self):
        return '206'
