from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "-o\"{'foo':'test'}\" -d"

    def test_diversity_2(self):
        return "-o\"Model(foo='test')\" -d"

    def test_diversity_3(self):
        return "-o\"Model(foo='bar',bar='foo')\" -d -ne -a"

    def test_diversity_4(self):
        return "-o\"Model(foo='bar',bar='foo',bla='da')\" -u -d -s"

    def test_diversity_5(self):
        return "-d -q -o\"Model(foo='bar',bar='foo',bla='da')\""

    def test_diversity_6(self):
        return "-o\"Model(foo='bar',bar='foo',bla='da')\" -d -c{str:repr}"

    def test_diversity_7(self):
        return "-ne -a -o\"Model(foo='bar',bar='foo',bla='da')\" -ifoo -d -c{str:repr}"

    def test_diversity_8(self):
        return "-o\"Model(foo='bar',bar='foo')\" -q -d"

    def test_diversity_9(self):
        return "-o\"{'foo':'1','bar':'2','bla':'3','da':'4'}\" -d -ebla"

    def test_diversity_10(self):
        return "-o\"Model(foo='bar',bar='foo')\" -ifoo -ebla -d -c{str:repr}"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "-o\"{'foo':'test'}\""

    def test_diversity_2(self):
        return "-o\"Model(foo='test')\""

    def test_diversity_3(self):
        return "-o\"Model(foo='bar',bar='foo')\" -a"

    def test_diversity_4(self):
        return "-o\"Model(foo='bar',bar='foo',bla='da')\" -u -s"

    def test_diversity_5(self):
        return "-q -o\"Model(foo='bar',bar='foo',bla='da')\""

    def test_diversity_6(self):
        return "-o\"Model(foo='bar',bar='foo',bla='da')\" -c{str:repr}"

    def test_diversity_7(self):
        return "-a -o\"Model(foo='bar',bar='foo',bla='da')\" -ifoo -c{str:repr}"

    def test_diversity_8(self):
        return "-o\"Model(foo='bar',bar='foo')\" -q"

    def test_diversity_9(self):
        return "-o\"{'foo':'1','bar':'2','bla':'3','da':'4'}\" -ebla"

    def test_diversity_10(self):
        return "-o\"Model(foo='bar',bar='foo')\" -ifoo -ebla -c{str:repr}"
