from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(True, 'ls -lah /QXrjcUnoOmPPuqv')"

    def test_diversity_2(self):
        return "(True, 'ls -lah /aTdseJywIMA')"

    def test_diversity_3(self):
        return "(True, 'ls -lah /cCcmovRv')"

    def test_diversity_4(self):
        return "(True, 'pacman -s JbumHVHV')"

    def test_diversity_5(self):
        return "(True, 'ls -lah /roNgdpljCe')"

    def test_diversity_6(self):
        return "(True, 'pacman -s NMrAUHXvtFGs')"

    def test_diversity_7(self):
        return "(True, 'pacman -s mbzkyCaT')"

    def test_diversity_8(self):
        return "(True, 'pacman -s IrGevJw')"

    def test_diversity_9(self):
        return "(True, 'ls -lah /cqQBEEPEdxUAsWU')"

    def test_diversity_10(self):
        return "(True, 'ls -lah /zQDRkHBzdAUth')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "(True, 'ls JikWszBqxy.py')"

    def test_diversity_2(self):
        return "(True, 'ls oXavAoCqAnGEkx.py')"

    def test_diversity_3(self):
        return "(True, 'ls CeAaVC.py')"

    def test_diversity_4(self):
        return "(True, 'ls eXzljjjbcGOMWc.py')"

    def test_diversity_5(self):
        return "(True, 'ls UFiYpHkpzpzc.py')"

    def test_diversity_6(self):
        return "(True, 'ls MnXLNZokOinW.py')"

    def test_diversity_7(self):
        return "(True, 'ls /RiuqqOLsKXEkw')"

    def test_diversity_8(self):
        return "(True, 'ls /hTjYWURVxABhu')"

    def test_diversity_9(self):
        return "(True, 'ls /FIFCLVmHnDPbzD')"

    def test_diversity_10(self):
        return "(True, 'ls /brREiSsNu')"
