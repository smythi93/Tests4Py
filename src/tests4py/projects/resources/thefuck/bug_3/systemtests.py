from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_2(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_3(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_4(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_5(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_6(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_7(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_8(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_9(self):
        return "Error Retrieving Shell, Error Details"

    def test_diversity_10(self):
        return "Error Retrieving Shell, Error Details"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "Fish Shell 3.6.1"

    def test_diversity_2(self):
        return "Fish Shell 3.6.0"

    def test_diversity_3(self):
        return "Fish Shell 3.5.1"

    def test_diversity_4(self):
        return "Fish Shell 3.5.0"

    def test_diversity_5(self):
        return "Fish Shell 3.4.1"

    def test_diversity_6(self):
        return "Fish Shell 2.5.0"

    def test_diversity_7(self):
        return "Fish Shell 2.4.1"

    def test_diversity_8(self):
        return "Fish Shell 2.4.0"

    def test_diversity_9(self):
        return "Fish Shell 2.3.1"

    def test_diversity_10(self):
        return "Fish Shell 2.3.0"
