from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcImRjeXVhc1wiOlwiZ2F1aXFcIiAsIC8vbWpneWxcblwiZGVjYW16XCI6XCJicm5idmJcIn0iLCAiZXhwZWN0ZWQiOiB7ImRjeXVhcyI6ICJnYXVpcSIsICJkZWNhbXoiOiAiYnJuYnZiIn19'

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcInliaVwiOjY3MyAsIC8va3JiXG5cImVibWJmYVwiOlwieWRoXCJ9IiwgImV4cGVjdGVkIjogeyJ5YmkiOiA2NzMsICJlYm1iZmEiOiAieWRoIn19'

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcImV5ZXZiXCI6XCJtcG1ieVwiICwgLy9qdmdlY3NcblwibHV2aFwiOlwia3R5Y1wifSIsICJleHBlY3RlZCI6IHsiZXlldmIiOiAibXBtYnkiLCAibHV2aCI6ICJrdHljIn19'

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcInB5endcIjozMzEgLCAvL2hscHdyXG5cInNjZnh1ZlwiOjgxMX0iLCAiZXhwZWN0ZWQiOiB7InB5enciOiAzMzEsICJzY2Z4dWYiOiA4MTF9fQ=='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImNmeGxcIjpcInlmeGt5XCIgLCAvL2lkcXl2YlxuXCJodm5tXCI6NTYyfSIsICJleHBlY3RlZCI6IHsiY2Z4bCI6ICJ5ZnhreSIsICJodm5tIjogNTYyfX0='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImVyYmN1XCI6NDAgLCAvL2hrb25zXG5cImtpenJ5eFwiOlwia3J3dmNcIn0iLCAiZXhwZWN0ZWQiOiB7ImVyYmN1IjogNDAsICJraXpyeXgiOiAia3J3dmMifX0='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcImZzcGJ3XCI6XCJlaWJrbHJcIiAsIC8vanViXG5cImVxZXByalwiOlwidW1hdW11XCJ9IiwgImV4cGVjdGVkIjogeyJmc3BidyI6ICJlaWJrbHIiLCAiZXFlcHJqIjogInVtYXVtdSJ9fQ=='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInh4aWpcIjoyOTYgLCAvL2JzZm54XG5cInJwb3lvXCI6NzY3fSIsICJleHBlY3RlZCI6IHsieHhpaiI6IDI5NiwgInJwb3lvIjogNzY3fX0='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcImd0cG92Z1wiOlwia3JiXCIgLCAvL2dtcGpjXG5cInJ6bmxcIjo3MH0iLCAiZXhwZWN0ZWQiOiB7Imd0cG92ZyI6ICJrcmIiLCAicnpubCI6IDcwfX0='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcInJpb1wiOlwicnJ6d3FiXCIgLCAvL2p5dFxuXCJyeHRyXCI6XCJkem9wdlwifSIsICJleHBlY3RlZCI6IHsicmlvIjogInJyendxYiIsICJyeHRyIjogImR6b3B2In19'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcInhwYmZ1alwiOjcwNSxcInB6YXV2bFwiOlwicnFzdXdqXCJ9IiwgImV4cGVjdGVkIjogeyJ4cGJmdWoiOiA3MDUsICJwemF1dmwiOiAicnFzdXdqIn19'

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcImtiYXV2XCI6NTYwLFwibmR4cVwiOlwianNoa2poXCJ9IiwgImV4cGVjdGVkIjogeyJrYmF1diI6IDU2MCwgIm5keHEiOiAianNoa2poIn19'

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcInBnb2FmXCI6Mzc4LFwiaWp5c1wiOjQ2N30iLCAiZXhwZWN0ZWQiOiB7InBnb2FmIjogMzc4LCAiaWp5cyI6IDQ2N319'

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcInd6b2tcIjpcInZzanR2XCIsXCJudHB2bnNcIjozODF9IiwgImV4cGVjdGVkIjogeyJ3em9rIjogInZzanR2IiwgIm50cHZucyI6IDM4MX19'

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcInNua1wiOjEwOCxcIm1vZHVnc1wiOlwic2pvZW1cIn0iLCAiZXhwZWN0ZWQiOiB7InNuayI6IDEwOCwgIm1vZHVncyI6ICJzam9lbSJ9fQ=='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImlsbm96Y1wiOlwiZWh5Z2VcIixcInBidWdpXCI6XCJzeGV6YXBcIn0iLCAiZXhwZWN0ZWQiOiB7Imlsbm96YyI6ICJlaHlnZSIsICJwYnVnaSI6ICJzeGV6YXAifX0='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInhzeXBlXCI6MTk4LFwicGt3bnZsXCI6XCJpdmVla2FcIn0iLCAiZXhwZWN0ZWQiOiB7InhzeXBlIjogMTk4LCAicGt3bnZsIjogIml2ZWVrYSJ9fQ=='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInFmeGFrXCI6XCJiZ3FcIixcImp1Z2huelwiOjQ2Mn0iLCAiZXhwZWN0ZWQiOiB7InFmeGFrIjogImJncSIsICJqdWdobnoiOiA0NjJ9fQ=='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcImh1dVwiOjE0NixcImplZGhcIjpcInBneHl3XCJ9IiwgImV4cGVjdGVkIjogeyJodXUiOiAxNDYsICJqZWRoIjogInBneHl3In19'

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcImhpYmxsdFwiOlwidnZvZFwiLFwiemZueGlyXCI6XCJuamVcIn0iLCAiZXhwZWN0ZWQiOiB7ImhpYmxsdCI6ICJ2dm9kIiwgInpmbnhpciI6ICJuamUifX0='
