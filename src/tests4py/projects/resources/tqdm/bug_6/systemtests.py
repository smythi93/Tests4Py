from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'gen 752'

    def test_diversity_2(self):
        return 'gen 900'

    def test_diversity_3(self):
        return 'gen 57'

    def test_diversity_4(self):
        return 'gen 371'

    def test_diversity_5(self):
        return 'gen 682'

    def test_diversity_6(self):
        return 'gen 444'

    def test_diversity_7(self):
        return 'gen 675'

    def test_diversity_8(self):
        return 'gen 358'

    def test_diversity_9(self):
        return 'gen 136'

    def test_diversity_10(self):
        return 'gen 465'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'range 463'

    def test_diversity_2(self):
        return 'list 683'

    def test_diversity_3(self):
        return 'list 670'

    def test_diversity_4(self):
        return 'range 19'

    def test_diversity_5(self):
        return 'range 422'

    def test_diversity_6(self):
        return 'range 99'

    def test_diversity_7(self):
        return 'range 93'

    def test_diversity_8(self):
        return 'range 551'

    def test_diversity_9(self):
        return 'list 507'

    def test_diversity_10(self):
        return 'list 517'

