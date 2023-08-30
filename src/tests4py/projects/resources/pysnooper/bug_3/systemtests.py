from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-otest1.log"

    def test_diversity_2(self):
        return "-otest2.log -d1"

    def test_diversity_3(self):
        return "-otest3.log -vx"

    def test_diversity_4(self):
        return "-otest4.log -vx,y"

    def test_diversity_5(self):
        return "-otest5.log -vw -d2"

    def test_diversity_6(self):
        return "-otest6.log -ptest"

    def test_diversity_7(self):
        return "-otest7.log -d1 -ptest"

    def test_diversity_8(self):
        return "-otest8.log -vx -ptest"

    def test_diversity_9(self):
        return "-otest9.log -d1 -vw,x,y,z"

    def test_diversity_10(self):
        return "-otest10.log -d1 -ptest -vx,z"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return ""

    def test_diversity_2(self):
        return "-o -d1"

    def test_diversity_3(self):
        return "-vx"

    def test_diversity_4(self):
        return "-o -vx,y"

    def test_diversity_5(self):
        return "-vw -d2"

    def test_diversity_6(self):
        return "-o -ptest"

    def test_diversity_7(self):
        return "-d1 -ptest"

    def test_diversity_8(self):
        return "-o -vx -ptest"

    def test_diversity_9(self):
        return "-d1 -vw,x,y,z"

    def test_diversity_10(self):
        return "-o -d1 -ptest -vx,z"
