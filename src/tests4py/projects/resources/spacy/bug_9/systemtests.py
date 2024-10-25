from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "GREFREF UserWarning"

    def test_diversity_2(self):
        return "YTJHTYHT UserWarning"

    def test_diversity_3(self):
        return "RTYRYRT UserWarning"

    def test_diversity_4(self):
        return "DFGFDGD UserWarning"

    def test_diversity_5(self):
        return "DRGERGERGEA UserWarning"

    def test_diversity_6(self):
        return "sfefewfweg UserWarning"

    def test_diversity_7(self):
        return "herhrehger UserWarning"

    def test_diversity_8(self):
        return "werewrew UserWarning"

    def test_diversity_9(self):
        return "gerggerfe UserWarning"

    def test_diversity_10(self):
        return "grwfgwfw UserWarning"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "kjwjnfw"

    def test_diversity_2(self):
        return "sdfswer"

    def test_diversity_3(self):
        return "gerregd"

    def test_diversity_4(self):
        return "fwefwefw"

    def test_diversity_5(self):
        return "wrgwfw"

    def test_diversity_6(self):
        return "GWRGFWE"

    def test_diversity_7(self):
        return "SFGSDFS"

    def test_diversity_8(self):
        return "WRFKJFG"

    def test_diversity_9(self):
        return "SDLFSDIJ"

    def test_diversity_10(self):
        return "KADJHA"
