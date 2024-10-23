from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "'20130101' 123 'UTC' 'foo' None"

    def test_diversity_2(self):
        return "'20130101' 34 'US/Eastern' 'foo' None"

    def test_diversity_3(self):
        return "'20130101' 33 'UTC' 'foo' None"

    def test_diversity_4(self):
        return "'20130101' 654 'US/Eastern' 'foo' None"

    def test_diversity_5(self):
        return "'20130101' 941 'Asia/Tokyo' 'foo' None"

    def test_diversity_6(self):
        return "'20130101' 634 'US/Eastern' 'foo' None"

    def test_diversity_7(self):
        return "'20130101' 74 'dateutil/US/Pacific' 'foo' None"

    def test_diversity_8(self):
        return "'20130101' 2 'Asia/Tokyo' 'foo' None"

    def test_diversity_9(self):
        return "'20130101' 33 'UTC' 'foo' None"

    def test_diversity_10(self):
        return "'20130101' 745 'US/Eastern' 'foo' None"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "'20130101' 662 'Asia/Tokyo' 'foo' 'infer'"

    def test_diversity_2(self):
        return "'20130101' 111 'US/Eastern' 'foo' 'infer'"

    def test_diversity_3(self):
        return "'20130101' 99 'US/Eastern' 'foo' 'infer'"

    def test_diversity_4(self):
        return "'20130101' 453 'dateutil/US/Pacific' 'foo' 'infer'"

    def test_diversity_5(self):
        return "'20130101' 746 'US/Eastern' 'foo' 'infer'"

    def test_diversity_6(self):
        return "'20130101' 22 'UTC' 'foo' 'infer'"

    def test_diversity_7(self):
        return "'20130101' 634 'US/Eastern' 'foo' 'infer'"

    def test_diversity_8(self):
        return "'20130101' 53 'dateutil/US/Pacific' 'foo' 'infer'"

    def test_diversity_9(self):
        return "'20130101' 32 'US/Eastern' 'foo' 'infer'"

    def test_diversity_10(self):
        return "'20130101' 11 'Asia/Tokyo' 'foo' 'infer'"
