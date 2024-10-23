from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "165 8 4 'not in index'"

    def test_diversity_2(self):
        return "265 8 87 'not in index'"

    def test_diversity_3(self):
        return "365 2338 47 'not in index'"

    def test_diversity_4(self):
        return "465 2358 8 'not in index'"

    def test_diversity_5(self):
        return "5565 6238 387 'not in index'"

    def test_diversity_6(self):
        return "765 638 482 'not in index'"

    def test_diversity_7(self):
        return "865 235 454 'not in index'"

    def test_diversity_8(self):
        return "658 233 488 'not in index'"

    def test_diversity_9(self):
        return "695 232 400 'not in index'"

    def test_diversity_10(self):
        return "605 2218 457 'not in index'"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "2 222 22 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_2(self):
        return "66 4 6 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_3(self):
        return "7543 51 3 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_4(self):
        return "33 88 99 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_5(self):
        return "345 12 3123 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_6(self):
        return "123 32 54 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_7(self):
        return "126 12 54 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_8(self):
        return "366 115 38 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_9(self):
        return "33 15 58 'None of \\[.*\\] are in the \\[index\\]'"

    def test_diversity_10(self):
        return "3 23 712 'None of \\[.*\\] are in the \\[index\\]'"
