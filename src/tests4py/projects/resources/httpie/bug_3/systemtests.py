from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'Cache=nqc X-Api=wgtz X-Test=__NONE__'

    def test_diversity_2(self):
        return 'X-Trace=jekck X-Api=mltuar Foo=__NONE__'

    def test_diversity_3(self):
        return 'X-Trace=imrwgoa Accept=fgnp X-Test=__NONE__'

    def test_diversity_4(self):
        return 'Authorization=fsj X-Test=__NONE__'

    def test_diversity_5(self):
        return 'Accept=bkx X-Token=__NONE__ X-Test=wgxavk Bar=rwbjidd'

    def test_diversity_6(self):
        return 'Accept=__NONE__ X-Api=lqafv X-Token=ycstrln'

    def test_diversity_7(self):
        return 'X-Trace=uwzryxqz X-Token=__NONE__ Bar=tqaohrz Cache=ltsblur'

    def test_diversity_8(self):
        return 'X-Api=__NONE__ Cache=syakg'

    def test_diversity_9(self):
        return 'X-Test=sjwef X-Custom=__NONE__ X-Api=yyuezi'

    def test_diversity_10(self):
        return 'Bar=geokay X-Trace=__NONE__'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'Foo=hdlfe Bar=rrufsnvi'

    def test_diversity_2(self):
        return 'X-Trace=sshheo'

    def test_diversity_3(self):
        return 'Origin=pbyn X-Token=krmhvww'

    def test_diversity_4(self):
        return 'X-Token=rct Origin=mwmtx Cache=oisvpn'

    def test_diversity_5(self):
        return 'X-Custom=lyutstw Cache=toeuf X-Test=mwnzsofl'

    def test_diversity_6(self):
        return 'X-Token=nroapnis Bar=jqscz Authorization=ypp'

    def test_diversity_7(self):
        return 'Authorization=rdqztazi X-Token=wns X-Api=tafh'

    def test_diversity_8(self):
        return 'X-Trace=lahbhc Referer=pmbayi Origin=yqsvzkj'

    def test_diversity_9(self):
        return 'Origin=ossth'

    def test_diversity_10(self):
        return 'Bar=ubuedy'
