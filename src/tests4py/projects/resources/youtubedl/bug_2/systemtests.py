from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJyZXBzIjogW1sidiIsICJjd2F0ZCIsIDEyNDkxNjJdLCBbInYiLCAidGdjdGYiLCA0NDA1OTMyXSwgWyJhIiwgInRnY3RmIiwgMTY0OTU5XV0sICJleHBlY3RlZCI6IFsiY3dhdGQiLCAidGdjdGYiLCAidGdjdGYiXX0='

    def test_diversity_2(self):
        return 'eyJyZXBzIjogW1sidiIsICJvbW9ud3giLCA0NDUyOTE1XSwgWyJ2IiwgInVoenh4bCIsIDU2NzIwMTNdLCBbImEiLCAib21vbnd4IiwgNzQzMzBdXSwgImV4cGVjdGVkIjogWyJvbW9ud3giLCAib21vbnd4IiwgInVoenh4bCJdfQ=='

    def test_diversity_3(self):
        return 'eyJyZXBzIjogW1sidiIsICJleWx2YiIsIDMyMTM0MjRdLCBbInYiLCAiemJsY3FhIiwgMzg1Mjg3Nl0sIFsiYSIsICJ6YmxjcWEiLCA3ODE0N11dLCAiZXhwZWN0ZWQiOiBbImV5bHZiIiwgInpibGNxYSIsICJ6YmxjcWEiXX0='

    def test_diversity_4(self):
        return 'eyJyZXBzIjogW1sidiIsICJ3bW12aCIsIDE4MDAzMDddLCBbImEiLCAid2RrcGdjIiwgMTI1OTAxXSwgWyJ2IiwgIndka3BnYyIsIDU0ODY2Ml1dLCAiZXhwZWN0ZWQiOiBbIndka3BnYyIsICJ3ZGtwZ2MiLCAid21tdmgiXX0='

    def test_diversity_5(self):
        return 'eyJyZXBzIjogW1sidiIsICJ3eXphcHIiLCA2MDg5NDldLCBbInYiLCAia2hsIiwgNzc3NDI2XSwgWyJhIiwgImtobCIsIDE1NTg4MF1dLCAiZXhwZWN0ZWQiOiBbImtobCIsICJraGwiLCAid3l6YXByIl19'

    def test_diversity_6(self):
        return 'eyJyZXBzIjogW1sidiIsICJ0dWYiLCA3MjI1NTBdLCBbImEiLCAidHVmIiwgOTE4MTddLCBbInYiLCAicWhjZHNhIiwgNTE2Njk3NF1dLCAiZXhwZWN0ZWQiOiBbInFoY2RzYSIsICJ0dWYiLCAidHVmIl19'

    def test_diversity_7(self):
        return 'eyJyZXBzIjogW1sidiIsICJmemR0IiwgNTY0MjIxNV0sIFsiYSIsICJsY2pyeiIsIDUyMTE5XSwgWyJ2IiwgImxjanJ6IiwgODIxNjEwXSwgWyJ2IiwgImZpbG16IiwgNDA2ODI0NF1dLCAiZXhwZWN0ZWQiOiBbImZpbG16IiwgImZ6ZHQiLCAibGNqcnoiLCAibGNqcnoiXX0='

    def test_diversity_8(self):
        return 'eyJyZXBzIjogW1sidiIsICJqeGdwYmEiLCA1MDY0MjE2XSwgWyJ2IiwgInNua2Z4IiwgMzg1MzIxNV0sIFsidiIsICJjcm12ciIsIDU2OTgzODldLCBbImEiLCAiY3JtdnIiLCAxOTU3NDBdXSwgImV4cGVjdGVkIjogWyJjcm12ciIsICJjcm12ciIsICJqeGdwYmEiLCAic25rZngiXX0='

    def test_diversity_9(self):
        return 'eyJyZXBzIjogW1sidiIsICJoanN6Zm4iLCA2MjQyMTBdLCBbInYiLCAieHplYiIsIDI5OTIzODZdLCBbImEiLCAieHplYiIsIDUwNDYyXV0sICJleHBlY3RlZCI6IFsiaGpzemZuIiwgInh6ZWIiLCAieHplYiJdfQ=='

    def test_diversity_10(self):
        return 'eyJyZXBzIjogW1sidiIsICJ5Z3J1IiwgMzM0OTQyN10sIFsidiIsICJvcnBidHoiLCAyMDEzMDUyXSwgWyJhIiwgIm9ycGJ0eiIsIDEwNDE0Ml1dLCAiZXhwZWN0ZWQiOiBbIm9ycGJ0eiIsICJvcnBidHoiLCAieWdydSJdfQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJyZXBzIjogW1sidiIsICJsYmJ5IiwgNTg2NTU4M10sIFsidiIsICJ3cHZuYyIsIDE4MTI1N10sIFsidiIsICJ6cmNrIiwgMjA4Nzk0M11dLCAiZXhwZWN0ZWQiOiBbImxiYnkiLCAid3B2bmMiLCAienJjayJdfQ=='

    def test_diversity_2(self):
        return 'eyJyZXBzIjogW1sidiIsICJnemMiLCA1MjA1NDU0XSwgWyJ2IiwgImpydHdweiIsIDMyMzM0NzVdXSwgImV4cGVjdGVkIjogWyJnemMiLCAianJ0d3B6Il19'

    def test_diversity_3(self):
        return 'eyJyZXBzIjogW1sidiIsICJpZHpucSIsIDMzNDQyMjZdLCBbImEiLCAibGl4IiwgMTk1MjgwNl0sIFsidiIsICJzemdiZCIsIDM5NTI0MzNdXSwgImV4cGVjdGVkIjogWyJpZHpucSIsICJsaXgiLCAic3pnYmQiXX0='

    def test_diversity_4(self):
        return 'eyJyZXBzIjogW1siYSIsICJvaGxzIiwgMzUwNTMzMV0sIFsiYSIsICJpamRuZSIsIDE3MDk1MjVdXSwgImV4cGVjdGVkIjogWyJpamRuZSIsICJvaGxzIl19'

    def test_diversity_5(self):
        return 'eyJyZXBzIjogW1siYSIsICJjdmZtemYiLCAxOTUzNjExXSwgWyJhIiwgImR6bWdlZSIsIDIyMjIzNzRdLCBbImEiLCAiYWt5ZCIsIDMzMjc5NTBdXSwgImV4cGVjdGVkIjogWyJha3lkIiwgImN2Zm16ZiIsICJkem1nZWUiXX0='

    def test_diversity_6(self):
        return 'eyJyZXBzIjogW1siYSIsICJid250YyIsIDM1OTc3ODNdLCBbInYiLCAiaG1iIiwgNDUxNzExOF0sIFsidiIsICJsanV2aSIsIDE2MzAzODJdXSwgImV4cGVjdGVkIjogWyJid250YyIsICJobWIiLCAibGp1dmkiXX0='

    def test_diversity_7(self):
        return 'eyJyZXBzIjogW1sidiIsICJvZWNlIiwgNTEzNDQxNl0sIFsiYSIsICJsdGoiLCAzODc2NzI4XV0sICJleHBlY3RlZCI6IFsibHRqIiwgIm9lY2UiXX0='

    def test_diversity_8(self):
        return 'eyJyZXBzIjogW1sidiIsICJlZXZkcSIsIDU5ODI5ODVdLCBbImEiLCAiZG54b2IiLCA4MzQ3MzVdLCBbInYiLCAicHZ2bWsiLCA1NDQ4NDI0XSwgWyJhIiwgImx0aHgiLCA0NjA4NzBdXSwgImV4cGVjdGVkIjogWyJkbnhvYiIsICJlZXZkcSIsICJsdGh4IiwgInB2dm1rIl19'

    def test_diversity_9(self):
        return 'eyJyZXBzIjogW1siYSIsICJneXEiLCA0NTA1MzUwXSwgWyJhIiwgInNla2NlIiwgMjAzOTcwMF0sIFsiYSIsICJyZngiLCAxMzQ5NTRdLCBbInYiLCAiem5oZ2IiLCA0MDg2NjY4XV0sICJleHBlY3RlZCI6IFsiZ3lxIiwgInJmeCIsICJzZWtjZSIsICJ6bmhnYiJdfQ=='

    def test_diversity_10(self):
        return 'eyJyZXBzIjogW1sidiIsICJkdnYiLCAzNjA0Njg1XSwgWyJ2IiwgInByYXRkaSIsIDMwMzk5ODddLCBbInYiLCAib2RwaGVvIiwgNDc4NjQ1N10sIFsiYSIsICJndGNoIiwgMjc2ODUwMl1dLCAiZXhwZWN0ZWQiOiBbImR2diIsICJndGNoIiwgIm9kcGhlbyIsICJwcmF0ZGkiXX0='
