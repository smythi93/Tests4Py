from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBuZXN0ZWRfc2NvcGVzIGFzIF9nZGx3Zgo='

    def test_diversity_2(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCB3aXRoX3N0YXRlbWVudCBhcyBfdXF5eXhmCg=='

    def test_diversity_3(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBnZW5lcmF0b3Jfc3RvcCBhcyBfb3R4dWhtZW0K'

    def test_diversity_4(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBkaXZpc2lvbiBhcyBfZXZxdXYK'

    def test_diversity_5(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBnZW5lcmF0b3Jfc3RvcCBhcyBfY2luaQo='

    def test_diversity_6(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCB1bmljb2RlX2xpdGVyYWxzIGFzIF9uZWxid2wK'

    def test_diversity_7(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbiBhcyBfa3BxaXZoaWkK'

    def test_diversity_8(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCB1bmljb2RlX2xpdGVyYWxzIGFzIF9xb29uZmRiCg=='

    def test_diversity_9(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBuZXN0ZWRfc2NvcGVzIGFzIF9wa3lhYnN1Cg=='

    def test_diversity_10(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhYnNvbHV0ZV9pbXBvcnQgYXMgX3V4YXdsanZ2Cg=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhYnNvbHV0ZV9pbXBvcnQK'

    def test_diversity_2(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbiwgZGl2aXNpb24K'

    def test_diversity_3(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCB1bmljb2RlX2xpdGVyYWxzCg=='

    def test_diversity_4(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbiwgbmVzdGVkX3Njb3Blcwo='

    def test_diversity_5(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBkaXZpc2lvbiwgdW5pY29kZV9saXRlcmFscwo='

    def test_diversity_6(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBkaXZpc2lvbgo='

    def test_diversity_7(self):
        return 'em1reHZmbHggPSA4Cg=='

    def test_diversity_8(self):
        return 'emxtYWZrdCA9IDQK'

    def test_diversity_9(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCB3aXRoX3N0YXRlbWVudCwgcHJpbnRfZnVuY3Rpb24K'

    def test_diversity_10(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbiwgZ2VuZXJhdG9yX3N0b3AK'
