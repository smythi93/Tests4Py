from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "500" '' ''

    def test_diversity_2(self):
        return "111" '' ''

    def test_diversity_3(self):
        return "321" '' ''

    def test_diversity_4(self):
        return "1" '' ''

    def test_diversity_5(self):
        return "6545" '' ''

    def test_diversity_6(self):
        return "322" '' ''

    def test_diversity_7(self):
        return "1299" '' ''

    def test_diversity_8(self):
        return "32" '' ''

    def test_diversity_9(self):
        return "43" '' ''

    def test_diversity_10(self):
        return "766" '' ''


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "git diff jdjdsgs" '' ''

    def test_diversity_2(self):
        return "git diff wefssw" '' ''

    def test_diversity_3(self):
        return "git diff werqsads" '' ''

    def test_diversity_4(self):
        return "git diff FDFWEFSA" '' ''

    def test_diversity_5(self):
        return "git diff FWEDSA" '' ''

    def test_diversity_6(self):
        return "git diff ergefSF" '' ''

    def test_diversity_7(self):
        return "git diff ferfYJYTJ" '' ''

    def test_diversity_8(self):
        return "git diff TRYRFD" '' ''

    def test_diversity_9(self):
        return "git diff HNRTGFVD" '' ''

    def test_diversity_10(self):
        return "git diff WERQFERF" '' ''
