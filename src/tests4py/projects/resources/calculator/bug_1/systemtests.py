from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "sqrt(-100)"

    def test_diversity_2(self):
        return "sqrt(-15)"

    def test_diversity_3(self):
        return "sqrt(-777)"

    def test_diversity_4(self):
        return "sqrt(-102)"

    def test_diversity_5(self):
        return "sqrt(-1)"

    def test_diversity_6(self):
        return "sqrt(-34)"

    def test_diversity_7(self):
        return "sqrt(-74)"

    def test_diversity_8(self):
        return "sqrt(-0)"

    def test_diversity_9(self):
        return "sqrt(-343)"

    def test_diversity_10(self):
        return "sqrt(-112)"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "sqrt(100)"

    def test_diversity_2(self):
        return "sqrt(42)"

    def test_diversity_3(self):
        return "sqrt(84)"

    def test_diversity_4(self):
        return "tan(120)"

    def test_diversity_5(self):
        return "sqrt(1000)"

    def test_diversity_6(self):
        return "sqrt(232)"

    def test_diversity_7(self):
        return "sqrt(49)"

    def test_diversity_8(self):
        return "sin(864)"

    def test_diversity_9(self):
        return "sqrt(64)"

    def test_diversity_10(self):
        return "cos(16)"
