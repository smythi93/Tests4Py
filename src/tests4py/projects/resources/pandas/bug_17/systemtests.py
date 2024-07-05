from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "1241 1067-7-11 UTC"

    def test_diversity_2(self):
        return "1621 1067-7-11 UTC"

    def test_diversity_3(self):
        return "12 1067-7-11 dateutil/Asia/Singapore"

    def test_diversity_4(self):
        return "7635 1067-7-11 US/Eastern"

    def test_diversity_5(self):
        return "133 1067-7-11 UTC"

    def test_diversity_6(self):
        return "877 1067-7-11 dateutil/Asia/Singapore"

    def test_diversity_7(self):
        return "6432 1067-7-11 US/Eastern"

    def test_diversity_8(self):
        return "645 1067-7-11 dateutil/Asia/Singapore"

    def test_diversity_9(self):
        return "423 1067-7-11 US/Eastern"

    def test_diversity_10(self):
        return "756 1067-7-11 UTC"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "86 2067-7-11 dateutil/Asia/Singapore"

    def test_diversity_2(self):
        return "4 2067-7-11 US/Eastern"

    def test_diversity_3(self):
        return "5 2067-7-11 Asia/Tokyo"

    def test_diversity_4(self):
        return "57 2067-7-11 US/Eastern"

    def test_diversity_5(self):
        return "756 2067-7-11 UTC"

    def test_diversity_6(self):
        return "543 2067-7-11 UTC"

    def test_diversity_7(self):
        return "432 2067-7-11 dateutil/Asia/Singapore"

    def test_diversity_8(self):
        return "409 2067-7-11 US/Eastern"

    def test_diversity_9(self):
        return "54 2067-7-11 Asia/Tokyo"

    def test_diversity_10(self):
        return "756 2067-7-11 US/Eastern"
