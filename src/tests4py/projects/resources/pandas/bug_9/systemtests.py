from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1435-1-17"

    def test_diversity_2(self):
        return "1213-11-7"

    def test_diversity_3(self):
        return "1543-3-4"

    def test_diversity_4(self):
        return "1432-7-11"

    def test_diversity_5(self):
        return "1324-9-30"

    def test_diversity_6(self):
        return "1123-3-3"

    def test_diversity_7(self):
        return "1190-7-7"

    def test_diversity_8(self):
        return "1359-9-21"

    def test_diversity_9(self):
        return "1249-5-23"

    def test_diversity_10(self):
        return "1645-5-21"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "1908-1-6"

    def test_diversity_2(self):
        return "1999-10-11"

    def test_diversity_3(self):
        return "1874-12-1"

    def test_diversity_4(self):
        return "1749-11-17"

    def test_diversity_5(self):
        return "1876-3-13"

    def test_diversity_6(self):
        return "1816-1-12"

    def test_diversity_7(self):
        return "1789-4-16"

    def test_diversity_8(self):
        return "2082-5-10"

    def test_diversity_9(self):
        return "1984-6-21"

    def test_diversity_10(self):
        return "1923-9-22"
