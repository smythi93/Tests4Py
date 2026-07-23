from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "git semi"

    def test_diversity_2(self):
        return "ls semi"

    def test_diversity_3(self):
        return "cat semi"

    def test_diversity_4(self):
        return "echo semi"

    def test_diversity_5(self):
        return "cp semi"

    def test_diversity_6(self):
        return "mv semi"

    def test_diversity_7(self):
        return "rm semi"

    def test_diversity_8(self):
        return "date semi"

    def test_diversity_9(self):
        return "grep semi"

    def test_diversity_10(self):
        return "sort semi"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "head plain"

    def test_diversity_2(self):
        return "tail plain"

    def test_diversity_3(self):
        return "uniq plain"

    def test_diversity_4(self):
        return "wc plain"

    def test_diversity_5(self):
        return "pwd plain"

    def test_diversity_6(self):
        return "sed plain"

    def test_diversity_7(self):
        return "awk plain"

    def test_diversity_8(self):
        return "find plain"

    def test_diversity_9(self):
        return "tar plain"

    def test_diversity_10(self):
        return "curl plain"
