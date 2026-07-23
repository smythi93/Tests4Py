from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogIjIwMTktMDgtMDQiLCAiZXhwZWN0ZWQiOiAiMjAxOTA4MDQifQ=='

    def test_diversity_2(self):
        return 'eyJkYXRlIjogIjE5NzAtMDItMjYiLCAiZXhwZWN0ZWQiOiAiMTk3MDAyMjYifQ=='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogIjIwMDctMDEtMjIiLCAiZXhwZWN0ZWQiOiAiMjAwNzAxMjIifQ=='

    def test_diversity_4(self):
        return 'eyJkYXRlIjogIjIwMTQtMDItMDQiLCAiZXhwZWN0ZWQiOiAiMjAxNDAyMDQifQ=='

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIjIwMTktMDYtMDgiLCAiZXhwZWN0ZWQiOiAiMjAxOTA2MDgifQ=='

    def test_diversity_6(self):
        return 'eyJkYXRlIjogIjE5NzEtMDEtMjYiLCAiZXhwZWN0ZWQiOiAiMTk3MTAxMjYifQ=='

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIjE5NzEtMDYtMjEiLCAiZXhwZWN0ZWQiOiAiMTk3MTA2MjEifQ=='

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIjIwMDktMDgtMjAiLCAiZXhwZWN0ZWQiOiAiMjAwOTA4MjAifQ=='

    def test_diversity_9(self):
        return 'eyJkYXRlIjogIjE5OTktMDMtMDMiLCAiZXhwZWN0ZWQiOiAiMTk5OTAzMDMifQ=='

    def test_diversity_10(self):
        return 'eyJkYXRlIjogIjE5ODEtMTItMDQiLCAiZXhwZWN0ZWQiOiAiMTk4MTEyMDQifQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogIjE2IFNlcHRlbWJlciAxOTcwIiwgImV4cGVjdGVkIjogIjE5NzAwOTE2In0='

    def test_diversity_2(self):
        return 'eyJkYXRlIjogIjIyIEZlYnJ1YXJ5IDE5ODUiLCAiZXhwZWN0ZWQiOiAiMTk4NTAyMjIifQ=='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogIjIwIEZlYnJ1YXJ5IDE5OTkiLCAiZXhwZWN0ZWQiOiAiMTk5OTAyMjAifQ=='

    def test_diversity_4(self):
        return 'eyJkYXRlIjogIk9jdG9iZXIgMiwgMjAwMiIsICJleHBlY3RlZCI6ICIyMDAyMTAwMiJ9'

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIkZlYnJ1YXJ5IDIxLCAyMDA1IiwgImV4cGVjdGVkIjogIjIwMDUwMjIxIn0='

    def test_diversity_6(self):
        return 'eyJkYXRlIjogIjggTWF5IDE5OTIiLCAiZXhwZWN0ZWQiOiAiMTk5MjA1MDgifQ=='

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIjE3IEF1Z3VzdCAxOTgyIiwgImV4cGVjdGVkIjogIjE5ODIwODE3In0='

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIkZlYnJ1YXJ5IDEsIDIwMDIiLCAiZXhwZWN0ZWQiOiAiMjAwMjAyMDEifQ=='

    def test_diversity_9(self):
        return 'eyJkYXRlIjogIkF1Z3VzdCAyMiwgMjAxNSIsICJleHBlY3RlZCI6ICIyMDE1MDgyMiJ9'

    def test_diversity_10(self):
        return 'eyJkYXRlIjogIkZlYnJ1YXJ5IDE5LCAxOTczIiwgImV4cGVjdGVkIjogIjE5NzMwMjE5In0='
