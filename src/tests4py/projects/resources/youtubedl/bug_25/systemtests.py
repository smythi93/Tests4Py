from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcIndpdVwiOiBcIjAxOjM0OjQ4XCJ9IiwgImV4cGVjdGVkIjogeyJ3aXUiOiAiMDE6MzQ6NDgifX0='

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcIm1kYlwiOiBcIjA1OjUwOjA2XCJ9IiwgImV4cGVjdGVkIjogeyJtZGIiOiAiMDU6NTA6MDYifX0='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcInNxeWNlXCI6IFwiMDY6MTU6MzBcIn0iLCAiZXhwZWN0ZWQiOiB7InNxeWNlIjogIjA2OjE1OjMwIn19'

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcImFsem56YXJcIjogXCIwNDo0MTozOFwifSIsICJleHBlY3RlZCI6IHsiYWx6bnphciI6ICIwNDo0MTozOCJ9fQ=='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImh6YnJqcVwiOiBcIjA0OjM3OjMxXCJ9IiwgImV4cGVjdGVkIjogeyJoemJyanEiOiAiMDQ6Mzc6MzEifX0='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcInZxdWJva2VcIjogXCIwMzo0MjoxN1wifSIsICJleHBlY3RlZCI6IHsidnF1Ym9rZSI6ICIwMzo0MjoxNyJ9fQ=='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInh0Y3F1XCI6IFwiMDM6MTk6NDVcIn0iLCAiZXhwZWN0ZWQiOiB7Inh0Y3F1IjogIjAzOjE5OjQ1In19'

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcIm9yZ2RcIjogXCIwMzo1NTozN1wifSIsICJleHBlY3RlZCI6IHsib3JnZCI6ICIwMzo1NTozNyJ9fQ=='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcImJkY2VcIjogXCIwNDoxNzowM1wifSIsICJleHBlY3RlZCI6IHsiYmRjZSI6ICIwNDoxNzowMyJ9fQ=='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcInRla2pcIjogXCIwMDowMzozMFwifSIsICJleHBlY3RlZCI6IHsidGVraiI6ICIwMDowMzozMCJ9fQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcInlzdVwiOiBcIm5ia2NcIn0iLCAiZXhwZWN0ZWQiOiB7InlzdSI6ICJuYmtjIn19'

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcIm5jdHp4clwiOiA5NTU4OH0iLCAiZXhwZWN0ZWQiOiB7Im5jdHp4ciI6IDk1NTg4fX0='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcIndodHN2Y1wiOiBcInFtdW5uYVwifSIsICJleHBlY3RlZCI6IHsid2h0c3ZjIjogInFtdW5uYSJ9fQ=='

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcIml2Y3VmZG9cIjogODk2NX0iLCAiZXhwZWN0ZWQiOiB7Iml2Y3VmZG8iOiA4OTY1fX0='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImd3eGZxXCI6IFwiY3ZlXCJ9IiwgImV4cGVjdGVkIjogeyJnd3hmcSI6ICJjdmUifX0='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcIm96ZFwiOiBcInNyb1wifSIsICJleHBlY3RlZCI6IHsib3pkIjogInNybyJ9fQ=='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcImtueGpcIjogXCJvcWhiblwifSIsICJleHBlY3RlZCI6IHsia254aiI6ICJvcWhibiJ9fQ=='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInpqbndwdlwiOiBcInZ1emZqdm1cIn0iLCAiZXhwZWN0ZWQiOiB7InpqbndwdiI6ICJ2dXpmanZtIn19'

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcIm1naHZoXCI6IDYzNTk3fSIsICJleHBlY3RlZCI6IHsibWdodmgiOiA2MzU5N319'

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcIml1cHVcIjogXCJ3dG93XCJ9IiwgImV4cGVjdGVkIjogeyJpdXB1IjogInd0b3cifX0='
