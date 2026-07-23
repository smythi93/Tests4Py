from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "request example.com 443"

    def test_diversity_2(self):
        return "request secure.host 8443"

    def test_diversity_3(self):
        return "request api.service.io 9443"

    def test_diversity_4(self):
        return "request data.node 10443"

    def test_diversity_5(self):
        return "request proxy.target 4443"

    def test_diversity_6(self):
        return "request cdn.assets 2096"

    def test_diversity_7(self):
        return "request mail.server 993"

    def test_diversity_8(self):
        return "request git.repo 22443"

    def test_diversity_9(self):
        return "request shop.store 6443"

    def test_diversity_10(self):
        return "request auth.gateway 7443"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "port example.com 443"

    def test_diversity_2(self):
        return "port secure.host 8443"

    def test_diversity_3(self):
        return "port api.service.io 9443"

    def test_diversity_4(self):
        return "port data.node 10443"

    def test_diversity_5(self):
        return "port proxy.target 4443"

    def test_diversity_6(self):
        return "port cdn.assets 2096"

    def test_diversity_7(self):
        return "port mail.server 993"

    def test_diversity_8(self):
        return "port git.repo 22443"

    def test_diversity_9(self):
        return "port shop.store 6443"

    def test_diversity_10(self):
        return "port auth.gateway 7443"
