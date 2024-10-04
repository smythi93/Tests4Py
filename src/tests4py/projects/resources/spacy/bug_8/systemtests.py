from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1231 -"

    def test_diversity_2(self):
        return "7 -"

    def test_diversity_3(self):
        return "786 -"

    def test_diversity_4(self):
        return "868 -"

    def test_diversity_5(self):
        return "35 -"

    def test_diversity_6(self):
        return "3783 -"

    def test_diversity_7(self):
        return "7837 -"

    def test_diversity_8(self):
        return "3278 -"

    def test_diversity_9(self):
        return "383 -"

    def test_diversity_10(self):
        return "455 -"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "asjhduasd +"

    def test_diversity_2(self):
        return "ajhbdjhweqf *"

    def test_diversity_3(self):
        return "kjdskhHYJJJ ?"

    def test_diversity_4(self):
        return "GHBDFkjerr 1"

    def test_diversity_5(self):
        return "jkskwrr *"

    def test_diversity_6(self):
        return "ilkopkpS 1"

    def test_diversity_7(self):
        return "KJIFW *"

    def test_diversity_8(self):
        return "JHSDFUSs 1"

    def test_diversity_9(self):
        return "wjHJDSFJ ?"

    def test_diversity_10(self):
        return "huweihw +"
