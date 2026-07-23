from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'both <html><body><p>gnjjzm</p></body></html>'

    def test_diversity_2(self):
        return 'both <html><body><p>vrpordle</p></body></html>'

    def test_diversity_3(self):
        return 'both <html><body><p>bvbr</p></body></html>'

    def test_diversity_4(self):
        return 'both <html><body><p>rucxv</p></body></html>'

    def test_diversity_5(self):
        return 'both <html><body><p>nczycldi</p></body></html>'

    def test_diversity_6(self):
        return 'both <html><body><p>ozxoncp</p></body></html>'

    def test_diversity_7(self):
        return 'both <html><body><p>pmjaszzr</p></body></html>'

    def test_diversity_8(self):
        return 'both <html><body><p>ywkig</p></body></html>'

    def test_diversity_9(self):
        return 'both <html><body><p>jnvna</p></body></html>'

    def test_diversity_10(self):
        return 'both <html><body><p>waarbfptf</p></body></html>'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'text <html><body><p>hlmpsnji</p></body></html>'

    def test_diversity_2(self):
        return 'response <html><body><p>swgzmo</p></body></html>'

    def test_diversity_3(self):
        return 'text <html><body><p>tfpy</p></body></html>'

    def test_diversity_4(self):
        return 'response <html><body><p>gabq</p></body></html>'

    def test_diversity_5(self):
        return 'response <html><body><p>naiuvqf</p></body></html>'

    def test_diversity_6(self):
        return 'response <html><body><p>qgyxeh</p></body></html>'

    def test_diversity_7(self):
        return 'text <html><body><p>iwqlu</p></body></html>'

    def test_diversity_8(self):
        return 'response <html><body><p>grsdxkg</p></body></html>'

    def test_diversity_9(self):
        return 'response <html><body><p>zoqxzt</p></body></html>'

    def test_diversity_10(self):
        return 'response <html><body><p>pxupjj</p></body></html>'

