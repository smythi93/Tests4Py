from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '2001-11-23T02:06:49.1098+0300'

    def test_diversity_2(self):
        return '2000-06-21T19:30:39.9+0200'

    def test_diversity_3(self):
        return '2016-08-08T02:42:34.78+0100'

    def test_diversity_4(self):
        return '2011-05-08T20:59:12.52564+0800'

    def test_diversity_5(self):
        return '2002-10-16T05:04:35.03761Z'

    def test_diversity_6(self):
        return '2003-09-05T21:19:29.03Z'

    def test_diversity_7(self):
        return '2004-08-02T18:24:48.2811+0730'

    def test_diversity_8(self):
        return '2005-08-24T16:52:28.84748+0400'

    def test_diversity_9(self):
        return '2016-02-27T15:24:52.47-0400'

    def test_diversity_10(self):
        return '2018-05-05T23:20:50.179+1100'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '2002-07-07T01:57:18Z'

    def test_diversity_2(self):
        return '2007-09-27T02:50:59-0530'

    def test_diversity_3(self):
        return '2014-02-19T08:54:04-0600'

    def test_diversity_4(self):
        return '2003-07-07T22:56:56+0800'

    def test_diversity_5(self):
        return '2011-04-17T22:26:11-0330'

    def test_diversity_6(self):
        return '2001-06-18T04:31:58-0730'

    def test_diversity_7(self):
        return '2004-03-02T19:10:59Z'

    def test_diversity_8(self):
        return '2017-02-23T10:10:00-1000'

    def test_diversity_9(self):
        return '2020-02-25T04:58:13Z'

    def test_diversity_10(self):
        return '2013-07-24T10:13:52-0630'
