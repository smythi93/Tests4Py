from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'dunder __delattr__'

    def test_diversity_2(self):
        return 'dunder __format__'

    def test_diversity_3(self):
        return 'dunder __reduce_ex__'

    def test_diversity_4(self):
        return 'dunder __reduce__'

    def test_diversity_5(self):
        return 'dunder __init__'

    def test_diversity_6(self):
        return 'dunder __str__'

    def test_diversity_7(self):
        return 'dunder __sizeof__'

    def test_diversity_8(self):
        return 'dunder __hash__'

    def test_diversity_9(self):
        return 'dunder __doc__'

    def test_diversity_10(self):
        return 'dunder __setattr__'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'code W661 pHvLgZM alIU'

    def test_diversity_2(self):
        return 'code E183 NjC kDpr'

    def test_diversity_3(self):
        return 'code W385 AvzDZX ybDrxwc xYxv'

    def test_diversity_4(self):
        return 'code W435 zRJuydKT SzEZCKx jvaoAmJp IoTUcWS'

    def test_diversity_5(self):
        return 'code E083 BEgN tpXmTM'

    def test_diversity_6(self):
        return 'code W648 kGXPRhZ QBNVTkiR Incrckd ltrW'

    def test_diversity_7(self):
        return 'code E789 JzsQOcQ PvkUGar hfCB cWNLwzuA'

    def test_diversity_8(self):
        return 'code E747 quKw EaAe GmCi aeop'

    def test_diversity_9(self):
        return 'code T646 smXfc'

    def test_diversity_10(self):
        return 'code E912 kmzH Trr kUEda'
