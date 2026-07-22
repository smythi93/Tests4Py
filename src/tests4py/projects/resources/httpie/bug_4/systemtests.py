from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'http://26.9.23.229/bwplgig hosT test797.net'

    def test_diversity_2(self):
        return 'http://43.57.125.20/eymrrewf hosT test35.org'

    def test_diversity_3(self):
        return 'http://108.218.190.177/ydlz hOST httpbin494.org'

    def test_diversity_4(self):
        return 'http://79.24.134.252/wellh hOST server850.net'

    def test_diversity_5(self):
        return 'http://159.246.185.148/mwmcyzgg hOST service144.net'

    def test_diversity_6(self):
        return 'http://62.162.2.253/smsz HOsT api351.com'

    def test_diversity_7(self):
        return 'http://67.27.112.47/mekly HOST test743.org'

    def test_diversity_8(self):
        return 'http://162.238.69.254/jajz HOST test318.io'

    def test_diversity_9(self):
        return 'http://186.136.81.1/wet HoST httpbin966.com'

    def test_diversity_10(self):
        return 'http://56.143.97.74/bwp HOST test34.net'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'http://145.130.190.70/vbp - api918.org'

    def test_diversity_2(self):
        return 'http://209.104.233.138/aecyojwd Host httpbin540.org'

    def test_diversity_3(self):
        return 'http://95.79.239.11/dtz Host service735.org'

    def test_diversity_4(self):
        return 'http://178.36.2.26/hmbzotzo Host example379.io'

    def test_diversity_5(self):
        return 'http://93.213.31.143/vjini - httpbin892.io'

    def test_diversity_6(self):
        return 'http://223.11.232.9/qzyywbd - server953.org'

    def test_diversity_7(self):
        return 'http://57.246.151.247/zgargtw - service155.org'

    def test_diversity_8(self):
        return 'http://20.43.243.32/jkupmbz - service583.net'

    def test_diversity_9(self):
        return 'http://1.132.74.104/dubwufi Host service167.net'

    def test_diversity_10(self):
        return 'http://57.229.159.8/srk - httpbin353.io'
