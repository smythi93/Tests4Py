from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eHZ5bmYgPSB4Z2woCiAgICB4dCwgICMgdHlwZTogaW50CiAgICB2eXdnLCAgIyB0eXBlOiBzdHIKICAgIGJjZ2wsICAjIHR5cGU6IGludAopICAjIHR5cGU6IGJ5dGVzCg=='

    def test_diversity_2(self):
        return 'cmFnYiA9IGN4KAogICAgeWdtLCAgIyB0eXBlOiBib29sCiAgICBpZ3UsICAjIHR5cGU6IGZsb2F0CikgICMgdHlwZTogYm9vbAo='

    def test_diversity_3(self):
        return 'amVpZyA9ICgKICAgIGhxLCAgIyB0eXBlOiBzdHIKICAgIHlwcXFrLCAgIyB0eXBlOiBpbnQKKSAgIyB0eXBlOiBUdXBsZVtzdHIsIGludF0K'

    def test_diversity_4(self):
        return 'cG4gPSAoCiAgICBlb2x1LCAgIyB0eXBlOiBzdHIKICAgIGt1eCwgICMgdHlwZTogYnl0ZXMKKSAgIyB0eXBlOiBUdXBsZVtzdHIsIGJ5dGVzXQo='

    def test_diversity_5(self):
        return 'aXN5b2sgPSAoCiAgICBxdXVzdywgICMgdHlwZTogZmxvYXQKICAgIHZ3bWdwLCAgIyB0eXBlOiBzdHIKKSAgIyB0eXBlOiBUdXBsZVtmbG9hdCwgc3RyXQo='

    def test_diversity_6(self):
        return 'dGggPSAoCiAgICBhdSwgICMgdHlwZTogaW50CiAgICBzdywgICMgdHlwZTogaW50CikgICMgdHlwZTogVHVwbGVbaW50LCBpbnRdCg=='

    def test_diversity_7(self):
        return 'b2wgPSBtZnMoCiAgICBiYywgICMgdHlwZTogc3RyCiAgICBzZmdoLCAgIyB0eXBlOiBieXRlcwogICAgc3osICAjIHR5cGU6IHN0cgopICAjIHR5cGU6IGJ5dGVzCg=='

    def test_diversity_8(self):
        return 'cHpnID0gWwogICAgdWtrYiwgICMgdHlwZTogYm9vbAogICAgbnF0ZHUsICAjIHR5cGU6IGJvb2wKXSAgIyB0eXBlOiBMaXN0W2Zsb2F0XQo='

    def test_diversity_9(self):
        return 'bHIgPSB6cnN3YSgKICAgIHNmZSwgICMgdHlwZTogZmxvYXQKICAgIGp0LCAgIyB0eXBlOiBieXRlcwopICAjIHR5cGU6IGZsb2F0Cg=='

    def test_diversity_10(self):
        return 'ZmUgPSBbCiAgICBicW0sICAjIHR5cGU6IGludAogICAgcnF3dGEsICAjIHR5cGU6IGZsb2F0Cl0gICMgdHlwZTogTGlzdFtieXRlc10K'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'cGpuID0gW10gICMgdHlwZTogTGlzdFtieXRlc10K'

    def test_diversity_2(self):
        return 'ZGVmIGR0KGRyeHMpOgogICAgbXV2ID0gY29tcHV0ZSgpICAjIHR5cGU6IHN0cgogICAgcmV0dXJuIG11dgo='

    def test_diversity_3(self):
        return 'a2plenkgPSAxMwo='

    def test_diversity_4(self):
        return 'YnkgPSBbXSAgIyB0eXBlOiBMaXN0W2ludF0K'

    def test_diversity_5(self):
        return 'ZGVmIHZhbWgoZ3J0bCk6CiAgICBiaiA9IGNvbXB1dGUoKSAgIyB0eXBlOiBpbnQKICAgIHJldHVybiBiago='

    def test_diversity_6(self):
        return 'ZGVmIGRlKHNsaSk6CiAgICBleiA9IGNvbXB1dGUoKSAgIyB0eXBlOiBzdHIKICAgIHJldHVybiBlego='

    def test_diversity_7(self):
        return 'ZWlnID0gW10gICMgdHlwZTogTGlzdFtpbnRdCg=='

    def test_diversity_8(self):
        return 'c2VrcCA9IFtdICAjIHR5cGU6IExpc3RbYnl0ZXNdCg=='

    def test_diversity_9(self):
        return 'Y2cgPSA1MQo='

    def test_diversity_10(self):
        return 'dXJ2ID0gMjYK'
