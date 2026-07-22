from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'zzJWYXTn'

    def test_diversity_2(self):
        return 'zzONOBJaJ'

    def test_diversity_3(self):
        return 'zzJljLLFrm'

    def test_diversity_4(self):
        return 'zzLAzTTc'

    def test_diversity_5(self):
        return 'zzEDjbE'

    def test_diversity_6(self):
        return 'zzzFXmSaG'

    def test_diversity_7(self):
        return 'zznHiV'

    def test_diversity_8(self):
        return 'zzMnCXKikm'

    def test_diversity_9(self):
        return 'zziAizYu'

    def test_diversity_10(self):
        return 'zzHnZMxWKE'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'echo'

    def test_diversity_2(self):
        return 'tail'

    def test_diversity_3(self):
        return 'ls'

    def test_diversity_4(self):
        return 'sed'

    def test_diversity_5(self):
        return 'find'

    def test_diversity_6(self):
        return 'mv'

    def test_diversity_7(self):
        return 'head'

    def test_diversity_8(self):
        return 'node'

    def test_diversity_9(self):
        return 'wget'

    def test_diversity_10(self):
        return 'curl'
