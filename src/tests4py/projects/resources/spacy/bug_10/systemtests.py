from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "hgwevdghw TEXT"

    def test_diversity_2(self):
        return "vhgdhg TEXT"

    def test_diversity_3(self):
        return "vaghdsvh TEXT"

    def test_diversity_4(self):
        return "hgfyFCGFs TEXT"

    def test_diversity_5(self):
        return "dbhwvduw TEXT"

    def test_diversity_6(self):
        return "BBVDHG TEXT"

    def test_diversity_7(self):
        return "jabsjdwj TEXT"

    def test_diversity_8(self):
        return "HSVDGH TEXT"

    def test_diversity_9(self):
        return "qbdghwe TEXT"

    def test_diversity_10(self):
        return "hjasbdgavjd TEXT"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "jhgsdgqw INVALID KEY"

    def test_diversity_2(self):
        return "JHBJGV INVALID KEY"

    def test_diversity_3(self):
        return "hgjKHKHK INVALID KEY"

    def test_diversity_4(self):
        return "hjghHHS INVALID KEY"

    def test_diversity_5(self):
        return "bhggYFGFGH INVALID KEY"

    def test_diversity_6(self):
        return "HGGHFhgn INVALID KEY"

    def test_diversity_7(self):
        return "uywegruywe INVALID KEY"

    def test_diversity_8(self):
        return "wehdguew INVALID KEY"

    def test_diversity_9(self):
        return "ajhsbdjh INVALID KEY"

    def test_diversity_10(self):
        return "HJSGHDW INVALID KEY"
