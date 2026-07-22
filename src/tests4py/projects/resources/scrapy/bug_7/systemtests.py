from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'aHR0cDovL3R2dXd5aC5pbw== IGRsb2UgIA=='

    def test_diversity_2(self):
        return 'aHR0cDovL2hxY3Iub3Jn ICBnbnN2dS9kbXQvcmdseGR6IA=='

    def test_diversity_3(self):
        return 'aHR0cDovL3V1anIuY29t IGJxaXBreS9qcmQg'

    def test_diversity_4(self):
        return 'aHR0cDovL3l3Z3RidGwub3Jn IGFpayA='

    def test_diversity_5(self):
        return 'aHR0cDovL3VuY3RlLmNvbQ== IHJrbGd0L2JsZmRhIA=='

    def test_diversity_6(self):
        return 'aHR0cDovL2lmZHkuY29t IGliY2RmL25ldGF3YyAg'

    def test_diversity_7(self):
        return 'aHR0cDovL3BpbGlraGpxLmNvbQ== IGNlL2lmICA='

    def test_diversity_8(self):
        return 'aHR0cDovL2NvZi5uZXQ= IGpycm9xIA=='

    def test_diversity_9(self):
        return 'aHR0cDovL3NheXhzZnFhLmlv IHl6Zi9nb2EgIA=='

    def test_diversity_10(self):
        return 'aHR0cDovL21xeGJjeGRyLmlv ICBtenJkbC9hbHFqdmgva2lxICA='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'aHR0cDovL3ljemtuZHNlLm5ldA== bGEvenRheXd1'

    def test_diversity_2(self):
        return 'aHR0cDovL3pqaWsuY29t c2M='

    def test_diversity_3(self):
        return 'aHR0cDovL2V6ZmVobi5jb20= cng='

    def test_diversity_4(self):
        return 'aHR0cDovL25rZHF0cS5vcmc= bmdvL25zci9nbA=='

    def test_diversity_5(self):
        return 'aHR0cDovL3Blay5vcmc= Zmhpay9odWJlY3Y='

    def test_diversity_6(self):
        return 'aHR0cDovL2FucGl0eGwuaW8= cndqdg=='

    def test_diversity_7(self):
        return 'aHR0cDovL21seGl1ai5vcmc= eXhveXEvcmx0L2J4Yg=='

    def test_diversity_8(self):
        return 'aHR0cDovL3h4amtya2Mub3Jn bGRmcS9nd3VlYQ=='

    def test_diversity_9(self):
        return 'aHR0cDovL2RwaGgub3Jn eHB1cXIvb3pubnI='

    def test_diversity_10(self):
        return 'aHR0cDovL2pydy5jb20= bXB0d3YvdWRsYQ=='
