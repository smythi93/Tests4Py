from tests4py.tests.diversity import Systemtests


class TestsFailing(Systemtests):
    def __init__(self):
        super().__init__(passing=False)

    def test_diversity_1(self):
        return "-otest.log\n-cint=str"

    def test_diversity_2(self):
        return "-cint=str"

    def test_diversity_3(self):
        return "-d1\n-T\n-cint=repr"

    def test_diversity_4(self):
        return "-o\n-d1\n-cbool=str"

    def test_diversity_5(self):
        return "-otest.log\n-O\n-cint=repr,bool=str"

    def test_diversity_6(self):
        return "-wx\n-d1\n-cfloat=str"

    def test_diversity_7(self):
        return "-wy\n-cstr=str"

    def test_diversity_8(self):
        return "-otest.log\n-wx\n-cstr=int"

    def test_diversity_9(self):
        return "-ptest\n-cbool=int"

    def test_diversity_10(self):
        return "-wx\n-ptest\n-cint=str"


class TestsPassing(Systemtests):
    def __init__(self):
        super().__init__(passing=True)

    def test_diversity_1(self):
        return "-otest.log"

    def test_diversity_2(self):
        return ""

    def test_diversity_3(self):
        return "-d1\n-T"

    def test_diversity_4(self):
        return "-o\n-d1"

    def test_diversity_5(self):
        return "-otest.log\n-O"

    def test_diversity_6(self):
        return "-wx\n-d1"

    def test_diversity_7(self):
        return "-wy"

    def test_diversity_8(self):
        return "-otest.log\n-wx"

    def test_diversity_9(self):
        return "-ptest"

    def test_diversity_10(self):
        return "-wx\n-ptest"
