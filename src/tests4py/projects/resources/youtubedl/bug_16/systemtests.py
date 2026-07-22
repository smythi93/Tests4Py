from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjdWVzIjogW1szMjc4LCAzMzgxLCAiemV1bnFjb20gZXVyIl0sIFsxOTMyLCAxOTgyLCAibHd5Il0sIFsyNTg5LCAyNjI5LCAiZHNka3F5ZnggbmtibWVyIl1dLCAibW9kZSI6ICJieXRlcyJ9'

    def test_diversity_2(self):
        return 'eyJjdWVzIjogW1sxOTQ1LCAyMDQyLCAiZnJzdHhtbGYgandkbWJxem8iXSwgWzQxNywgNjAyLCAiYnVyZ3NibnYgZGxoanN1bWEiXV0sICJtb2RlIjogImJ5dGVzIn0='

    def test_diversity_3(self):
        return 'eyJjdWVzIjogW1szMzQwLCAzNTIyLCAiZ2xydSJdXSwgIm1vZGUiOiAiYnl0ZXMifQ=='

    def test_diversity_4(self):
        return 'eyJjdWVzIjogW1sxNTU5LCAxNTgwLCAid2dvZmJyciJdXSwgIm1vZGUiOiAiYnl0ZXMifQ=='

    def test_diversity_5(self):
        return 'eyJjdWVzIjogW1s4MDEsIDg3MiwgImFodyJdLCBbMjIwNiwgMjM3MCwgInh0eWxrbXRrIGNjb3FicGIiXV0sICJtb2RlIjogImJ5dGVzIn0='

    def test_diversity_6(self):
        return 'eyJjdWVzIjogW1s4OTYsIDEwNTEsICJ5c2ciXSwgWzE4MDksIDE4NDIsICJrcHVzIHl5cmJxc3RxIl1dLCAibW9kZSI6ICJieXRlcyJ9'

    def test_diversity_7(self):
        return 'eyJjdWVzIjogW1s0NzYsIDYxMCwgInF1aSBycm1payJdLCBbMTYxNCwgMTY0NiwgInp2bCBkcHlxbXpjZCJdLCBbMTI2NywgMTI4NiwgInNvd2Rwc3lwIl1dLCAibW9kZSI6ICJieXRlcyJ9'

    def test_diversity_8(self):
        return 'eyJjdWVzIjogW1syODkyLCAyOTUwLCAib3FpdyBod2h3cmlxciJdXSwgIm1vZGUiOiAiYnl0ZXMifQ=='

    def test_diversity_9(self):
        return 'eyJjdWVzIjogW1syMTQyLCAyMjczLCAiamJycCJdXSwgIm1vZGUiOiAiYnl0ZXMifQ=='

    def test_diversity_10(self):
        return 'eyJjdWVzIjogW1sxOTEsIDMzMSwgIndpenFxIl0sIFsxMjM4LCAxNDE1LCAidmpwIHVwa29jIl0sIFsxMTM1LCAxMjYyLCAicnNxZW9lbnYgaHZpcCJdXSwgIm1vZGUiOiAiYnl0ZXMifQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJjdWVzIjogW1syOTMsIDM5MCwgInlpZyB3YnpjZ3NmbCJdLCBbMjE0NiwgMjI4MiwgImViemxvIGNjaHBvcCJdLCBbMTAxNiwgMTA0MywgImRhcWR2cGZwIl1dLCAibW9kZSI6ICJzdHIifQ=='

    def test_diversity_2(self):
        return 'eyJjdWVzIjogW1szMDQsIDMyOCwgInRvYXZzcCB2dXkiXSwgWzI2MDksIDI3ODIsICJnc3d1ZmgiXV0sICJtb2RlIjogInN0ciJ9'

    def test_diversity_3(self):
        return 'eyJjdWVzIjogW1s4NzAsIDEwNjAsICJvdHJmdHJreiBudXJ2ZiJdLCBbMjUyNCwgMjU0NCwgImdjbHhzbWRkIHBiaSJdLCBbMjYyMSwgMjc5NiwgInVsaWRsIHFlemtscGYiXV0sICJtb2RlIjogInN0ciJ9'

    def test_diversity_4(self):
        return 'eyJjdWVzIjogW1sxODE1LCAxODk1LCAiemt2dnFyZSBxb2dvIl0sIFsxOSwgMTk2LCAicGdic3docyBkZm0iXSwgWzMzMDUsIDMzNDEsICJqZmJjIl1dLCAibW9kZSI6ICJzdHIifQ=='

    def test_diversity_5(self):
        return 'eyJjdWVzIjogW1sxNzgsIDI3NCwgInd0eHdieiJdXSwgIm1vZGUiOiAic3RyIn0='

    def test_diversity_6(self):
        return 'eyJjdWVzIjogW1s2MDYsIDYxNywgImJlcHZkIl0sIFsyNDM3LCAyNjM0LCAic3BlYnhsIHV5Z3NveSJdXSwgIm1vZGUiOiAic3RyIn0='

    def test_diversity_7(self):
        return 'eyJjdWVzIjogW1sxNjMxLCAxNjQ5LCAibmRocCJdLCBbMjQzNSwgMjQ2NSwgImtwYWMiXSwgWzIyNzMsIDI0MTgsICJxd3BoIl1dLCAibW9kZSI6ICJzdHIifQ=='

    def test_diversity_8(self):
        return 'eyJjdWVzIjogW1syMjMwLCAyMzYzLCAibnFmeCB0cG90amh1Il0sIFsxODUsIDM2MiwgImZka3RteGggdmN3eWwiXSwgWzc2OSwgODgxLCAiZmVncm1wbyJdXSwgIm1vZGUiOiAic3RyIn0='

    def test_diversity_9(self):
        return 'eyJjdWVzIjogW1sxODYsIDMxOSwgImtyeHh2cG1uIHNzcnR5amxjIl1dLCAibW9kZSI6ICJzdHIifQ=='

    def test_diversity_10(self):
        return 'eyJjdWVzIjogW1szMDcsIDM1NSwgIndncWVxZnhxIGx4YnVhdWoiXSwgWzEzMTEsIDEzOTgsICJucmEgd2JndmMiXV0sICJtb2RlIjogInN0ciJ9'
