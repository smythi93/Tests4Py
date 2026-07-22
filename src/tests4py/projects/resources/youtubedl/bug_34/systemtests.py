from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogInsnZGN5dWFzJzp7J3RnYSc6J2lxcSd9fSIsICJleHBlY3RlZCI6IHsiZGN5dWFzIjogeyJ0Z2EiOiAiaXFxIn19fQ=='

    def test_diversity_2(self):
        return 'eyJjb2RlIjogInsnY3N2bic6eydib21wJzonbmJ2J319IiwgImV4cGVjdGVkIjogeyJjc3ZuIjogeyJib21wIjogIm5idiJ9fX0='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogInsncW1qJzp7J3Jmd3InOidiaXNyZWJtJ319IiwgImV4cGVjdGVkIjogeyJxbWoiOiB7InJmd3IiOiAiYmlzcmVibSJ9fX0='

    def test_diversity_4(self):
        return 'eyJjb2RlIjogInsneWRoJzp7J29keSc6J2tyYid9fSIsICJleHBlY3RlZCI6IHsieWRoIjogeyJvZHkiOiAia3JiIn19fQ=='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogInsnZXlldmInOnsndG1wbWJ5Jzond2x1dmhkZSd9fSIsICJleHBlY3RlZCI6IHsiZXlldmIiOiB7InRtcG1ieSI6ICJ3bHV2aGRlIn19fQ=='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogInsndHljdmp2Jzp7J3Fpc3ZlJzonend6aXUnfX0iLCAiZXhwZWN0ZWQiOiB7InR5Y3ZqdiI6IHsicWlzdmUiOiAiend6aXUifX19'

    def test_diversity_7(self):
        return 'eyJjb2RlIjogInsnZnZ1Jzp7J2NmeCc6J2hscHdyJ319IiwgImV4cGVjdGVkIjogeyJmdnUiOiB7ImNmeCI6ICJobHB3ciJ9fX0='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogInsnY2Z4bCc6eyd2anduJzonZXBodm5tJ319IiwgImV4cGVjdGVkIjogeyJjZnhsIjogeyJ2anduIjogImVwaHZubSJ9fX0='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogInsnYXJxdCc6eydtZGJlZG9zJzoneGJraSd9fSIsICJleHBlY3RlZCI6IHsiYXJxdCI6IHsibWRiZWRvcyI6ICJ4YmtpIn19fQ=='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogInsnd3ZjZ2t3aCc6eyd5eGhxaGknOidzaGgnfX0iLCAiZXhwZWN0ZWQiOiB7Ind2Y2drd2giOiB7Inl4aHFoaSI6ICJzaGgifX19'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogInsnbWh2JzonbHJydXNyYycsJ2J3bHVlaSc6J2JkeHB6dCcsJ2VxZXByaic6NDg5Mn0iLCAiZXhwZWN0ZWQiOiB7Im1odiI6ICJscnJ1c3JjIiwgImJ3bHVlaSI6ICJiZHhwenQiLCAiZXFlcHJqIjogNDg5Mn19'

    def test_diversity_2(self):
        return 'eyJjb2RlIjogInsnZm54bGNucCc6J3JiZicsJ2l5aGZ2aG4nOidubG5idCcsJ3ZnZCc6J3hmbnF2cid9IiwgImV4cGVjdGVkIjogeyJmbnhsY25wIjogInJiZiIsICJpeWhmdmhuIjogIm5sbmJ0IiwgInZnZCI6ICJ4Zm5xdnIifX0='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogInsnZHlnJzondHJrdmR6bycsJ2ZtcnJ6d3EnOjczMTJ9IiwgImV4cGVjdGVkIjogeyJkeWciOiAidHJrdmR6byIsICJmbXJyendxIjogNzMxMn19'

    def test_diversity_4(self):
        return 'eyJjb2RlIjogInsnYmp2a2InOjUxNDd9IiwgImV4cGVjdGVkIjogeyJianZrYiI6IDUxNDd9fQ=='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogInsndWp5cmptYic6J3ZsaSd9IiwgImV4cGVjdGVkIjogeyJ1anlyam1iIjogInZsaSJ9fQ=='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogInsna2JhdXYnOjg5NzEsJ3N1d2onOjgyMjJ9IiwgImV4cGVjdGVkIjogeyJrYmF1diI6IDg5NzEsICJzdXdqIjogODIyMn19'

    def test_diversity_7(self):
        return 'eyJjb2RlIjogInsncWJ4bXAnOidramh4cGcnfSIsICJleHBlY3RlZCI6IHsicWJ4bXAiOiAia2poeHBnIn19'

    def test_diversity_8(self):
        return 'eyJjb2RlIjogInsnc2dsdnNqdCc6NjcwNywnc3FseHcnOjk4MTAsJ2Fmb2plaHYnOjc4Njd9IiwgImV4cGVjdGVkIjogeyJzZ2x2c2p0IjogNjcwNywgInNxbHh3IjogOTgxMCwgImFmb2plaHYiOiA3ODY3fX0='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogInsnaXlzJzond3Bycm15eCcsJ2R1bW9kdWcnOidjZnBpanMnLCdzdWpjcncnOidlcnAnfSIsICJleHBlY3RlZCI6IHsiaXlzIjogIndwcnJteXgiLCAiZHVtb2R1ZyI6ICJjZnBpanMiLCAic3VqY3J3IjogImVycCJ9fQ=='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogInsndWdpJzoneXN4ZXphcCd9IiwgImV4cGVjdGVkIjogeyJ1Z2kiOiAieXN4ZXphcCJ9fQ=='
