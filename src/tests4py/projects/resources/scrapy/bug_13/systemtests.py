from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'default 33429'

    def test_diversity_2(self):
        return 'default 7415'

    def test_diversity_3(self):
        return 'default 53514'

    def test_diversity_4(self):
        return 'default 8427'

    def test_diversity_5(self):
        return 'default 23294'

    def test_diversity_6(self):
        return 'default 84130'

    def test_diversity_7(self):
        return 'default 47997'

    def test_diversity_8(self):
        return 'default 14973'

    def test_diversity_9(self):
        return 'default 88494'

    def test_diversity_10(self):
        return 'default 5657'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'custom 24466'

    def test_diversity_2(self):
        return 'custom 76977'

    def test_diversity_3(self):
        return 'custom 7050'

    def test_diversity_4(self):
        return 'custom 63866'

    def test_diversity_5(self):
        return 'custom 38215'

    def test_diversity_6(self):
        return 'custom 53936'

    def test_diversity_7(self):
        return 'custom 79114'

    def test_diversity_8(self):
        return 'custom 30458'

    def test_diversity_9(self):
        return 'custom 52681'

    def test_diversity_10(self):
        return 'custom 86204'
