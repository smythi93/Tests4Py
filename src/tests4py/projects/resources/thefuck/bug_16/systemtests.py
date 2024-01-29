from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "fuck"

    def test_diversity_2(self):
        return "thefuck"

    def test_diversity_3(self):
        return "FUCK"

    def test_diversity_4(self):
        return "HDHddusfugs"

    def test_diversity_5(self):
        return "krngeruvenj"

    def test_diversity_6(self):
        return "uJGKhdfhf"

    def test_diversity_7(self):
        return "rgefgre"

    def test_diversity_8(self):
        return "fenfdseefe"

    def test_diversity_9(self):
        return "HJDSgdshjdg"

    def test_diversity_10(self):
        return "jrfhugd"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "fuck"

    def test_diversity_2(self):
        return "FUCK"

    def test_diversity_3(self):
        return "thefuck"

    def test_diversity_4(self):
        return "mjerew"

    def test_diversity_5(self):
        return "efrwger"

    def test_diversity_6(self):
        return "FDSweda"

    def test_diversity_7(self):
        return "fdsGResa"

    def test_diversity_8(self):
        return "KGrjwuai"

    def test_diversity_9(self):
        return "dkjfdssDSF"

    def test_diversity_10(self):
        return "sfNDSUFGUahs"
