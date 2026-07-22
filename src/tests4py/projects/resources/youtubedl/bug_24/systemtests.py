from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJmaWx0ZXIiOiAiY29ueWhuIT0zMDE0MyIsICJkY3QiOiB7ImNvbnlobiI6ICIzMDE0MyJ9LCAiZXhwZWN0ZWQiOiBmYWxzZX0='

    def test_diversity_2(self):
        return 'eyJmaWx0ZXIiOiAienZpaGp4ej00NDYyMCIsICJkY3QiOiB7Inp2aWhqeHoiOiAiNDQ2MjAifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_3(self):
        return 'eyJmaWx0ZXIiOiAicnlrdnFweT01MzU3MyIsICJkY3QiOiB7InJ5a3ZxcHkiOiAiNTM1NzMifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_4(self):
        return 'eyJmaWx0ZXIiOiAicHVmbj01NDk2IiwgImRjdCI6IHsicHVmbiI6ICI1NDk2In0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_5(self):
        return 'eyJmaWx0ZXIiOiAicWxwdiE9MTIwMjkiLCAiZGN0IjogeyJxbHB2IjogIjEyMDI5In0sICJleHBlY3RlZCI6IGZhbHNlfQ=='

    def test_diversity_6(self):
        return 'eyJmaWx0ZXIiOiAidmJhYmJhIT0zMjMwNCIsICJkY3QiOiB7InZiYWJiYSI6ICIzMjMwNCJ9LCAiZXhwZWN0ZWQiOiBmYWxzZX0='

    def test_diversity_7(self):
        return 'eyJmaWx0ZXIiOiAiZmN4YWJlPTY3NzUyIiwgImRjdCI6IHsiZmN4YWJlIjogIjY3NzUyIn0sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_8(self):
        return 'eyJmaWx0ZXIiOiAiZnRmIT00NjYyOCIsICJkY3QiOiB7ImZ0ZiI6ICI0NjYyOCJ9LCAiZXhwZWN0ZWQiOiBmYWxzZX0='

    def test_diversity_9(self):
        return 'eyJmaWx0ZXIiOiAiYm5nIT0xOTA4OSIsICJkY3QiOiB7ImJuZyI6ICIxOTA4OSJ9LCAiZXhwZWN0ZWQiOiBmYWxzZX0='

    def test_diversity_10(self):
        return 'eyJmaWx0ZXIiOiAiaXJ1YWg9MjY3NjgiLCAiZGN0IjogeyJpcnVhaCI6ICIyNjc2OCJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJmaWx0ZXIiOiAibHJjPWdocWFvaHQiLCAiZGN0IjogeyJscmMiOiAiZ2hxYW9odCJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_2(self):
        return 'eyJmaWx0ZXIiOiAieGNrdXB3PTgxMTcwIiwgImRjdCI6IHsieGNrdXB3IjogODExNzB9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_3(self):
        return 'eyJmaWx0ZXIiOiAid2R4anpmcWc9c252biIsICJkY3QiOiB7IndkeGp6ZnFnIjogInNudm4ifSwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_4(self):
        return 'eyJmaWx0ZXIiOiAibWtuYm91PTYxIiwgImRjdCI6IHsibWtuYm91IjogIjczIn0sICJleHBlY3RlZCI6IGZhbHNlfQ=='

    def test_diversity_5(self):
        return 'eyJmaWx0ZXIiOiAiaXlkdD05NzA0IiwgImRjdCI6IHsiaXlkdCI6IDk3MDR9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_6(self):
        return 'eyJmaWx0ZXIiOiAiZmdsdXNkcHE9NDA3IiwgImRjdCI6IHsiZmdsdXNkcHEiOiAiNTcyIn0sICJleHBlY3RlZCI6IGZhbHNlfQ=='

    def test_diversity_7(self):
        return 'eyJmaWx0ZXIiOiAicXJzdG91eHc9eG9qZGgiLCAiZGN0IjogeyJxcnN0b3V4dyI6ICJ4b2pkaCJ9LCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_8(self):
        return 'eyJmaWx0ZXIiOiAiZ2Zqb2dsZj0xMDg3MyIsICJkY3QiOiB7Imdmam9nbGYiOiAxMDg3M30sICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_9(self):
        return 'eyJmaWx0ZXIiOiAidHJndD0zODIiLCAiZGN0IjogeyJ0cmd0IjogIjY5MiJ9LCAiZXhwZWN0ZWQiOiBmYWxzZX0='

    def test_diversity_10(self):
        return 'eyJmaWx0ZXIiOiAiZ29vamRsPTMyMiIsICJkY3QiOiB7Imdvb2pkbCI6ICI1NjEifSwgImV4cGVjdGVkIjogZmFsc2V9'
