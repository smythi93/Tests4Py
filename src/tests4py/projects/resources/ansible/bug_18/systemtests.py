from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'kali os 2002.3'

    def test_diversity_2(self):
        return 'kali os 2064.3'

    def test_diversity_3(self):
        return 'kali os 2005.7'

    def test_diversity_4(self):
        return 'kali os 2066.2'

    def test_diversity_5(self):
        return 'kali os 2065.0'

    def test_diversity_6(self):
        return 'kali os 2090.2'

    def test_diversity_7(self):
        return 'kali os 2066.1'

    def test_diversity_8(self):
        return 'kali os 2068.6'

    def test_diversity_9(self):
        return 'kali os 2075.9'

    def test_diversity_10(self):
        return 'kali os 2007.6'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'kali lsb 2070.4'

    def test_diversity_2(self):
        return 'ubuntu os 2082.7'

    def test_diversity_3(self):
        return 'kali lsb 2026.6'

    def test_diversity_4(self):
        return 'kali lsb 2008.1'

    def test_diversity_5(self):
        return 'steamos os 2051.7'

    def test_diversity_6(self):
        return 'kali lsb 2072.2'

    def test_diversity_7(self):
        return 'ubuntu os 2078.8'

    def test_diversity_8(self):
        return 'ubuntu os 2061.9'

    def test_diversity_9(self):
        return 'kali lsb 2006.8'

    def test_diversity_10(self):
        return 'steamos lsb 2001.3'
