from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJmb3JtYXQiOiAid29yc3Rbd2lkdGg-MjYzNV0iLCAiZm10cyI6IFtbInBsc2dyIiwgMTIwN10sIFsidnZwemFyIiwgMTYzNV0sIFsidm9jcm55IiwgNzAwXSwgWyJ6cHUiLCAxNDYxXSwgWyJvdnZvZm0iLCA2NTldXSwgImV4cGVjdGVkIjogW119'

    def test_diversity_2(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD4yNjg4XSIsICJmbXRzIjogW1siY3hleXYiLCAxNzNdLCBbIm1heiIsIDE2ODhdLCBbImhndmIiLCAxMjM0XV0sICJleHBlY3RlZCI6IFtdfQ=='

    def test_diversity_3(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD4yMjkxXSIsICJmbXRzIjogW1siamxnIiwgMjg0XSwgWyJoanpkemsiLCA0NjJdLCBbInZpa3dlIiwgMTI5MV1dLCAiZXhwZWN0ZWQiOiBbXX0='

    def test_diversity_4(self):
        return 'eyJmb3JtYXQiOiAid29yc3Rbd2lkdGg-MjQ5MV0iLCAiZm10cyI6IFtbImV6bXZkIiwgMTQ5MV0sIFsibHpmIiwgMjA5XSwgWyJ4dnMiLCA1MjRdXSwgImV4cGVjdGVkIjogW119'

    def test_diversity_5(self):
        return 'eyJmb3JtYXQiOiAid29yc3Rbd2lkdGg-MjUwNV0iLCAiZm10cyI6IFtbIm94YmMiLCA3MjNdLCBbImhxeWwiLCAxNDc0XSwgWyJ4c21leCIsIDE1MDVdXSwgImV4cGVjdGVkIjogW119'

    def test_diversity_6(self):
        return 'eyJmb3JtYXQiOiAid29yc3Rbd2lkdGg-MTk3Nl0iLCAiZm10cyI6IFtbInVjZCIsIDQ4Nl0sIFsibGZ4ZCIsIDc3M10sIFsic25memsiLCA1NzRdLCBbInFlemV5IiwgOTc2XV0sICJleHBlY3RlZCI6IFtdfQ=='

    def test_diversity_7(self):
        return 'eyJmb3JtYXQiOiAid29yc3Rbd2lkdGg-MTcxMV0iLCAiZm10cyI6IFtbImZudSIsIDY1N10sIFsicXJ6ZyIsIDcxMV0sIFsibnl5amEiLCA1NDFdXSwgImV4cGVjdGVkIjogW119'

    def test_diversity_8(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD4yOTE0XSIsICJmbXRzIjogW1sibXJ5cWRoIiwgMTkxNF0sIFsidnN6cmkiLCA0MDBdLCBbImp6a2FycyIsIDEzMjhdLCBbInhlbmN3IiwgMTc0OF0sIFsicGZkIiwgMTg0Ml1dLCAiZXhwZWN0ZWQiOiBbXX0='

    def test_diversity_9(self):
        return 'eyJmb3JtYXQiOiAid29yc3Rbd2lkdGg-MjgyNl0iLCAiZm10cyI6IFtbImJ0ZW0iLCAyNDJdLCBbImhsd2NsYyIsIDE2NzJdLCBbIm53d3IiLCAzMzddLCBbImxnem1ybSIsIDE4MjZdXSwgImV4cGVjdGVkIjogW119'

    def test_diversity_10(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD4yNTM4XSIsICJmbXRzIjogW1sieHlyZXNoIiwgMTM2MF0sIFsiYmRkeHh4IiwgMTUzOF0sIFsienl5IiwgMTM1MF0sIFsibHZkIiwgMjk0XSwgWyJlam5iYyIsIDE1MDldXSwgImV4cGVjdGVkIjogW119'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD0xMTYyXSIsICJmbXRzIjogW1siZG9zbmoiLCAxMjg2XSwgWyJyYW9ocWoiLCA3MjhdLCBbImJwcG4iLCAxNTU3XSwgWyJ3Z2xtcyIsIDExNjJdXSwgImV4cGVjdGVkIjogWyJ3Z2xtcyJdfQ=='

    def test_diversity_2(self):
        return 'eyJmb3JtYXQiOiAiYWxsW3dpZHRoPj0yNjRdIiwgImZtdHMiOiBbWyJxdXFlaWsiLCAxOTcyXSwgWyJlenppcSIsIDExOTVdLCBbImRwenMiLCAyNjRdXSwgImV4cGVjdGVkIjogWyJxdXFlaWsiLCAiZXp6aXEiLCAiZHB6cyJdfQ=='

    def test_diversity_3(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD04MzhdIiwgImZtdHMiOiBbWyJwbnFnIiwgMTcwN10sIFsic293ZHYiLCAxMjYwXSwgWyJ0cnZvcmUiLCA4MzhdXSwgImV4cGVjdGVkIjogWyJ0cnZvcmUiXX0='

    def test_diversity_4(self):
        return 'eyJmb3JtYXQiOiAiYWxsW3dpZHRoPj00MTFdIiwgImZtdHMiOiBbWyJuc3dzIiwgNDExXSwgWyJ5Y2dxaSIsIDczN10sIFsiaXBmIiwgMTAyNV0sIFsic2xjYSIsIDEyNDFdLCBbImt1YmhmdiIsIDc1Ml1dLCAiZXhwZWN0ZWQiOiBbIm5zd3MiLCAieWNncWkiLCAiaXBmIiwgInNsY2EiLCAia3ViaGZ2Il19'

    def test_diversity_5(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD0zNDhdIiwgImZtdHMiOiBbWyJvbm5yemQiLCA1NjJdLCBbImZ1dmZhIiwgMTYyMl0sIFsib21jZSIsIDM3M10sIFsib2Z1ZmwiLCAzNDhdLCBbImx3YWJhIiwgNDg1XV0sICJleHBlY3RlZCI6IFsib2Z1ZmwiXX0='

    def test_diversity_6(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD0xOTc5XSIsICJmbXRzIjogW1sidmV0dCIsIDg1OF0sIFsid3VmZyIsIDE5NzldLCBbImVlaXYiLCAxMTM1XSwgWyJ1Zml1aiIsIDE4MjddXSwgImV4cGVjdGVkIjogWyJ3dWZnIl19'

    def test_diversity_7(self):
        return 'eyJmb3JtYXQiOiAiYWxsW3dpZHRoPj0zNThdIiwgImZtdHMiOiBbWyJpem5vciIsIDM1OF0sIFsiaXp1Ymd6IiwgMTQxMF0sIFsiZ3p3bXBxIiwgNzM4XSwgWyJkcGVlaSIsIDE4MzhdXSwgImV4cGVjdGVkIjogWyJpem5vciIsICJpenViZ3oiLCAiZ3p3bXBxIiwgImRwZWVpIl19'

    def test_diversity_8(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD0xNjAwXSIsICJmbXRzIjogW1sib3psIiwgMTAzNF0sIFsianN6eCIsIDE2MDBdLCBbIm1oZG1iciIsIDE5MzJdLCBbIm5scXoiLCAxNjUwXV0sICJleHBlY3RlZCI6IFsianN6eCJdfQ=='

    def test_diversity_9(self):
        return 'eyJmb3JtYXQiOiAiYWxsW3dpZHRoPj05NzJdIiwgImZtdHMiOiBbWyJzaGEiLCAxMzgyXSwgWyJueWdqdCIsIDk4MF0sIFsid2prIiwgOTcyXV0sICJleHBlY3RlZCI6IFsic2hhIiwgIm55Z2p0IiwgIndqayJdfQ=='

    def test_diversity_10(self):
        return 'eyJmb3JtYXQiOiAiYmVzdFt3aWR0aD0xNjcwXSIsICJmbXRzIjogW1sic3R4IiwgODczXSwgWyJqaGZ6aSIsIDEyNTJdLCBbInZicnhkZCIsIDE2NzBdLCBbInVzbiIsIDI3N10sIFsiZWh0bCIsIDE1NDRdXSwgImV4cGVjdGVkIjogWyJ2YnJ4ZGQiXX0='
