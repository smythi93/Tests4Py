from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'zzJeHCGz'

    def test_diversity_2(self):
        return 'zzitPhTlnT'

    def test_diversity_3(self):
        return 'zzNEXFvUGA'

    def test_diversity_4(self):
        return 'zzIENUDUU'

    def test_diversity_5(self):
        return 'zzXiIjSv'

    def test_diversity_6(self):
        return 'zzJOJQe'

    def test_diversity_7(self):
        return 'zzTKLRFl'

    def test_diversity_8(self):
        return 'zznUgjWKfG'

    def test_diversity_9(self):
        return 'zzZOxPSV'

    def test_diversity_10(self):
        return 'zzEObaDUsS'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'sed'

    def test_diversity_2(self):
        return 'wget'

    def test_diversity_3(self):
        return 'rm'

    def test_diversity_4(self):
        return 'open'

    def test_diversity_5(self):
        return 'tar'

    def test_diversity_6(self):
        return 'make'

    def test_diversity_7(self):
        return 'awk'

    def test_diversity_8(self):
        return 'echo'

    def test_diversity_9(self):
        return 'find'

    def test_diversity_10(self):
        return 'mv'
