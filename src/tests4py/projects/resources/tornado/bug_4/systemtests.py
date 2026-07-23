from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '110 bytes=-164157'

    def test_diversity_2(self):
        return '115 bytes=14-8'

    def test_diversity_3(self):
        return '158 bytes=25-6'

    def test_diversity_4(self):
        return '63 bytes=-191561'

    def test_diversity_5(self):
        return '15 bytes=-227698'

    def test_diversity_6(self):
        return '39 bytes=-712366'

    def test_diversity_7(self):
        return '103 bytes=-573318'

    def test_diversity_8(self):
        return '118 bytes=-351876'

    def test_diversity_9(self):
        return '11 bytes=6-0'

    def test_diversity_10(self):
        return '24 bytes=21-11'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '135 bytes=23-80'

    def test_diversity_2(self):
        return '192 bytes=-136'

    def test_diversity_3(self):
        return '133 bytes=-77'

    def test_diversity_4(self):
        return '107 bytes=33-93'

    def test_diversity_5(self):
        return '127 bytes=-113'

    def test_diversity_6(self):
        return '85 bytes=66-78'

    def test_diversity_7(self):
        return '52 bytes=24-24'

    def test_diversity_8(self):
        return '117 bytes=20-76'

    def test_diversity_9(self):
        return '103 bytes=-6'

    def test_diversity_10(self):
        return '140 bytes=80-128'
