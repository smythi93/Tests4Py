from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'datalim 1.233 324.226'

    def test_diversity_2(self):
        return 'datalim 1.994 509.476'

    def test_diversity_3(self):
        return 'datalim 0.503 194.322'

    def test_diversity_4(self):
        return 'datalim 1.129 391.72'

    def test_diversity_5(self):
        return 'datalim 1.051 266.638'

    def test_diversity_6(self):
        return 'datalim 0.599 239.202'

    def test_diversity_7(self):
        return 'datalim 0.9 349.553'

    def test_diversity_8(self):
        return 'datalim 1.44 545.533'

    def test_diversity_9(self):
        return 'datalim 0.79 253.964'

    def test_diversity_10(self):
        return 'datalim 0.654 141.104'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'box 1.81 625.14'

    def test_diversity_2(self):
        return 'box 1.622 434.086'

    def test_diversity_3(self):
        return 'box 1.276 332.217'

    def test_diversity_4(self):
        return 'box 0.674 246.51'

    def test_diversity_5(self):
        return 'box 1.92 567.142'

    def test_diversity_6(self):
        return 'box 1.237 292.324'

    def test_diversity_7(self):
        return 'box 1.356 342.998'

    def test_diversity_8(self):
        return 'box 1.0 313.523'

    def test_diversity_9(self):
        return 'box 1.742 643.487'

    def test_diversity_10(self):
        return 'box 1.804 720.528'
