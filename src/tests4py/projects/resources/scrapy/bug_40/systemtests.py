from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eydhbW91bnQnOiA4NS40OTMsICdib29sZWFuJzogMTMuMDcsICdjb3VudCc6IC0yMzV9'

    def test_diversity_2(self):
        return 'eydudW1iZXInOiBUcnVlLCAnbGV2ZWwnOiA3MTV9'

    def test_diversity_3(self):
        return 'eydudW1iZXInOiAtNTYuMTU3LCAnYm9vbGVhbic6IFRydWV9'

    def test_diversity_4(self):
        return 'eydsZXZlbCc6IEZhbHNlLCAnYm9vbGVhbic6IDM5MH0='

    def test_diversity_5(self):
        return 'eydmbGFnJzogLTE2LjQ5LCAncmF0aW8nOiA4ODIsICdib29sZWFuJzogLTk0NH0='

    def test_diversity_6(self):
        return 'eydsZXZlbCc6IC0yNTQsICdib29sZWFuJzogVHJ1ZSwgJ2NvdW50JzogVHJ1ZSwgJ3JhdGlvJzogLTIzOX0='

    def test_diversity_7(self):
        return 'eydjb3VudCc6IC02NzEsICdib29sZWFuJzogLTcwNywgJ3JhdGlvJzogLTUzLjAxNX0='

    def test_diversity_8(self):
        return 'eydmbGFnJzogRmFsc2UsICdsZXZlbCc6IFRydWV9'

    def test_diversity_9(self):
        return 'eydjb3VudCc6IC0yMTUsICdhbW91bnQnOiBUcnVlfQ=='

    def test_diversity_10(self):
        return 'eydyYXRpbyc6IEZhbHNlLCAnZmxhZyc6IC0xODEsICdib29sZWFuJzogMzYuNjEyLCAnYW1vdW50JzogLTYuODJ9'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eydzbHVnJzogJ29lb2p5JywgJ2tpbmQnOiAnbnRwJ30='

    def test_diversity_2(self):
        return 'eydsYWJlbCc6ICdhbnJrYScsICduYW1lJzogJ3d1ZWNreHB0JywgJ2tpbmQnOiAneXB4aSd9'

    def test_diversity_3(self):
        return 'eydjb2RlJzogJ2JlenYnLCAna2luZCc6ICd6amlrJywgJ3NsdWcnOiAnYnNjJ30='

    def test_diversity_4(self):
        return 'eydzbHVnJzogJ3FpcCcsICduYW1lJzogJ3hvanJkZCcsICdraW5kJzogJ2V6ZmVobicsICd0YWcnOiAnc2RyeHZ5dyd9'

    def test_diversity_5(self):
        return 'eydsYWJlbCc6ICdlcm5nJywgJ3RpdGxlJzogJ25rZHF0cScsICdraW5kJzogJ2ZkeGlobnMnfQ=='

    def test_diversity_6(self):
        return 'eyd0YWcnOiAnamhwaW1ibGYnLCAnbmFtZSc6ICd4cnF5JywgJ2xhYmVsJzogJ2N3dycsICdraW5kJzogJ2VqeHN3Yid9'

    def test_diversity_7(self):
        return 'eyd0aXRsZSc6ICd5YXonLCAnbmFtZSc6ICdpYmNkZm8nLCAnc2x1Zyc6ICdldGF3Yyd9'

    def test_diversity_8(self):
        return 'eyd0aXRsZSc6ICd0eGxsamFrJywgJ2NvZGUnOiAndnJhbWJpdWQnLCAndGFnJzogJ3FvbWRwYWInLCAnbGFiZWwnOiAnbmxtbCd9'

    def test_diversity_9(self):
        return 'eydraW5kJzogJ3JsdHEnLCAndGl0bGUnOiAndXRvJywgJ3RhZyc6ICdjb2YnLCAnY29kZSc6ICdmanJybyd9'

    def test_diversity_10(self):
        return 'eyd0aXRsZSc6ICdvZXN6a28nLCAna2luZCc6ICd1ZWF0aHVtaScsICdsYWJlbCc6ICdmcWFrZm9nYyd9'
