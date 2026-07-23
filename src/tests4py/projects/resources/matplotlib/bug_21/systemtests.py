from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'box caps h'

    def test_diversity_2(self):
        return 'box caps +'

    def test_diversity_3(self):
        return 'box medians h'

    def test_diversity_4(self):
        return 'box medians v'

    def test_diversity_5(self):
        return 'box boxes o'

    def test_diversity_6(self):
        return 'box whiskers p'

    def test_diversity_7(self):
        return 'box boxes ^'

    def test_diversity_8(self):
        return 'box whiskers D'

    def test_diversity_9(self):
        return 'box whiskers x'

    def test_diversity_10(self):
        return 'box medians D'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'flier means o'

    def test_diversity_2(self):
        return 'flier fliers D'

    def test_diversity_3(self):
        return 'flier means v'

    def test_diversity_4(self):
        return 'flier means p'

    def test_diversity_5(self):
        return 'flier means s'

    def test_diversity_6(self):
        return 'flier fliers ^'

    def test_diversity_7(self):
        return 'flier means *'

    def test_diversity_8(self):
        return 'flier fliers s'

    def test_diversity_9(self):
        return 'flier means +'

    def test_diversity_10(self):
        return 'flier means x'
