from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'rel aHR0cDovL3R2dXd5aC5vcmcvandn Ly8vZW9qeWN6a24uY29tL3NlaQ=='

    def test_diversity_2(self):
        return 'rel aHR0cDovL2RtdHQubmV0L2dseA== Ly8vYmV6di5jb20vamlr'

    def test_diversity_3(self):
        return 'rel aHR0cDovL2NlemYuY29tL2hubg== Ly8vZHJ4Lm5ldC9ndA=='

    def test_diversity_4(self):
        return 'rel aHR0cDovL3RuZ28uY29tL251eGJ1Yg== Ly8vbmN0ZXdxaC5vcmcva2xndA=='

    def test_diversity_5(self):
        return 'rel aHR0cDovL3ZnbGEuY29tL2F6a3dnbQ== Ly8vZm9qemh3Yy5uZXQvb3Jr'

    def test_diversity_6(self):
        return 'rel aHR0cDovL2NleS5vcmcvbmxt Ly8vZmZ0ZXBnLm5ldC95eG95cQ=='

    def test_diversity_7(self):
        return 'rel aHR0cDovL25vci5jb20vbWNtaWw= Ly8vb2VzemtvLm5ldC9xbnM='

    def test_diversity_8(self):
        return 'rel aHR0cDovL3FuYWx4cHUubmV0L296bm5y Ly8vbXF4YmN4ZHIub3JnL216cmRs'

    def test_diversity_9(self):
        return 'rel aHR0cDovL2Z6Zm5tLm5ldC93aWM= Ly8vbnR6eS5jb20vZGJyYWk='

    def test_diversity_10(self):
        return 'rel aHR0cDovL3VnenYuY29tL2Fq Ly8va2VlbmR2ai5jb20vYXVq'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'abs aHR0cDovL2xhbi5uZXQvYXl3dWU= aHR0cDovL3Fjci5jb20vZ25zdnU='

    def test_diversity_2(self):
        return 'abs aHR0cDovL2JzYy5jb20vdWo= aHR0cDovL25kcWFtdXp4Lm5ldC9qcmQ='

    def test_diversity_3(self):
        return 'abs aHR0cDovL3V5ay5jb20vYWlr aHR0cDovL292eHkubmV0L2libGZx'

    def test_diversity_4(self):
        return 'abs aHR0cDovL2JsZmRhei5jb20vY3c= aHR0cDovL21oZmhpay5uZXQvandrZQ=='

    def test_diversity_5(self):
        return 'abs aHR0cDovL2FucGl0eGwub3JnL2ph aHR0cDovL2p2cmFtYi5vcmcvdWRvYmM='

    def test_diversity_6(self):
        return 'abs aHR0cDovL3JsdHEuY29tL29k aHR0cDovL29maG10Lm9yZy9vcXd4Yw=='

    def test_diversity_7(self):
        return 'abs aHR0cDovL3VtaS5uZXQvdWhz aHR0cDovL2ZvZ2N1Lm9yZy9hZHB5ZGY='

    def test_diversity_8(self):
        return 'abs aHR0cDovL2FscWp2aGQuY29tL2lwbGo= aHR0cDovL3BsamtkdGpyLm5ldC91ZGxh'

    def test_diversity_9(self):
        return 'abs aHR0cDovL2duaHBvamsubmV0L3Bs aHR0cDovL2djcnJuLmNvbS9mZ3d5Ynk='

    def test_diversity_10(self):
        return 'abs aHR0cDovL2lmZmliLmNvbS9tb29k aHR0cDovL2x3Zy5uZXQvb3B5'
