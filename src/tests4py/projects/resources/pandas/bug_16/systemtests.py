from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "['2292-09', '2292-10', '2292-11', '2292-12'] '2293-12'"

    def test_diversity_2(self):
        return "['1367-09', '1367-10', '1367-11', '1367-12'] '1368-12'"

    def test_diversity_3(self):
        return "['1236-09', '1236-10', '1236-11', '1236-12'] '1237-12'"

    def test_diversity_4(self):
        return "['2001-09', '2001-10', '2001-11', '2001-12'] '2002-12'"

    def test_diversity_5(self):
        return "['6571-09', '6571-10', '6571-11', '6571-12'] '6572-12'"

    def test_diversity_6(self):
        return "['3451-09', '3451-10', '3451-11', '3451-12'] '3452-12'"

    def test_diversity_7(self):
        return "['7531-09', '7531-10', '7531-11', '7531-12'] '7532-12'"

    def test_diversity_8(self):
        return "['4352-09', '4352-10', '4352-11', '4352-12'] '4353-12'"

    def test_diversity_9(self):
        return "['1990-09', '1990-10', '1990-11', '1990-12'] '1991-12'"

    def test_diversity_10(self):
        return "['1012-09', '1012-10', '1012-11', '1012-12'] '1013-12'"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "['1012-01', '1012-02', '1012-03', '1012-04'] '1013-01'"

    def test_diversity_2(self):
        return "['4612-01', '4612-02', '4612-03', '4612-04'] '4613-01'"

    def test_diversity_3(self):
        return "['6712-01', '6712-02', '6712-03', '6712-04'] '6713-01'"

    def test_diversity_4(self):
        return "['3451-01', '3451-02', '3451-03', '3451-04'] '3452-01'"

    def test_diversity_5(self):
        return "['1324-01', '1324-02', '1324-03', '1324-04'] '1325-01'"

    def test_diversity_6(self):
        return "['6432-01', '6432-02', '6432-03', '6432-04'] '6433-01'"

    def test_diversity_7(self):
        return "['9876-01', '9876-02', '9876-03', '9876-04'] '9877-01'"

    def test_diversity_8(self):
        return "['5672-01', '5672-02', '5672-03', '5672-04'] '5673-01'"

    def test_diversity_9(self):
        return "['5316-01', '5316-02', '5316-03', '5316-04'] '5317-01'"

    def test_diversity_10(self):
        return "['7865-01', '7865-02', '7865-03', '7865-04'] '7866-01'"
