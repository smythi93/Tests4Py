from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "initializers.orthogonal 1281 ast.Gt()"

    def test_diversity_2(self):
        return "initializers.orthogonal 7655 ast.Lt()"

    def test_diversity_3(self):
        return "initializers.normal 1256 ast.Gt()"

    def test_diversity_4(self):
        return "initializers.uniform 6342 ast.Gt()"

    def test_diversity_5(self):
        return "initializers.truncated_normal 1233 ast.Gt()"

    def test_diversity_6(self):
        return "initializers.variance_scaling 4555 ast.Lt()"

    def test_diversity_7(self):
        return "initializers.uniform 4221 ast.Gt()"

    def test_diversity_8(self):
        return "initializers.variance_scaling 5612 ast.Lt()"

    def test_diversity_9(self):
        return "initializers.uniform 5612 ast.Lt()"

    def test_diversity_10(self):
        return "initializers.variance_scaling 9812 ast.Lt()"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "initializers.orthogonal 6432 ast.Eq()"

    def test_diversity_2(self):
        return "initializers.orthogonal 3434 ast.Eq()"

    def test_diversity_3(self):
        return "initializers.normal 8999 ast.Eq()"

    def test_diversity_4(self):
        return "initializers.uniform 1235 ast.Eq()"

    def test_diversity_5(self):
        return "initializers.truncated_normal 2323 ast.Eq()"

    def test_diversity_6(self):
        return "initializers.variance_scaling 1211 ast.Eq()"

    def test_diversity_7(self):
        return "initializers.uniform 6534 ast.Eq()"

    def test_diversity_8(self):
        return "initializers.variance_scaling 3422 ast.Eq()"

    def test_diversity_9(self):
        return "initializers.uniform 4252 ast.Eq()"

    def test_diversity_10(self):
        return "initializers.variance_scaling 6322 ast.Eq()"
