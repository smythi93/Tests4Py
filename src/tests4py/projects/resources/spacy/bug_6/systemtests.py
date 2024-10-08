from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "sdfjhds ahdqegq 0"

    def test_diversity_2(self):
        return "NJDIUhja ahdssy 0"

    def test_diversity_3(self):
        return "kdjha akjsdjhas 0"

    def test_diversity_4(self):
        return "kjdjhas jhasbdhja 0"

    def test_diversity_5(self):
        return "mnasjd UYDSGUD 0"

    def test_diversity_6(self):
        return "asjdsa easjhfa 0"

    def test_diversity_7(self):
        return "askjndkjhas HJBFEJEWB 0"

    def test_diversity_8(self):
        return "kgkhjGAK VJABHJKHAsd 0"

    def test_diversity_9(self):
        return "amdnsahs jhasbdgha 0"

    def test_diversity_10(self):
        return "dsqhFA ihiHYIUHI 0"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "ksjndfhjs asjhdajhg 1"

    def test_diversity_2(self):
        return "wjhfghw GHSAGHD 1"

    def test_diversity_3(self):
        return "sdfsifhsi asdiuahui 1"

    def test_diversity_4(self):
        return "JHDAHA WDHFWE 1"

    def test_diversity_5(self):
        return "hgHGGH UFYiuj 1"

    def test_diversity_6(self):
        return "GHIUUYI jhgkas 1"

    def test_diversity_7(self):
        return "hsdgh HJHJHNKJ 1"

    def test_diversity_8(self):
        return "kjhdhs aUYGUYIUH 1"

    def test_diversity_9(self):
        return "isdhf HHFdsf 1"

    def test_diversity_10(self):
        return "sdiofsui HGIahrti 1"
