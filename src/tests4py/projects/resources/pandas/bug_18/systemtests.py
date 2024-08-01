from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "0.0, 2.234896, 2.224896, 2.224896, 2.224896, 2.234896, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_2(self):
        return "0.0, 2.237654, 2.227654, 2.227654, 2.227654, 2.237654, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_3(self):
        return "0.0, 2.231234, 2.221234, 2.221234, 2.221234, 2.231234, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_4(self):
        return "0.0, 2.236547, 2.226547, 2.226547, 2.226547, 2.236547, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_5(self):
        return "0.0, 2.230912, 2.220912, 2.220912, 2.220912, 2.230912, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_6(self):
        return "0.0, 2.234389, 2.224389, 2.224389, 2.224389, 2.234389, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_7(self):
        return "0.0, 2.236576, 2.226576, 2.226576, 2.226576, 2.236576, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_8(self):
        return "0.0, 2.233386, 2.223386, 2.223386, 2.223386, 2.233386, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_9(self):
        return "0.0, 2.230032, 2.220032, 2.220032, 2.220032, 2.230032, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_10(self):
        return "0.0, 2.234242, 2.224242, 2.224242, 2.224242, 2.234242, 0.0, 0.0, numpy.nan, numpy.nan"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "0.0, 2.2323963331, 2.2295083331, 2.2283403331, 2.2290913331, 2.2319893331, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_2(self):
        return "0.0, 2.2323963332, 2.2295083332, 2.2283403332, 2.2290913332, 2.2319893332, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_3(self):
        return "0.0, 2.2323963330, 2.2295083330, 2.2283403330, 2.2290913330, 2.2319893330, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_4(self):
        return "0.0, 2.2323963333, 2.2295083333, 2.2283403333, 2.2290913333, 2.2319893333, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_5(self):
        return "0.0, 2.2323963334, 2.2295083334, 2.2283403334, 2.2290913334, 2.2319893334, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_6(self):
        return "0.0, 2.2323963335, 2.2295083335, 2.2283403335, 2.2290913335, 2.2319893335, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_7(self):
        return "0.0, 2.2323963336, 2.2295083336, 2.2283403336, 2.2290913336, 2.2319893336, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_8(self):
        return "0.0, 2.2323963337, 2.2295083337, 2.2283403337, 2.2290913337, 2.2319893337, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_9(self):
        return "0.0, 2.2323963338, 2.2295083338, 2.2283403338, 2.2290913338, 2.2319893338, 0.0, 0.0, numpy.nan, numpy.nan"

    def test_diversity_10(self):
        return "0.0, 2.2323963366, 2.2295083366, 2.2283403366, 2.2290913366, 2.2319893366, 0.0, 0.0, numpy.nan, numpy.nan"
