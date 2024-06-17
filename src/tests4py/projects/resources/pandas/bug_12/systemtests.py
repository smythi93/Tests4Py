from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "[1.0, 2.0, 3.0]"

    def test_diversity_2(self):
        return "[6.0, 7.0, 8.0]"

    def test_diversity_3(self):
        return "[90.0, 91.0, 92.0]"

    def test_diversity_4(self):
        return "[331.0, 332.0, 333.0]"

    def test_diversity_5(self):
        return "[765.0, 766.0, 767.0]"

    def test_diversity_6(self):
        return "[553.0, 554.0, 555.0]"

    def test_diversity_7(self):
        return "[7860.0, 7861.0, 7862.0]"

    def test_diversity_8(self):
        return "[77.0, 78.0, 79.0]"

    def test_diversity_9(self):
        return "[100.0, 101.0, 102.0]"

    def test_diversity_10(self):
        return "[67.0, 68.0, 69.0]"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "[62.0, 63.0, 64.0]"

    def test_diversity_2(self):
        return "[123.0, 124.0, 125.0]"

    def test_diversity_3(self):
        return "[678.0, 679.0, 680.0]"

    def test_diversity_4(self):
        return "[999.0, 1000.0, 1001.0]"

    def test_diversity_5(self):
        return "[54.0, 55.0, 56.0]"

    def test_diversity_6(self):
        return "[4.0, 5.0, 6.0]"

    def test_diversity_7(self):
        return "[1.0, 2.0, 3.0]"

    def test_diversity_8(self):
        return "[6.0, 7.0, 8.0]"

    def test_diversity_9(self):
        return "[868.0, 868.0, 868.0]"

    def test_diversity_10(self):
        return "[67.0, 68.0, 69.0]"
