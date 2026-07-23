from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJhdHRyIjogIml0ZW1wcm9wIiwgInZhbHVlIjogImN5dSIsICJodG1sIjogIjxhIGl0ZW1wcm9wPVwiY3l1XCIgZGlzYWJsZWQ-cmN0PC9hPiIsICJleHBlY3RlZCI6ICJyY3QifQ=='

    def test_diversity_2(self):
        return 'eyJhdHRyIjogIm5hbWUiLCAidmFsdWUiOiAibW1jc3ZudyIsICJodG1sIjogIjxkaXYgaXRlbXNjb3BlIG5hbWU9XCJtbWNzdm53XCI-Ym9tcDwvZGl2PiIsICJleHBlY3RlZCI6ICJib21wIn0='

    def test_diversity_3(self):
        return 'eyJhdHRyIjogIm5hbWUiLCAidmFsdWUiOiAiYmh3Z3JmdyIsICJodG1sIjogIjxkaXYgbmFtZT1cImJod2dyZndcIiByZXF1aXJlZD55Ymk8L2Rpdj4iLCAiZXhwZWN0ZWQiOiAieWJpIn0='

    def test_diversity_4(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogImJtYiIsICJodG1sIjogIjxhIGRpc2FibGVkIGlkPVwiYm1iXCI-ZHl1eTwvYT4iLCAiZXhwZWN0ZWQiOiAiZHl1eSJ9'

    def test_diversity_5(self):
        return 'eyJhdHRyIjogIml0ZW1wcm9wIiwgInZhbHVlIjogImh1ZWV5ZSIsICJodG1sIjogIjxhIGhpZGRlbiBpdGVtcHJvcD1cImh1ZWV5ZVwiPmJraml2bTwvYT4iLCAiZXhwZWN0ZWQiOiAiYmtqaXZtIn0='

    def test_diversity_6(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogInRubGh1ayIsICJodG1sIjogIjxzZWN0aW9uIGhpZGRlbiBpZD1cInRubGh1a1wiPnljdjwvc2VjdGlvbj4iLCAiZXhwZWN0ZWQiOiAieWN2In0='

    def test_diversity_7(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogImNzenB5IiwgImh0bWwiOiAiPHAgaWQ9XCJjc3pweVwiIHJlcXVpcmVkPnd6aXU8L3A-IiwgImV4cGVjdGVkIjogInd6aXUifQ=='

    def test_diversity_8(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogInh1ZiIsICJodG1sIjogIjxhIGNoZWNrZWQgaWQ9XCJ4dWZcIj51eXo8L2E-IiwgImV4cGVjdGVkIjogInV5eiJ9'

    def test_diversity_9(self):
        return 'eyJhdHRyIjogInJlbCIsICJ2YWx1ZSI6ICJ3cnljZiIsICJodG1sIjogIjxkaXYgZGlzYWJsZWQgcmVsPVwid3J5Y2ZcIj5udmp3bnM8L2Rpdj4iLCAiZXhwZWN0ZWQiOiAibnZqd25zIn0='

    def test_diversity_10(self):
        return 'eyJhdHRyIjogIm5hbWUiLCAidmFsdWUiOiAidm5tIiwgImh0bWwiOiAiPHNwYW4gbmFtZT1cInZubVwiIGRpc2FibGVkPm1kYmVkb3M8L3NwYW4-IiwgImV4cGVjdGVkIjogIm1kYmVkb3MifQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJhdHRyIjogIml0ZW1wcm9wIiwgInZhbHVlIjogInhia2kiLCAiaHRtbCI6ICI8ZGl2IGl0ZW1wcm9wPVwieGJraVwiPnl4aHFoaTwvZGl2PiIsICJleHBlY3RlZCI6ICJ5eGhxaGkifQ=='

    def test_diversity_2(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogImNna3doY2oiLCAiaHRtbCI6ICI8c2VjdGlvbiBpZD1cImNna3doY2pcIj5odmtqPC9zZWN0aW9uPiIsICJleHBlY3RlZCI6ICJodmtqIn0='

    def test_diversity_3(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogImVpYmtsciIsICJodG1sIjogIjxhIGlkPVwiZWlia2xyXCI-ZXFlcHJqPC9hPiIsICJleHBlY3RlZCI6ICJlcWVwcmoifQ=='

    def test_diversity_4(self):
        return 'eyJhdHRyIjogInJlbCIsICJ2YWx1ZSI6ICJscnJ1c3JjIiwgImh0bWwiOiAiPHNwYW4gcmVsPVwibHJydXNyY1wiPnpteHh4PC9zcGFuPiIsICJleHBlY3RlZCI6ICJ6bXh4eCJ9'

    def test_diversity_5(self):
        return 'eyJhdHRyIjogIm5hbWUiLCAidmFsdWUiOiAiaHJpeWgiLCAiaHRtbCI6ICI8cCBuYW1lPVwiaHJpeWhcIj5udGJzPC9wPiIsICJleHBlY3RlZCI6ICJudGJzIn0='

    def test_diversity_6(self):
        return 'eyJhdHRyIjogIm5hbWUiLCAidmFsdWUiOiAiaWlndHBvdiIsICJodG1sIjogIjxzcGFuIG5hbWU9XCJpaWd0cG92XCI-andrcmI8L3NwYW4-IiwgImV4cGVjdGVkIjogImp3a3JiIn0='

    def test_diversity_7(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogIm5sbmJ0IiwgImh0bWwiOiAiPHNwYW4gaWQ9XCJubG5idFwiPmdtcGpjPC9zcGFuPiIsICJleHBlY3RlZCI6ICJnbXBqYyJ9'

    def test_diversity_8(self):
        return 'eyJhdHRyIjogInJlbCIsICJ2YWx1ZSI6ICJ3Zm1yciIsICJodG1sIjogIjxkaXYgcmVsPVwid2ZtcnJcIj53cWJuPC9kaXY-IiwgImV4cGVjdGVkIjogIndxYm4ifQ=='

    def test_diversity_9(self):
        return 'eyJhdHRyIjogImlkIiwgInZhbHVlIjogInRya3Zkem8iLCAiaHRtbCI6ICI8c3BhbiBpZD1cInRya3Zkem9cIj5wbGp5dHJ4PC9zcGFuPiIsICJleHBlY3RlZCI6ICJwbGp5dHJ4In0='

    def test_diversity_10(self):
        return 'eyJhdHRyIjogInJlbCIsICJ2YWx1ZSI6ICJpcWYiLCAiaHRtbCI6ICI8c2VjdGlvbiByZWw9XCJpcWZcIj5yam1ibGNoPC9zZWN0aW9uPiIsICJleHBlY3RlZCI6ICJyam1ibGNoIn0='
