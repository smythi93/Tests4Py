from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "0.78, 0.97, 0.58, 0.52, 0.84 'restore_best_weights' True"

    def test_diversity_2(self):
        return "0.70, 0.97, 0.50, 0.52, 0.81 'restore_best_weights' True"

    def test_diversity_3(self):
        return "0.72, 0.97, 0.59, 0.52, 0.80 'restore_best_weights' True"

    def test_diversity_4(self):
        return "0.74, 0.97, 0.51, 0.52, 0.83 'restore_best_weights' True"

    def test_diversity_5(self):
        return "0.76, 0.97, 0.52, 0.52, 0.85 'restore_best_weights' True"

    def test_diversity_6(self):
        return "0.79, 0.97, 0.53, 0.52, 0.83 'restore_best_weights' True"

    def test_diversity_7(self):
        return "0.71, 0.97, 0.56, 0.52, 0.86 'restore_best_weights' True"

    def test_diversity_8(self):
        return "0.73, 0.97, 0.57, 0.52, 0.88 'restore_best_weights' True"

    def test_diversity_9(self):
        return "0.75, 0.97, 0.58, 0.55, 0.87 'restore_best_weights' True"

    def test_diversity_10(self):
        return "0.77, 0.97, 0.52, 0.51, 0.84 'restore_best_weights' True"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "0.78, 0.91, 0.52, 0.52, 0.83"

    def test_diversity_2(self):
        return "0.70, 0.92, 0.52, 0.52, 0.82"

    def test_diversity_3(self):
        return "0.79, 0.90, 0.52, 0.52, 0.85"

    def test_diversity_4(self):
        return "0.77, 0.93, 0.52, 0.52, 0.87"

    def test_diversity_5(self):
        return "0.76, 0.94, 0.52, 0.52, 0.82"

    def test_diversity_6(self):
        return "0.75, 0.96, 0.52, 0.52, 0.83"

    def test_diversity_7(self):
        return "0.74, 0.95, 0.52, 0.52, 0.84"

    def test_diversity_8(self):
        return "0.73, 0.97, 0.52, 0.52, 0.81"

    def test_diversity_9(self):
        return "0.72, 0.98, 0.52, 0.52, 0.80"

    def test_diversity_10(self):
        return "0.71, 0.99, 0.52, 0.52, 0.89"
