from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "700 190 890 ast.Gt()"

    def test_diversity_2(self):
        return "666 333 999 ast.Gt()"

    def test_diversity_3(self):
        return "400 143 543 ast.Gt()"

    def test_diversity_4(self):
        return "30 48 78 ast.Gt()"

    def test_diversity_5(self):
        return "99 401 500 ast.Gt()"

    def test_diversity_6(self):
        return "35 40 75 ast.Gt()"

    def test_diversity_7(self):
        return "301 400 701 ast.Gt()"

    def test_diversity_8(self):
        return "300 401 701 ast.Gt()"

    def test_diversity_9(self):
        return "330 440 770 ast.Gt()"

    def test_diversity_10(self):
        return "10 10 20 ast.Gt()"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "360 340 700 ast.Eq()"

    def test_diversity_2(self):
        return "760 40 800 ast.Eq()"

    def test_diversity_3(self):
        return "66 22 88 ast.Eq()"

    def test_diversity_4(self):
        return "3000 4000 7000 ast.Eq()"

    def test_diversity_5(self):
        return "300 400 700 ast.Eq()"

    def test_diversity_6(self):
        return "30 40 70 ast.Eq()"

    def test_diversity_7(self):
        return "3 4 7 ast.Eq()"

    def test_diversity_8(self):
        return "15 40 55 ast.Eq()"

    def test_diversity_9(self):
        return "350 450 800 ast.Eq()"

    def test_diversity_10(self):
        return "310 140 450 ast.Eq()"
