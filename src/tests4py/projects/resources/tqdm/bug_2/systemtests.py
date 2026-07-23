from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '982 ansi 91 KFRZLWANFM'

    def test_diversity_2(self):
        return '825 ansi 95 WIDMSS'

    def test_diversity_3(self):
        return '237 ansi 95 TLWMZY'

    def test_diversity_4(self):
        return '381 ansi 30 JAF'

    def test_diversity_5(self):
        return '406 ansi 30 DFUFZIQE'

    def test_diversity_6(self):
        return '499 ansi 37 ZGJBFJNOJE'

    def test_diversity_7(self):
        return '769 ansi 90 CFICRNOI'

    def test_diversity_8(self):
        return '494 ansi 32 WRYHRYD'

    def test_diversity_9(self):
        return '389 ansi 96 DBAJQMPACO'

    def test_diversity_10(self):
        return '360 ansi 0 UWC'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '592 plain 0 FRUFMAOT'

    def test_diversity_2(self):
        return '711 plain 34 WZYEFM'

    def test_diversity_3(self):
        return '439 plain 4 AKYQNW'

    def test_diversity_4(self):
        return '910 plain 95 XKWYIGCOT'

    def test_diversity_5(self):
        return '774 plain 93 JOGZQHMVYS'

    def test_diversity_6(self):
        return '485 plain 34 PQDZTFMI'

    def test_diversity_7(self):
        return '443 plain 97 FYRQFF'

    def test_diversity_8(self):
        return '400 plain 32 ABIWIDYSVA'

    def test_diversity_9(self):
        return '239 plain 36 IPKRLYXYG'

    def test_diversity_10(self):
        return '636 plain 37 SGTRK'

