from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'cli 266633'

    def test_diversity_2(self):
        return 'cli 58524'

    def test_diversity_3(self):
        return 'cli 427314'

    def test_diversity_4(self):
        return 'cli 837428'

    def test_diversity_5(self):
        return 'cli 66624'

    def test_diversity_6(self):
        return 'cli 990522'

    def test_diversity_7(self):
        return 'cli 185556'

    def test_diversity_8(self):
        return 'cli 672241'

    def test_diversity_9(self):
        return 'cli 383179'

    def test_diversity_10(self):
        return 'cli 118992'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'import 949153'

    def test_diversity_2(self):
        return 'import 707156'

    def test_diversity_3(self):
        return 'import 44460'

    def test_diversity_4(self):
        return 'import 895726'

    def test_diversity_5(self):
        return 'import 194932'

    def test_diversity_6(self):
        return 'import 615020'

    def test_diversity_7(self):
        return 'import 55603'

    def test_diversity_8(self):
        return 'import 510130'

    def test_diversity_9(self):
        return 'import 304923'

    def test_diversity_10(self):
        return 'import 430690'
