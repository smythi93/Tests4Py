from tests4py.tests.diversity import Systemtests


class TestsFailing(Systemtests):
    def __init__(self):
        super().__init__(passing=False)

    def test_diversity_1(self):
        return "-otest1.log"

    def test_diversity_2(self):
        return "-otest2.log\n-d1"

    def test_diversity_3(self):
        return "-otest3.log\n-vx"

    def test_diversity_4(self):
        return "-otest4.log\n-vx,y"

    def test_diversity_5(self):
        return "-otest5.log\n-vw\n-d2"

    def test_diversity_6(self):
        return "-otest6.log\n-ptest"

    def test_diversity_7(self):
        return "-otest7.log\n-d1\n-ptest"

    def test_diversity_8(self):
        return "-otest8.log\n-vx\n-ptest"

    def test_diversity_9(self):
        return "-otest9.log\n-d1\n-vw,x,y,z"

    def test_diversity_10(self):
        return "-otest10.log\n-d1\n-ptest\n-vx,z"


class TestsPassing(Systemtests):
    def __init__(self):
        super().__init__(passing=True)

    def test_diversity_1(self):
        return ""

    def test_diversity_2(self):
        return "-o\n-d1"

    def test_diversity_3(self):
        return "-vx"

    def test_diversity_4(self):
        return "-o\n-vx,y"

    def test_diversity_5(self):
        return "-vw\n-d2"

    def test_diversity_6(self):
        return "-o\n-ptest"

    def test_diversity_7(self):
        return "-d1\n-ptest"

    def test_diversity_8(self):
        return "-o\n-vx\n-ptest"

    def test_diversity_9(self):
        return "-d1\n-vw,x,y,z"

    def test_diversity_10(self):
        return "-o\n-d1\n-ptest\n-vx,z"
