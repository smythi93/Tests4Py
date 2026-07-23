from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'datetime 2019-08-01,2019-11-03'

    def test_diversity_2(self):
        return 'datetime 2019-02-15,2019-07-21,2019-10-07'

    def test_diversity_3(self):
        return 'datetime 2019-02-05,2019-05-03,2019-07-01,2019-12-06'

    def test_diversity_4(self):
        return 'datetime 2019-01-30,2019-05-22,2019-09-06'

    def test_diversity_5(self):
        return 'datetime 2019-03-06,2019-05-24,2019-06-14,2019-07-13'

    def test_diversity_6(self):
        return 'datetime 2019-07-23,2019-12-16'

    def test_diversity_7(self):
        return 'datetime 2019-02-01,2019-03-21,2019-08-22,2019-10-25'

    def test_diversity_8(self):
        return 'datetime 2019-01-18,2019-06-12'

    def test_diversity_9(self):
        return 'datetime 2019-03-08,2019-10-27,2019-11-22'

    def test_diversity_10(self):
        return 'datetime 2019-06-30,2019-08-30,2019-08-31,2019-09-05'

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'numeric 2019-02-14,2019-02-28,2019-08-21,2019-11-06'

    def test_diversity_2(self):
        return 'numeric 2019-02-21,2019-05-06,2019-09-27,2019-12-16'

    def test_diversity_3(self):
        return 'numeric 2019-03-01,2019-03-11,2019-04-16,2019-08-12'

    def test_diversity_4(self):
        return 'numeric 2019-10-24,2019-11-22'

    def test_diversity_5(self):
        return 'numeric 2019-08-12,2019-10-23,2019-11-23'

    def test_diversity_6(self):
        return 'numeric 2019-06-20,2019-06-21,2019-07-12,2019-11-23'

    def test_diversity_7(self):
        return 'numeric 2019-03-31,2019-12-13'

    def test_diversity_8(self):
        return 'numeric 2019-02-14,2019-03-17,2019-09-15'

    def test_diversity_9(self):
        return 'numeric 2019-02-20,2019-04-20,2019-10-31'

    def test_diversity_10(self):
        return 'numeric 2019-03-21,2019-11-02'
