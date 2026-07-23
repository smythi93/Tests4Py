from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'content aHR0cDovL3R2dXd5aC5vcmcvcm9ib3RzLnR4dA== U2l0ZW1hcDogaHR0cDovL3B4aWJkbXQubmV0L2dseGQueG1sClNpdGVtYXA6IGh0dHA6Ly9penp0YXkuY29tL2Vja3hwdGcueG1sClVzZXItYWdlbnQ6ICoKU2l0ZW1hcDogaHR0cDovL3BldHQubmV0L3BlZmN2aS54bWwKRGlzYWxsb3c6IC9qd2cK'

    def test_diversity_2(self):
        return 'content aHR0cDovL2xrdWVhc2ZuLmNvbS9yb2JvdHMudHh0 U2l0ZW1hcDogaHR0cDovL2pyZGQub3JnL3hpZmUueG1sClVzZXItYWdlbnQ6ICoKRGlzYWxsb3c6IC9xYW11egpTaXRlbWFwOiBodHRwOi8vYnRsZXhlLm9yZy9lZW92eC54bWwKU2l0ZW1hcDogaHR0cDovL25uYWEub3JnL3Z5d2cueG1sCg=='

    def test_diversity_3(self):
        return 'content aHR0cDovL3RuZ28uY29tL3JvYm90cy50eHQ= U2l0ZW1hcDogaHR0cDovL25jdGV3cWgub3JnL2tsZ3RtLnhtbApEaXNhbGxvdzogL2dsClVzZXItYWdlbnQ6ICoKU2l0ZW1hcDogaHR0cDovL2xmZGF6LmNvbS9jd3cueG1sCg=='

    def test_diversity_4(self):
        return 'content aHR0cDovL2tlZC5vcmcvcm9ib3RzLnR4dA== VXNlci1hZ2VudDogKgpTaXRlbWFwOiBodHRwOi8vZXRhd2MuY29tL255emFucGkueG1sCkRpc2FsbG93OiAvaWZkClNpdGVtYXA6IGh0dHA6Ly9sbGphLm9yZy9yb3BpbC54bWwKU2l0ZW1hcDogaHR0cDovL3VpaS5jb20vY2Rmby54bWwK'

    def test_diversity_5(self):
        return 'content aHR0cDovL3BhYi5jb20vcm9ib3RzLnR4dA== U2l0ZW1hcDogaHR0cDovL3hpdWoubmV0L3pybWUueG1sCkRpc2FsbG93OiAvbG0KU2l0ZW1hcDogaHR0cDovL295cWUubmV0L3dhZnV0by54bWwKVXNlci1hZ2VudDogKgo='

    def test_diversity_6(self):
        return 'content aHR0cDovL3d4Y2F4eC5vcmcvcm9ib3RzLnR4dA== VXNlci1hZ2VudDogKgpEaXNhbGxvdzogL2tyawpTaXRlbWFwOiBodHRwOi8vZ2hvZXMub3JnL29xdXFuLnhtbAo='

    def test_diversity_7(self):
        return 'content aHR0cDovL3Voc2oubmV0L3JvYm90cy50eHQ= VXNlci1hZ2VudDogKgpTaXRlbWFwOiBodHRwOi8vZHB5LmNvbS9mdnFuYS54bWwKRGlzYWxsb3c6IC9meGZ4Cg=='

    def test_diversity_8(self):
        return 'content aHR0cDovL213bXF4YmN4LmNvbS9yb2JvdHMudHh0 RGlzYWxsb3c6IC9yeHRtClVzZXItYWdlbnQ6ICoKU2l0ZW1hcDogaHR0cDovL2pydy5jb20vcm1wdHcueG1sClNpdGVtYXA6IGh0dHA6Ly9xdGZxdGVhZS5uZXQveGtpcWkueG1sCg=='

    def test_diversity_9(self):
        return 'content aHR0cDovL212cHdpLmNvbS9yb2JvdHMudHh0 U2l0ZW1hcDogaHR0cDovL25zZmcub3JnL2NzZC54bWwKU2l0ZW1hcDogaHR0cDovL3VkYi5uZXQvYWlwcS54bWwKU2l0ZW1hcDogaHR0cDovL2hwb2prcHAub3JnL2djcnJuLnhtbApVc2VyLWFnZW50OiAqCkRpc2FsbG93OiAvZWJzCg=='

    def test_diversity_10(self):
        return 'content aHR0cDovL3JubWMubmV0L3JvYm90cy50eHQ= U2l0ZW1hcDogaHR0cDovL2x3Zy5uZXQvb3B5Zy54bWwKRGlzYWxsb3c6IC90YQpTaXRlbWFwOiBodHRwOi8veWlmZi5vcmcvYmVtb29kLnhtbApVc2VyLWFnZW50OiAqCg=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'empty aHR0cDovL2ppa2EuY29tL3JvYm90cy50eHQ= eA=='

    def test_diversity_2(self):
        return 'empty aHR0cDovL3F0cS5uZXQvcm9ib3RzLnR4dA== eA=='

    def test_diversity_3(self):
        return 'empty aHR0cDovL2ZoaWtxLm9yZy9yb2JvdHMudHh0 eA=='

    def test_diversity_4(self):
        return 'empty aHR0cDovL2pxb20uY29tL3JvYm90cy50eHQ= eA=='

    def test_diversity_5(self):
        return 'empty aHR0cDovL2d6Zmpycm8ubmV0L3JvYm90cy50eHQ= eA=='

    def test_diversity_6(self):
        return 'empty aHR0cDovL3VtaS5uZXQvcm9ib3RzLnR4dA== eA=='

    def test_diversity_7(self):
        return 'empty aHR0cDovL3B1cXJsb2hoLmNvbS9yb2JvdHMudHh0 eA=='

    def test_diversity_8(self):
        return 'empty aHR0cDovL2xhdGZ6Zi5uZXQvcm9ib3RzLnR4dA== eA=='

    def test_diversity_9(self):
        return 'empty aHR0cDovL2Rsay5jb20vcm9ib3RzLnR4dA== eA=='

    def test_diversity_10(self):
        return 'empty aHR0cDovL2tmY3hxZXVlLm5ldC9yb2JvdHMudHh0 eA=='
