from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJmb3JtYXQiOiAid29yc3QvYmVzdCxiZXN0IiwgImZtdHMiOiBbWyJ1anh5bnQiLCAyODM4XSwgWyJoeHRuayIsIDE1OTddXSwgImV4cGVjdGVkIjogWyJ1anh5bnQiLCAiaHh0bmsiXX0='

    def test_diversity_2(self):
        return 'eyJmb3JtYXQiOiAiYmVzdC9iZXN0LHdvcnN0IiwgImZtdHMiOiBbWyJ3eGNmYWsiLCAxMDA1XSwgWyJzZm5naGgiLCAyNjgzXSwgWyJwdmlmbmYiLCAxMTU4XSwgWyJ3YXkiLCAxMjA1XV0sICJleHBlY3RlZCI6IFsid2F5IiwgInd4Y2ZhayJdfQ=='

    def test_diversity_3(self):
        return 'eyJmb3JtYXQiOiAiYmVzdC93b3JzdCx3b3JzdCIsICJmbXRzIjogW1sienB0ZnJtIiwgMzE0XSwgWyJxcGtvdHYiLCA4M10sIFsidmJreHIiLCAyOTMyXSwgWyJhd3FiIiwgMjYxMF1dLCAiZXhwZWN0ZWQiOiBbImF3cWIiLCAienB0ZnJtIl19'

    def test_diversity_4(self):
        return 'eyJmb3JtYXQiOiAid29yc3QvYmVzdCxiZXN0IiwgImZtdHMiOiBbWyJjeHkiLCAxMzg0XSwgWyJ5cmp5bSIsIDE3NjldLCBbImRjanNyIiwgMTA4NV1dLCAiZXhwZWN0ZWQiOiBbImN4eSIsICJkY2pzciJdfQ=='

    def test_diversity_5(self):
        return 'eyJmb3JtYXQiOiAiYmVzdC93b3JzdCx3b3JzdCIsICJmbXRzIjogW1siZmZ3YiIsIDI5OF0sIFsieHlsIiwgNzE4XV0sICJleHBlY3RlZCI6IFsieHlsIiwgImZmd2IiXX0='

    def test_diversity_6(self):
        return 'eyJmb3JtYXQiOiAid29yc3Qvd29yc3QsYmVzdCIsICJmbXRzIjogW1sieGdrZmRoIiwgODczXSwgWyJyeWhtIiwgMTUyMF0sIFsiZW91dCIsIDE0MTBdXSwgImV4cGVjdGVkIjogWyJ4Z2tmZGgiLCAiZW91dCJdfQ=='

    def test_diversity_7(self):
        return 'eyJmb3JtYXQiOiAid29yc3Qvd29yc3QsYmVzdCIsICJmbXRzIjogW1siaHJvIiwgOTk1XSwgWyJicXYiLCAyNDUzXV0sICJleHBlY3RlZCI6IFsiaHJvIiwgImJxdiJdfQ=='

    def test_diversity_8(self):
        return 'eyJmb3JtYXQiOiAid29yc3Qvd29yc3QsYmVzdCIsICJmbXRzIjogW1sieGxrIiwgMTYzNV0sIFsibHhkZWZvIiwgMjE4MV0sIFsiZXVsY2QiLCAxMTEwXV0sICJleHBlY3RlZCI6IFsieGxrIiwgImV1bGNkIl19'

    def test_diversity_9(self):
        return 'eyJmb3JtYXQiOiAid29yc3Qvd29yc3QsYmVzdCIsICJmbXRzIjogW1sibmJtbyIsIDEwMzFdLCBbIm51dyIsIDI3OTddLCBbImtic2wiLCAxNTU0XV0sICJleHBlY3RlZCI6IFsibmJtbyIsICJrYnNsIl19'

    def test_diversity_10(self):
        return 'eyJmb3JtYXQiOiAid29yc3QvYmVzdCxiZXN0IiwgImZtdHMiOiBbWyJrdnMiLCAxMzE4XSwgWyJkZm5vIiwgMTkyNF0sIFsiYmRudCIsIDk4MF1dLCAiZXhwZWN0ZWQiOiBbImt2cyIsICJiZG50Il19'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCx3b3JzdCIsICJmbXRzIjogW1siZHRybyIsIDE3MzddLCBbImV5emt2IiwgMTg0Nl1dLCAiZXhwZWN0ZWQiOiBbImV5emt2IiwgImR0cm8iXX0='

    def test_diversity_2(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCx3b3JzdCIsICJmbXRzIjogW1sibmp4bGQiLCA5MTBdLCBbIm95a3NrZiIsIDIxNjldLCBbImR3a3UiLCA1NzJdLCBbImJoYiIsIDI1NDhdXSwgImV4cGVjdGVkIjogWyJiaGIiLCAibmp4bGQiXX0='

    def test_diversity_3(self):
        return 'eyJmb3JtYXQiOiAiYmVzdC93b3JzdCIsICJmbXRzIjogW1sicXpza2FhIiwgMjgxMl0sIFsiemxmcGtzIiwgMjQwOF1dLCAiZXhwZWN0ZWQiOiBbInpsZnBrcyJdfQ=='

    def test_diversity_4(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCx3b3JzdCIsICJmbXRzIjogW1siZmd6Z2ciLCAyMDIyXSwgWyJlaXlxbWoiLCAyNzY3XSwgWyJsaXYiLCAzMzldLCBbInR4Y3ZucSIsIDU4M11dLCAiZXhwZWN0ZWQiOiBbInR4Y3ZucSIsICJmZ3pnZyJdfQ=='

    def test_diversity_5(self):
        return 'eyJmb3JtYXQiOiAid29yc3QsYmVzdCIsICJmbXRzIjogW1sicWdwciIsIDE2NzBdLCBbImR5emwiLCAyMTgxXSwgWyJkZWYiLCAxMzczXSwgWyJ2bW51cHAiLCAxODQzXV0sICJleHBlY3RlZCI6IFsicWdwciIsICJ2bW51cHAiXX0='

    def test_diversity_6(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCx3b3JzdCIsICJmbXRzIjogW1sidmVlbWUiLCAxMDk0XSwgWyJ1eG14ayIsIDIwMTddXSwgImV4cGVjdGVkIjogWyJ1eG14ayIsICJ2ZWVtZSJdfQ=='

    def test_diversity_7(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCx3b3JzdCIsICJmbXRzIjogW1sic2p0eSIsIDE2NDVdLCBbImZwb2ZzdiIsIDE2MzFdXSwgImV4cGVjdGVkIjogWyJmcG9mc3YiLCAic2p0eSJdfQ=='

    def test_diversity_8(self):
        return 'eyJmb3JtYXQiOiAid29yc3QsYmVzdCIsICJmbXRzIjogW1siend3YyIsIDYwOF0sIFsic25mIiwgMjk4NV1dLCAiZXhwZWN0ZWQiOiBbInp3d2MiLCAic25mIl19'

    def test_diversity_9(self):
        return 'eyJmb3JtYXQiOiAid29yc3QsYmVzdCIsICJmbXRzIjogW1siYm55d2QiLCAxMjMyXSwgWyJ5aG1rIiwgMjUwNF0sIFsia2h2IiwgMjI0Nl0sIFsieWJvIiwgMTQyMl1dLCAiZXhwZWN0ZWQiOiBbImJueXdkIiwgInlibyJdfQ=='

    def test_diversity_10(self):
        return 'eyJmb3JtYXQiOiAiYmVzdC93b3JzdCIsICJmbXRzIjogW1sibWN6dnMiLCAxMzAxXSwgWyJ2cnpyIiwgMjA3Ml0sIFsib3VndiIsIDIyNjFdXSwgImV4cGVjdGVkIjogWyJvdWd2Il19'
