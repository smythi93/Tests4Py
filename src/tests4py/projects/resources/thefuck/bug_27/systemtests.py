from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('xdg-open http://nqmiserbbx.io', 'xdg-open nqmiserbbx.io')"

    def test_diversity_2(self):
        return "('xdg-open http://hlrzhcq.io', 'xdg-open hlrzhcq.io')"

    def test_diversity_3(self):
        return "('xdg-open http://pwqef.io', 'xdg-open pwqef.io')"

    def test_diversity_4(self):
        return "('xdg-open http://mwwafr.io', 'xdg-open mwwafr.io')"

    def test_diversity_5(self):
        return "('gnome-open http://xlgil.io', 'gnome-open xlgil.io')"

    def test_diversity_6(self):
        return "('xdg-open http://woqhwtqs.io', 'xdg-open woqhwtqs.io')"

    def test_diversity_7(self):
        return "('xdg-open http://ubpjkx.io', 'xdg-open ubpjkx.io')"

    def test_diversity_8(self):
        return "('xdg-open http://bxliuqtjvh.io', 'xdg-open bxliuqtjvh.io')"

    def test_diversity_9(self):
        return "('xdg-open http://oxfyn.io', 'xdg-open oxfyn.io')"

    def test_diversity_10(self):
        return "('gnome-open http://rsuno.io', 'gnome-open rsuno.io')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('open http://jtqvlcqrcl.com', 'open jtqvlcqrcl.com')"

    def test_diversity_2(self):
        return "('open http://yimyfg.io', 'open yimyfg.io')"

    def test_diversity_3(self):
        return "('open http://hfjqzm.com', 'open hfjqzm.com')"

    def test_diversity_4(self):
        return "('open http://sczzihl.io', 'open sczzihl.io')"

    def test_diversity_5(self):
        return "('open http://fpbdld.com', 'open fpbdld.com')"

    def test_diversity_6(self):
        return "('open http://jnhnvc.io', 'open jnhnvc.io')"

    def test_diversity_7(self):
        return "('open http://gwjhzebfqb.io', 'open gwjhzebfqb.io')"

    def test_diversity_8(self):
        return "('open http://tvlebuhloh.com', 'open tvlebuhloh.com')"

    def test_diversity_9(self):
        return "('open http://nevdubas.com', 'open nevdubas.com')"

    def test_diversity_10(self):
        return "('open http://fngyxeol.io', 'open fngyxeol.io')"
