from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'cHJpbnQgInVubnVyaGUiLCBmdnZqbmsK'

    def test_diversity_2(self):
        return 'cHJpbnQgbm9sY2phCg=='

    def test_diversity_3(self):
        return 'cHJpbnQgInpjeSIK'

    def test_diversity_4(self):
        return 'cHJpbnQgImNlaGFteCIK'

    def test_diversity_5(self):
        return 'cHJpbnQgInNrY3RuIgo='

    def test_diversity_6(self):
        return 'cHJpbnQgcHlydGdnY2MK'

    def test_diversity_7(self):
        return 'cHJpbnQgImJoZHJxIgo='

    def test_diversity_8(self):
        return 'cHJpbnQgZXVjam51aGUK'

    def test_diversity_9(self):
        return 'cHJpbnQgIndiaXRyZWRvIiwgenF0d215Cg=='

    def test_diversity_10(self):
        return 'cHJpbnQgb3ZpbiwgYnVoYnNkemYK'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'ZGVmIGVjbnRidyhteXpnKToKICAgIHJldHVybiA2Cg=='

    def test_diversity_2(self):
        return 'cHJpbnQoImh4bm4iKQo='

    def test_diversity_3(self):
        return 'ZGVmIHFtbm1pYShqeWV1em0pOgogICAgcmV0dXJuIDgK'

    def test_diversity_4(self):
        return 'ZGVmIHd2aHUodHRrKToKICAgIHJldHVybiA4Cg=='

    def test_diversity_5(self):
        return 'cHJpbnQoImFsd20iKQo='

    def test_diversity_6(self):
        return 'ZGVmIGxhcW5pdnNnKHlhYnV4cnEpOgogICAgcmV0dXJuIDYK'

    def test_diversity_7(self):
        return 'cXF5dmlzbSA9IDQK'

    def test_diversity_8(self):
        return 'cHJpbnQoImpzZyIpCg=='

    def test_diversity_9(self):
        return 'eGdmbGhiZGEgPSAwCg=='

    def test_diversity_10(self):
        return 'ZGVmIGZya3Qodmp5eSk6CiAgICByZXR1cm4gOAo='
