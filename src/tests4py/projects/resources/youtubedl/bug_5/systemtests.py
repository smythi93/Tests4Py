from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogIlN1biwgMDQgQXVnIDIwMjAgMDA6MDU6NTggKzAwMDAiLCAiZXhwZWN0ZWQiOiAxNTk2NDk5NTU4fQ=='

    def test_diversity_2(self):
        return 'eyJkYXRlIjogIlN1biwgMjIgSmFuIDIwMDggMjI6MDU6MDYgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxMjAxMDM5NTA2fQ=='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogIldlZCwgMDEgQXByIDE5OTMgMDA6NTA6MDEgKzAwMDAiLCAiZXhwZWN0ZWQiOiA3MzM2MjU0MDF9'

    def test_diversity_4(self):
        return 'eyJkYXRlIjogIk1vbiwgMTYgT2N0IDIwMTIgMTk6Mjk6MDkgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxMzUwNDE1NzQ5fQ=='

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIlR1ZSwgMDQgRGVjIDE5ODIgMDA6MzI6MzEgKzAwMDAiLCAiZXhwZWN0ZWQiOiA0MDc4MDk5NTF9'

    def test_diversity_6(self):
        return 'eyJkYXRlIjogIlNhdCwgMTggTm92IDE5NzUgMTQ6MDQ6MzggKzAwMDAiLCAiZXhwZWN0ZWQiOiAxODU1NTE0Nzh9'

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIkZyaSwgMTkgU2VwIDE5NzYgMDE6MTc6NTIgKzAwMDAiLCAiZXhwZWN0ZWQiOiAyMTE5NDM4NzJ9'

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIldlZCwgMTAgTm92IDE5NzUgMTU6NTQ6MjIgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxODQ4NjY4NjJ9'

    def test_diversity_9(self):
        return 'eyJkYXRlIjogIlNhdCwgMDcgTm92IDE5ODYgMTQ6NTY6MzMgKzAwMDAiLCAiZXhwZWN0ZWQiOiA1MzE3NTkzOTN9'

    def test_diversity_10(self):
        return 'eyJkYXRlIjogIlNhdCwgMDMgU2VwIDE5NzIgMDA6MjE6MDkgKzAwMDAiLCAiZXhwZWN0ZWQiOiA4NDMyNzY2OX0='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJkYXRlIjogIjIwMDEvMTEvMTMgMDU6MDM6MDQgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxMDA1NjI3Nzg0fQ=='

    def test_diversity_2(self):
        return 'eyJkYXRlIjogIjIwMDgvMDgvMDYgMDI6MzU6MTMgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxMjE3OTkwMTEzfQ=='

    def test_diversity_3(self):
        return 'eyJkYXRlIjogIjE5ODAvMDEvMTIgMDM6MzM6MDkgKzAwMDAiLCAiZXhwZWN0ZWQiOiAzMTY0OTU5ODl9'

    def test_diversity_4(self):
        return 'eyJkYXRlIjogIjIwMTMvMDUvMTUgMDE6MjY6MTcgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxMzY4NTgxMTc3fQ=='

    def test_diversity_5(self):
        return 'eyJkYXRlIjogIjIwMTMvMDEvMDYgMDg6MDk6MTkgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxMzU3NDU5NzU5fQ=='

    def test_diversity_6(self):
        return 'eyJkYXRlIjogIjIwMjUvMDMvMjUgMTQ6MDI6MzYgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxNzQyOTExMzU2fQ=='

    def test_diversity_7(self):
        return 'eyJkYXRlIjogIjE5OTUvMDYvMTYgMTA6Mzc6NTIgKzAwMDAiLCAiZXhwZWN0ZWQiOiA4MDMyOTkwNzJ9'

    def test_diversity_8(self):
        return 'eyJkYXRlIjogIjIwMDAvMDgvMDIgMTU6NTU6NTIgKzAwMDAiLCAiZXhwZWN0ZWQiOiA5NjUyMzE3NTJ9'

    def test_diversity_9(self):
        return 'eyJkYXRlIjogIjIwMDkvMDMvMTUgMjM6NDk6MzMgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxMjM3MTYwOTczfQ=='

    def test_diversity_10(self):
        return 'eyJkYXRlIjogIjIwMjMvMDgvMTAgMDg6MDc6NDkgKzAwMDAiLCAiZXhwZWN0ZWQiOiAxNjkxNjU0ODY5fQ=='
