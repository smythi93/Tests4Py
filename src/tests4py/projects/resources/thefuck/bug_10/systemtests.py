from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "man -s5 read"

    def test_diversity_2(self):
        return "man -s4 read"

    def test_diversity_3(self):
        return "man -s 4 read"

    def test_diversity_4(self):
        return "man -s 5 write"

    def test_diversity_5(self):
        return "man read"

    def test_diversity_6(self):
        return "man 4 read"

    def test_diversity_7(self):
        return "man 5 write"

    def test_diversity_8(self):
        return "man missing"

    def test_diversity_9(self):
        return "man -s5 read"

    def test_diversity_10(self):
        return "man -s4 read"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "man -s2 write"

    def test_diversity_2(self):
        return "man -s3 read"

    def test_diversity_3(self):
        return "man -s 3 read"

    def test_diversity_4(self):
        return "man -s 2 read"

    def test_diversity_5(self):
        return "man read"

    def test_diversity_6(self):
        return "man 3 write"

    def test_diversity_7(self):
        return "man 2 read"

    def test_diversity_8(self):
        return "man missing"

    def test_diversity_9(self):
        return "man -s2 read"

    def test_diversity_10(self):
        return "man -s3 write"
