from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "'False' 'rmm GrYIK' 'rmm: not found'"

    def test_diversity_2(self):
        return "'False' 'datee IPRacmSKdSANSIz' 'datee: not found'"

    def test_diversity_3(self):
        return "'False' 'echoo crvtgrIxNqOBenJ' 'echoo: not found'"

    def test_diversity_4(self):
        return "'False' 'echoo oKqShsyyFBEXlR' 'echoo: not found'"

    def test_diversity_5(self):
        return "'False' 'wcc vmHdbemz' 'wcc: not found'"

    def test_diversity_6(self):
        return "'False' 'gitt slxygPxK' 'gitt: not found'"

    def test_diversity_7(self):
        return "'False' 'sedd DSdeCJPjFduKG' 'sedd: not found'"

    def test_diversity_8(self):
        return "'False' 'grepp ERvupbcqBuBbzTV' 'grepp: not found'"

    def test_diversity_9(self):
        return "'False' 'gitt VcwWRXAooTwpsQ' 'gitt: not found'"

    def test_diversity_10(self):
        return "'False' 'uniqq VrhfGLrF' 'uniqq: not found'"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "'True' 'gitt TgAUfdBOzwPVy' 'gitt: not found'"

    def test_diversity_2(self):
        return "'True' 'lss BPTPR' 'lss: not found'"

    def test_diversity_3(self):
        return "'True' 'rmm hJZfe' 'rmm: not found'"

    def test_diversity_4(self):
        return "'True' 'gitt ySRlGsN' 'gitt: not found'"

    def test_diversity_5(self):
        return "'True' 'headd BfYhIpMXTDfufL' 'headd: not found'"

    def test_diversity_6(self):
        return "'True' 'echoo rFZSXkOlewl' 'echoo: not found'"

    def test_diversity_7(self):
        return "'True' 'sortt qgUKqKJRbeB' 'sortt: not found'"

    def test_diversity_8(self):
        return "'True' 'pwdd mibCWTpnJV' 'pwdd: not found'"

    def test_diversity_9(self):
        return "'True' 'grepp CFsJCjvw' 'grepp: not found'"

    def test_diversity_10(self):
        return "'True' 'lss WUNTfHDP' 'lss: not found'"
