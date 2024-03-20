from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'mnfjsdfds, weqdas'

    def test_diversity_2(self):
        return 'NRALZctkaukjHs, FbYTY'

    def test_diversity_3(self):
        return 'fdsfwe, gegerf'

    def test_diversity_4(self):
        return 'dsfwefew, wewefgD'

    def test_diversity_5(self):
        return 'lrlJHKR, dalal'

    def test_diversity_6(self):
        return 'groKHHS, hgf'

    def test_diversity_7(self):
        return 'ADhjghjEGF, FbYTY'

    def test_diversity_8(self):
        return 'eretewds, YTJT'

    def test_diversity_9(self):
        return 'fghfghf, FEWFEW'

    def test_diversity_10(self):
        return 'GWEEUUad, FbYTY'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'nrgrtgt: EWRWsdas'

    def test_diversity_2(self):
        return 'asdrwDSD: grerefe'

    def test_diversity_3(self):
        return 'rtwerewc: FbYTY'

    def test_diversity_4(self):
        return 'wqsada: qweqweqw'

    def test_diversity_5(self):
        return 'erwfdf: WDSAS'

    def test_diversity_6(self):
        return 'sdfwew: GFRWS'

    def test_diversity_7(self):
        return 'fewewsdSFSE: FDSFSF'

    def test_diversity_8(self):
        return 'WERSADSFW: ewrwerw'

    def test_diversity_9(self):
        return 'NRALZctkaukjHs: GQWE'

    def test_diversity_10(self):
        return 'kewbfjkw: FbYTY'
