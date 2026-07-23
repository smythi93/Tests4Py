from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogIjA0LzA4LzIwMTkgMDA6MDU6NTgiLCAiZXhwZWN0ZWQiOiAiMjAxOTA4MDQifQ=='

    def test_diversity_2(self):
        return 'eyJkYXRlIjogIjIyLzAxLzIwMDcgMjI6MDU6MDYiLCAiZXhwZWN0ZWQiOiAiMjAwNzAxMjIifQ=='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogIjA4LzA2LzIwMTkgMDA6MDE6NTAiLCAiZXhwZWN0ZWQiOiAiMjAxOTA2MDgifQ=='

    def test_diversity_4(self):
        return 'eyJkYXRlIjogIjIxLzA2LzE5NzEgMTk6MzA6MzkiLCAiZXhwZWN0ZWQiOiAiMTk3MTA2MjEifQ=='

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIjAzLzAzLzE5OTkgMDU6NDU6MDciLCAiZXhwZWN0ZWQiOiAiMTk5OTAzMDMifQ=='

    def test_diversity_6(self):
        return 'eyJkYXRlIjogIjE2LzA5LzE5NzAgMDc6MDQ6NDIiLCAiZXhwZWN0ZWQiOiAiMTk3MDA5MTYifQ=='

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIjAzLzA4LzIwMDQgMTk6NDM6MDUiLCAiZXhwZWN0ZWQiOiAiMjAwNDA4MDMifQ=='

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIjAyLzEwLzIwMDIgMDg6NTI6MzUiLCAiZXhwZWN0ZWQiOiAiMjAwMjEwMDIifQ=='

    def test_diversity_9(self):
        return 'eyJkYXRlIjogIjEwLzExLzE5NzQgMTU6NTQ6MjIiLCAiZXhwZWN0ZWQiOiAiMTk3NDExMTAifQ=='

    def test_diversity_10(self):
        return 'eyJkYXRlIjogIjIxLzA0LzE5ODcgMDY6Mjk6NTYiLCAiZXhwZWN0ZWQiOiAiMTk4NzA0MjEifQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogIk5vdmVtYmVyIDEsIDIwMDMiLCAiZXhwZWN0ZWQiOiAiMjAwMzExMDEifQ=='

    def test_diversity_2(self):
        return 'eyJkYXRlIjogIjE5NzQvMDEvMTEgMTU6NDI6MjQiLCAiZXhwZWN0ZWQiOiAiMTk3NDAxMTEifQ=='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogIkphbnVhcnkgMywgMTk4MCIsICJleHBlY3RlZCI6ICIxOTgwMDEwMyJ9'

    def test_diversity_4(self):
        return 'eyJkYXRlIjogIjE5ODAvMDIvMTggMDA6NTk6MjIiLCAiZXhwZWN0ZWQiOiAiMTk4MDAyMTgifQ=='

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIjIwMTkvMDIvMTcgMDk6Mjk6MDIiLCAiZXhwZWN0ZWQiOiAiMjAxOTAyMTcifQ=='

    def test_diversity_6(self):
        return 'eyJkYXRlIjogIk1heSAyMiwgMTk5NiIsICJleHBlY3RlZCI6ICIxOTk2MDUyMiJ9'

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIjE5ODEvMDUvMDUgMDQ6NDk6NTMiLCAiZXhwZWN0ZWQiOiAiMTk4MTA1MDUifQ=='

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIjE5OTkvMDEvMTkgMTE6MzE6MjEiLCAiZXhwZWN0ZWQiOiAiMTk5OTAxMTkifQ=='

    def test_diversity_9(self):
        return 'eyJkYXRlIjogIjIwMDcvMDgvMTYgMTU6NTU6NTIiLCAiZXhwZWN0ZWQiOiAiMjAwNzA4MTYifQ=='

    def test_diversity_10(self):
        return 'eyJkYXRlIjogIk1hcmNoIDE1LCAyMDA4IiwgImV4cGVjdGVkIjogIjIwMDgwMzE1In0='
