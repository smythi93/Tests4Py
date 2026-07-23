from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'sf 38.2 monospace'

    def test_diversity_2(self):
        return 'sf 26.4 fantasy'

    def test_diversity_3(self):
        return 'sf 34.3 monospace'

    def test_diversity_4(self):
        return 'sf 36.0 fantasy'

    def test_diversity_5(self):
        return 'sf 26.3 fantasy'

    def test_diversity_6(self):
        return 'sf 41.4 serif'

    def test_diversity_7(self):
        return 'sf 15.2 monospace'

    def test_diversity_8(self):
        return 'sf 48.8 monospace'

    def test_diversity_9(self):
        return 'sf 26.2 monospace'

    def test_diversity_10(self):
        return 'sf 31.6 cursive'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'fs 38.6 monospace'

    def test_diversity_2(self):
        return 'fs 23.4 monospace'

    def test_diversity_3(self):
        return 'fs 17.5 cursive'

    def test_diversity_4(self):
        return 'fs 35.8 fantasy'

    def test_diversity_5(self):
        return 'fs 31.0 fantasy'

    def test_diversity_6(self):
        return 'fs 18.9 cursive'

    def test_diversity_7(self):
        return 'fs 58.8 monospace'

    def test_diversity_8(self):
        return 'fs 57.1 monospace'

    def test_diversity_9(self):
        return 'fs 35.6 serif'

    def test_diversity_10(self):
        return 'fs 49.5 monospace'
