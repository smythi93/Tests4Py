from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'withmeta 10 20'

    def test_diversity_2(self):
        return 'withmeta 3 4'

    def test_diversity_3(self):
        return 'withmeta 100 1'

    def test_diversity_4(self):
        return 'withmeta 7 8'

    def test_diversity_5(self):
        return 'withmeta 50 50'

    def test_diversity_6(self):
        return 'withmeta 2 9'

    def test_diversity_7(self):
        return 'withmeta 15 5'

    def test_diversity_8(self):
        return 'withmeta 33 11'

    def test_diversity_9(self):
        return 'withmeta 6 6'

    def test_diversity_10(self):
        return 'withmeta 21 4'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'plain 10 20'

    def test_diversity_2(self):
        return 'plain 3 4'

    def test_diversity_3(self):
        return 'plain 100 1'

    def test_diversity_4(self):
        return 'plain 7 8'

    def test_diversity_5(self):
        return 'plain 50 50'

    def test_diversity_6(self):
        return 'plain 2 9'

    def test_diversity_7(self):
        return 'plain 15 5'

    def test_diversity_8(self):
        return 'plain 33 11'

    def test_diversity_9(self):
        return 'plain 6 6'

    def test_diversity_10(self):
        return 'plain 21 4'
