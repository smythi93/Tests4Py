from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "E110"

    def test_diversity_2(self):
        return "E019"

    def test_diversity_3(self):
        return "E034"

    def test_diversity_4(self):
        return "E003"

    def test_diversity_5(self):
        return "E111"

    def test_diversity_6(self):
        return "E155"

    def test_diversity_7(self):
        return "E153"

    def test_diversity_8(self):
        return "E022"

    def test_diversity_9(self):
        return "E058"

    def test_diversity_10(self):
        return "E044"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "E177"

    def test_diversity_2(self):
        return "E181"

    def test_diversity_3(self):
        return "E122"

    def test_diversity_4(self):
        return "E099"

    def test_diversity_5(self):
        return "E012"

    def test_diversity_6(self):
        return "E123"

    def test_diversity_7(self):
        return "E021"

    def test_diversity_8(self):
        return "E188"

    def test_diversity_9(self):
        return "E015"

    def test_diversity_10(self):
        return "E158"
