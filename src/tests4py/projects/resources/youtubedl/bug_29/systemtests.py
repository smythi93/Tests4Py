from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogImJ5eXEgc2RrYnpicm5tIiwgImV4cGVjdGVkIjogbnVsbH0='

    def test_diversity_2(self):
        return 'eyJkYXRlIjogInN3bnhoIiwgImV4cGVjdGVkIjogbnVsbH0='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogInFjcWggY2p3aHJneHIiLCAiZXhwZWN0ZWQiOiBudWxsfQ=='

    def test_diversity_4(self):
        return 'eyJkYXRlIjogImtzcmYiLCAiZXhwZWN0ZWQiOiBudWxsfQ=='

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIm5jZ2JrZHBzIiwgImV4cGVjdGVkIjogbnVsbH0='

    def test_diversity_6(self):
        return 'eyJkYXRlIjogImxyYmggemZ3YmxrIiwgImV4cGVjdGVkIjogbnVsbH0='

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIndtdm13eG12IGpkZm1kcHciLCAiZXhwZWN0ZWQiOiBudWxsfQ=='

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIndycmtzd2Ygend6anZ0IiwgImV4cGVjdGVkIjogbnVsbH0='

    def test_diversity_9(self):
        return 'eyJkYXRlIjogImd4dmd3dnkiLCAiZXhwZWN0ZWQiOiBudWxsfQ=='

    def test_diversity_10(self):
        return 'eyJkYXRlIjogInljaGNsZyBneG1ndnlnIiwgImV4cGVjdGVkIjogbnVsbH0='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogIkp1bHkgNiwgMjAxNCIsICJleHBlY3RlZCI6ICIyMDE0MDcwNiJ9'

    def test_diversity_2(self):
        return 'eyJkYXRlIjogIkFwcmlsIDEwLCAyMDA3IiwgImV4cGVjdGVkIjogIjIwMDcwNDEwIn0='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogIkp1bmUgMTgsIDE5NzMiLCAiZXhwZWN0ZWQiOiAiMTk3MzA2MTgifQ=='

    def test_diversity_4(self):
        return 'eyJkYXRlIjogIkF1Z3VzdCAyNSwgMTk3OSIsICJleHBlY3RlZCI6ICIxOTc5MDgyNSJ9'

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIkF1Z3VzdCAxMSwgMjAwNSIsICJleHBlY3RlZCI6ICIyMDA1MDgxMSJ9'

    def test_diversity_6(self):
        return 'eyJkYXRlIjogIk1hcmNoIDIsIDE5NzgiLCAiZXhwZWN0ZWQiOiAiMTk3ODAzMDIifQ=='

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIk1hcmNoIDUsIDIwMDkiLCAiZXhwZWN0ZWQiOiAiMjAwOTAzMDUifQ=='

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIkZlYnJ1YXJ5IDIzLCAyMDA0IiwgImV4cGVjdGVkIjogIjIwMDQwMjIzIn0='

    def test_diversity_9(self):
        return 'eyJkYXRlIjogIk1hcmNoIDEsIDE5OTAiLCAiZXhwZWN0ZWQiOiAiMTk5MDAzMDEifQ=='

    def test_diversity_10(self):
        return 'eyJkYXRlIjogIk5vdmVtYmVyIDIsIDIwMTIiLCAiZXhwZWN0ZWQiOiAiMjAxMjExMDIifQ=='
