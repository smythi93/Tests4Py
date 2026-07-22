from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '299 minutes'

    def test_diversity_2(self):
        return '182 min'

    def test_diversity_3(self):
        return '9 mins'

    def test_diversity_4(self):
        return '5.2minute'

    def test_diversity_5(self):
        return '17.8 mins'

    def test_diversity_6(self):
        return '15.2 mins'

    def test_diversity_7(self):
        return '2.5 hour'

    def test_diversity_8(self):
        return '16.6 hour'

    def test_diversity_9(self):
        return '7.8 minute'

    def test_diversity_10(self):
        return '3.1 hour'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '9:45'

    def test_diversity_2(self):
        return '42:24'

    def test_diversity_3(self):
        return '1:04:37'

    def test_diversity_4(self):
        return '10:04'

    def test_diversity_5(self):
        return '1763s'

    def test_diversity_6(self):
        return '0:59:22'

    def test_diversity_7(self):
        return '16:09:42'

    def test_diversity_8(self):
        return '29:02'

    def test_diversity_9(self):
        return '17:42'

    def test_diversity_10(self):
        return '5:17:09'
