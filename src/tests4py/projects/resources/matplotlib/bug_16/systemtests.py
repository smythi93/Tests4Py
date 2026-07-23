from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "int8 -128 -128"

    def test_diversity_2(self):
        return "int8 -128 0"

    def test_diversity_3(self):
        return "int8 -128 1"

    def test_diversity_4(self):
        return "int16 -32768 -32768"

    def test_diversity_5(self):
        return "int16 -32768 0"

    def test_diversity_6(self):
        return "int16 -32768 2"

    def test_diversity_7(self):
        return "int32 -2147483648 -2147483648"

    def test_diversity_8(self):
        return "int32 -2147483648 0"

    def test_diversity_9(self):
        return "int64 -9223372036854775808 -9223372036854775808"

    def test_diversity_10(self):
        return "int64 -9223372036854775808 0"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "float64 1.0 5.0"

    def test_diversity_2(self):
        return "float64 -10.0 10.0"

    def test_diversity_3(self):
        return "float64 0.5 3.5"

    def test_diversity_4(self):
        return "float64 -2.5 7.5"

    def test_diversity_5(self):
        return "float64 2.0 8.0"

    def test_diversity_6(self):
        return "float64 -100.0 -50.0"

    def test_diversity_7(self):
        return "float64 3.14 9.42"

    def test_diversity_8(self):
        return "float64 -1.0 1.0"

    def test_diversity_9(self):
        return "float64 10.5 20.5"

    def test_diversity_10(self):
        return "float64 -7.0 -3.0"

