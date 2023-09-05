from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):

    def test_diversity_1(self):
        return '&a&quot;'

    def test_diversity_2(self):
        return '&a&eacute;'

    def test_diversity_3(self):
        return '&anna&&eacute;ric'

    def test_diversity_4(self):
        return '&anna&#47;&eacute;ric'

    def test_diversity_5(self):
        return '&&#47;'

    def test_diversity_6(self):
        return '&&#x2F;'

    def test_diversity_7(self):
        return '&&period;'

    def test_diversity_8(self):
        return '&&apos;'

    def test_diversity_9(self):
        return '&&apos;&period;'

    def test_diversity_10(self):
        return '&period;&&apos;'


class TestsPassing(PassingSystemtests):

    def test_diversity_1(self):
        return "%20;"

    def test_diversity_2(self):
        return "&#x2F;"

    def test_diversity_3(self):
        return "&#47;"

    def test_diversity_4(self):
        return "&eacute;"

    def test_diversity_5(self):
        return "&#2013266066;"

    def test_diversity_6(self):
        return '&period;&apos;'

    def test_diversity_7(self):
        return '&eacute;ric'

    def test_diversity_8(self):
        return '&period;'

    def test_diversity_9(self):
        return '&apos;'

    def test_diversity_10(self):
        return '%10;'
