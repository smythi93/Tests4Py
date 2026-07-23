from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJ0X2lkIjogInRfcGlnY2twc3giLCAidF90aXRsZSI6ICJseXVwZWdpIGFwZHp0IiwgImZpbmFsX2lkIjogImZfYnRpZ3N6aCIsICJmaWVsZCI6ICJpZCIsICJleHBlY3RlZCI6ICJmX2J0aWdzemgifQ=='

    def test_diversity_2(self):
        return 'eyJ0X2lkIjogInRfdmNneGV3ayIsICJ0X3RpdGxlIjogIm5ucGducWYgY2ltaGVzYWYiLCAiZmluYWxfaWQiOiAiZl9iamlid29qIiwgImZpZWxkIjogImlkIiwgImV4cGVjdGVkIjogImZfYmppYndvaiJ9'

    def test_diversity_3(self):
        return 'eyJ0X2lkIjogInRfeWVvZmsiLCAidF90aXRsZSI6ICJicG91amogeHBwd2ZxIiwgImZpbmFsX2lkIjogImZfZ3NsZHVlZGkiLCAiZmllbGQiOiAiaWQiLCAiZXhwZWN0ZWQiOiAiZl9nc2xkdWVkaSJ9'

    def test_diversity_4(self):
        return 'eyJ0X2lkIjogInRfb3h6dnAiLCAidF90aXRsZSI6ICJmb2h2dXZtIHR0eGF5IiwgImZpbmFsX2lkIjogImZfc21uaWJ2aWsiLCAiZmllbGQiOiAiaWQiLCAiZXhwZWN0ZWQiOiAiZl9zbW5pYnZpayJ9'

    def test_diversity_5(self):
        return 'eyJ0X2lkIjogInRfY2VicG9oayIsICJ0X3RpdGxlIjogImZ3Y3ZsIGN6cHRiIiwgImZpbmFsX2lkIjogImZfeWNtbGwiLCAiZmllbGQiOiAiaWQiLCAiZXhwZWN0ZWQiOiAiZl95Y21sbCJ9'

    def test_diversity_6(self):
        return 'eyJ0X2lkIjogInRfZG1pYyIsICJ0X3RpdGxlIjogInFrZ2VzZXNpIHJ2dXpoayIsICJmaW5hbF9pZCI6ICJmX3BjdnVqdyIsICJmaWVsZCI6ICJpZCIsICJleHBlY3RlZCI6ICJmX3BjdnVqdyJ9'

    def test_diversity_7(self):
        return 'eyJ0X2lkIjogInRfZGZqdSIsICJ0X3RpdGxlIjogInl5dHFvb3BrIGJhdGRldHciLCAiZmluYWxfaWQiOiAiZl9xb3F0bXkiLCAiZmllbGQiOiAiaWQiLCAiZXhwZWN0ZWQiOiAiZl9xb3F0bXkifQ=='

    def test_diversity_8(self):
        return 'eyJ0X2lkIjogInRfdHptZGZicyIsICJ0X3RpdGxlIjogImFydWVhIGZpdXN6ayIsICJmaW5hbF9pZCI6ICJmX2x5d3dzcSIsICJmaWVsZCI6ICJpZCIsICJleHBlY3RlZCI6ICJmX2x5d3dzcSJ9'

    def test_diversity_9(self):
        return 'eyJ0X2lkIjogInRfb3FxdWpzdWEiLCAidF90aXRsZSI6ICJvb3lzaHhwaSBmYWthdmFrIiwgImZpbmFsX2lkIjogImZfYW5mbXdtbXoiLCAiZmllbGQiOiAiaWQiLCAiZXhwZWN0ZWQiOiAiZl9hbmZtd21teiJ9'

    def test_diversity_10(self):
        return 'eyJ0X2lkIjogInRfeXZzcGIiLCAidF90aXRsZSI6ICJzYXptIGF2engiLCAiZmluYWxfaWQiOiAiZl91aXlhZXdlciIsICJmaWVsZCI6ICJpZCIsICJleHBlY3RlZCI6ICJmX3VpeWFld2VyIn0='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJ0X2lkIjogInRfeG9yZnZ1biIsICJ0X3RpdGxlIjogImdsY3Z0cnZ0IGh2bmMiLCAiZmluYWxfaWQiOiAiZl91Z2x0IiwgImZpZWxkIjogInRpdGxlIiwgImV4cGVjdGVkIjogImdsY3Z0cnZ0IGh2bmMifQ=='

    def test_diversity_2(self):
        return 'eyJ0X2lkIjogInRfcXRmcnp4YmgiLCAidF90aXRsZSI6ICJkZmRhamx3IHh4cHFvbG0iLCAiZmluYWxfaWQiOiAiZl9wdWhhbHFteiIsICJmaWVsZCI6ICJ0aXRsZSIsICJleHBlY3RlZCI6ICJkZmRhamx3IHh4cHFvbG0ifQ=='

    def test_diversity_3(self):
        return 'eyJ0X2lkIjogInRfbnhrYndsIiwgInRfdGl0bGUiOiAib2ptaG9pIGlpcm8iLCAiZmluYWxfaWQiOiAiZl9ucGFnIiwgImZpZWxkIjogInRpdGxlIiwgImV4cGVjdGVkIjogIm9qbWhvaSBpaXJvIn0='

    def test_diversity_4(self):
        return 'eyJ0X2lkIjogInRfenB2eiIsICJ0X3RpdGxlIjogInJrcHZqZSB6ZHNpIiwgImZpbmFsX2lkIjogImZfZ3RjYWlmeSIsICJmaWVsZCI6ICJ0aXRsZSIsICJleHBlY3RlZCI6ICJya3B2amUgemRzaSJ9'

    def test_diversity_5(self):
        return 'eyJ0X2lkIjogInRfa2NkcnhvIiwgInRfdGl0bGUiOiAib3FkcCBmamtvIiwgImZpbmFsX2lkIjogImZfZnhva3llIiwgImZpZWxkIjogInRpdGxlIiwgImV4cGVjdGVkIjogIm9xZHAgZmprbyJ9'

    def test_diversity_6(self):
        return 'eyJ0X2lkIjogInRfcnV1eWhpa3oiLCAidF90aXRsZSI6ICJpamZ1ZXFxciB1aGxzeSIsICJmaW5hbF9pZCI6ICJmX2lvZWpsIiwgImZpZWxkIjogInRpdGxlIiwgImV4cGVjdGVkIjogImlqZnVlcXFyIHVobHN5In0='

    def test_diversity_7(self):
        return 'eyJ0X2lkIjogInRfbGpiY3ZkdSIsICJ0X3RpdGxlIjogInJncWUgZ2FtbyIsICJmaW5hbF9pZCI6ICJmX3pocXhod3UiLCAiZmllbGQiOiAidGl0bGUiLCAiZXhwZWN0ZWQiOiAicmdxZSBnYW1vIn0='

    def test_diversity_8(self):
        return 'eyJ0X2lkIjogInRfdGpsdG5hdSIsICJ0X3RpdGxlIjogImx6Zm93and3IG5xeW5yYSIsICJmaW5hbF9pZCI6ICJmX29oenB1dCIsICJmaWVsZCI6ICJ0aXRsZSIsICJleHBlY3RlZCI6ICJsemZvd2p3dyBucXlucmEifQ=='

    def test_diversity_9(self):
        return 'eyJ0X2lkIjogInRfbGJlbmMiLCAidF90aXRsZSI6ICJ4c3pwcyBqYWtpZXNsbCIsICJmaW5hbF9pZCI6ICJmX21vYm0iLCAiZmllbGQiOiAidGl0bGUiLCAiZXhwZWN0ZWQiOiAieHN6cHMgamFraWVzbGwifQ=='

    def test_diversity_10(self):
        return 'eyJ0X2lkIjogInRfa256diIsICJ0X3RpdGxlIjogImVmdnEgaG9mcGhtIiwgImZpbmFsX2lkIjogImZfbXRpcnNmIiwgImZpZWxkIjogInRpdGxlIiwgImV4cGVjdGVkIjogImVmdnEgaG9mcGhtIn0='
