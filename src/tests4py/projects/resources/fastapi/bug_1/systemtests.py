from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-o{'foo':'test'}\n-d"

    def test_diversity_2(self):
        return "-oModel(foo='test')\n-d"

    def test_diversity_3(self):
        return "-oModel(foo='bar',bar='foo')\n-d\n-ne\n-a"

    def test_diversity_4(self):
        return "-oModel(foo='bar',bar='foo',bla='da')\n-u\n-d\n-s"

    def test_diversity_5(self):
        return "-d\n-q\n-oModel(foo='bar',bar='foo',bla='da')"

    def test_diversity_6(self):
        return "-oModel(foo='bar',bar='foo',bla='da')\n-d\n-c{str:repr}"

    def test_diversity_7(self):
        return "-ne\n-a\n-oModel(foo='bar',bar='foo',bla='da')\n-ifoo\n-d\n-c{str:repr}"

    def test_diversity_8(self):
        return "-oModel(foo='bar',bar='foo')\n-q\n-d"

    def test_diversity_9(self):
        return "-o{'foo':'1','bar':'2','bla':'3','da':'4'}\n-d\n-ebla"

    def test_diversity_10(self):
        return "-oModel(foo='bar',bar='foo')\n-ifoo\n-ebla\n-d\n-c{str:repr}"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-o{'foo':'test'}"

    def test_diversity_2(self):
        return "-oModel(foo='test')"

    def test_diversity_3(self):
        return "-oModel(foo='bar',bar='foo')\n-a"

    def test_diversity_4(self):
        return "-oModel(foo='bar',bar='foo',bla='da')\n-u\n-s"

    def test_diversity_5(self):
        return "-q\n-oModel(foo='bar',bar='foo',bla='da')"

    def test_diversity_6(self):
        return "-oModel(foo='bar',bar='foo',bla='da')\n-c{str:repr}"

    def test_diversity_7(self):
        return "-a\n-oModel(foo='bar',bar='foo',bla='da')\n-ifoo\n-c{str:repr}"

    def test_diversity_8(self):
        return "-oModel(foo='bar',bar='foo')\n-q"

    def test_diversity_9(self):
        return "-o{'foo':'1','bar':'2','bla':'3','da':'4'}\n-ebla"

    def test_diversity_10(self):
        return "-oModel(foo='bar',bar='foo')\n-ifoo\n-ebla\n-c{str:repr}"
