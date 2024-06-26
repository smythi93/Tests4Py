from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "340 P"

    def test_diversity_2(self):
        return "3 P"

    def test_diversity_3(self):
        return "144 P"

    def test_diversity_4(self):
        return "413 R"

    def test_diversity_5(self):
        return "35 R"

    def test_diversity_6(self):
        return "7890 P"

    def test_diversity_7(self):
        return "873 R"

    def test_diversity_8(self):
        return "634 P"

    def test_diversity_9(self):
        return "756 R"

    def test_diversity_10(self):
        return "7832 R"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "53 D"

    def test_diversity_2(self):
        return "873 B"

    def test_diversity_3(self):
        return "65 D"

    def test_diversity_4(self):
        return "5743 B"

    def test_diversity_5(self):
        return "13 D"

    def test_diversity_6(self):
        return "42 D"

    def test_diversity_7(self):
        return "3 B"

    def test_diversity_8(self):
        return "435 B"

    def test_diversity_9(self):
        return "3453 D"

    def test_diversity_10(self):
        return "5123 B"
