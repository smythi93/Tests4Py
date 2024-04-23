from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "man -s5 read, Output Message: A"

    def test_diversity_2(self):
        return "man -s4 read, Output Message: B"

    def test_diversity_3(self):
        return "man -s 4 read, Output Message: C"

    def test_diversity_4(self):
        return "man -s 5 write, Output Message: D"

    def test_diversity_5(self):
        return "man read, Output Message: E"

    def test_diversity_6(self):
        return "man 4 read, Output Message: F"

    def test_diversity_7(self):
        return "man 5 write, Output Message: G"

    def test_diversity_8(self):
        return "man missing, Output Message: H"

    def test_diversity_9(self):
        return "man -s5 read, Output Message: I"

    def test_diversity_10(self):
        return "man -s4 read, Output Message: J"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "man -s2 write, Output Message: A"

    def test_diversity_2(self):
        return "man -s3 read, Output Message: B"

    def test_diversity_3(self):
        return "man -s 3 read, Output Message: C"

    def test_diversity_4(self):
        return "man -s 2 read, Output Message: D"

    def test_diversity_5(self):
        return "man read, Output Message: E"

    def test_diversity_6(self):
        return "man 3 write, Output Message: F"

    def test_diversity_7(self):
        return "man 2 read, Output Message: G"

    def test_diversity_8(self):
        return "man missing, Output Message: H"

    def test_diversity_9(self):
        return "man -s2 read, Output Message: I"

    def test_diversity_10(self):
        return "man -s3 write, Output Message: J"
