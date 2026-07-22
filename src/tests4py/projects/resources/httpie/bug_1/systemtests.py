from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.txt 5 7 L.txt-5'

    def test_diversity_2(self):
        return 'NNNNNNNNNNNNNNNNNNNNN.dat 5 8 NN.dat-5'

    def test_diversity_3(self):
        return 'LLLLLLLLLLLLLLLLLLLLL.log 0 10 LLLLLL.log'

    def test_diversity_4(self):
        return 'UUUUUUUUUUUUUUUUUUUUU.txt 1 9 UUU.txt-1'

    def test_diversity_5(self):
        return 'PPPPPPPPPPPPPPPPPPPPPP 10 12 PPPPPPPPP-10'

    def test_diversity_6(self):
        return 'LLLLLLLLLLLLLLLLLLL.txt 2 9 LLL.txt-2'

    def test_diversity_7(self):
        return 'JJJJJJJJJJJJJJJJJJJ.dat 5 7 J.dat-5'

    def test_diversity_8(self):
        return 'JJJJJJJJJJJJJJJJJJJJJJJJJ 10 12 JJJJJJJJJ-10'

    def test_diversity_9(self):
        return 'RRRRRRRRRRRRRRRRRRRRRRRRR 10 6 RRR-10'

    def test_diversity_10(self):
        return 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQ.txt 1 6 QQQQ-1'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'gbultik.txt 10 255 gbultik.txt-10'

    def test_diversity_2(self):
        return 'szyaf.txt 10 255 szyaf.txt-10'

    def test_diversity_3(self):
        return 'nqqb 2 255 nqqb-2'

    def test_diversity_4(self):
        return 'omfv 0 255 omfv'

    def test_diversity_5(self):
        return 'quoshz 5 255 quoshz-5'

    def test_diversity_6(self):
        return 'ajtrje.txt 2 255 ajtrje.txt-2'

    def test_diversity_7(self):
        return 'klycvne.txt 10 255 klycvne.txt-10'

    def test_diversity_8(self):
        return 'raaih.png 10 255 raaih.png-10'

    def test_diversity_9(self):
        return 'cwekkhck.txt 10 255 cwekkhck.txt-10'

    def test_diversity_10(self):
        return 'vwu.png 0 255 vwu.png'
