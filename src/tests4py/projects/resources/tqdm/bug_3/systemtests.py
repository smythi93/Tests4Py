from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'gen 32'

    def test_diversity_2(self):
        return 'gen 245'

    def test_diversity_3(self):
        return 'gen 992'

    def test_diversity_4(self):
        return 'gen 758'

    def test_diversity_5(self):
        return 'gen 199'

    def test_diversity_6(self):
        return 'gen 94'

    def test_diversity_7(self):
        return 'gen 579'

    def test_diversity_8(self):
        return 'gen 969'

    def test_diversity_9(self):
        return 'gen 638'

    def test_diversity_10(self):
        return 'gen 264'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'total 161'

    def test_diversity_2(self):
        return 'total 484'

    def test_diversity_3(self):
        return 'list 262'

    def test_diversity_4(self):
        return 'list 608'

    def test_diversity_5(self):
        return 'list 711'

    def test_diversity_6(self):
        return 'total 141'

    def test_diversity_7(self):
        return 'total 296'

    def test_diversity_8(self):
        return 'list 842'

    def test_diversity_9(self):
        return 'total 286'

    def test_diversity_10(self):
        return 'list 234'

