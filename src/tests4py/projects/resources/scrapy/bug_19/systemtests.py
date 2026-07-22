from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'origin_req_host aHR0cDovL2F2aGpmb2VkLmlvL3FwZXR0bi9wZWZjdg=='

    def test_diversity_2(self):
        return 'host aHR0cDovL2NreHB0Lm9yZy9zdnVnd2YvcmdseGR6L3p2ZGY='

    def test_diversity_3(self):
        return 'full_url aHR0cDovL3FhbXV6eC5vcmcvb2MveGlm'

    def test_diversity_4(self):
        return 'host aHR0cDovL292eHkuaW8vYmwvcW90'

    def test_diversity_5(self):
        return 'origin_req_host aHR0cDovL2pocGltYmxmLm9yZy9hcA=='

    def test_diversity_6(self):
        return 'full_url aHR0cDovL2NudWkubmV0L2NkZg=='

    def test_diversity_7(self):
        return 'full_url aHR0cDovL2l1ZG9iLmNvbS9jZS9pZg=='

    def test_diversity_8(self):
        return 'full_url aHR0cDovL2dnei5vcmcvdGxrZy93eGNheA=='

    def test_diversity_9(self):
        return 'type aHR0cDovL3VtaS5vcmcvYWtmby9meGZ4L2Fv'

    def test_diversity_10(self):
        return 'origin_req_host aHR0cDovL3N0di5uZXQveHRtei90Zi9hbHFqdmg='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'get_type aHR0cDovL2xhbi5pby95dw=='

    def test_diversity_2(self):
        return 'get_type aHR0cDovL2thYmwuaW8vdWo='

    def test_diversity_3(self):
        return 'get_host aHR0cDovL2Rjc2RyLm9yZy9ndC91eS9leGVqZQ=='

    def test_diversity_4(self):
        return 'get_host aHR0cDovL29kbnV4LmNvbS9idW5jdC9qc2E='

    def test_diversity_5(self):
        return 'get_host aHR0cDovL21oZmhpay5uZXQva2Uvdmds'

    def test_diversity_6(self):
        return 'get_type aHR0cDovL3pod2Mub3JnL3JrbnVkbi90eGxsamEvanZyYW0='

    def test_diversity_7(self):
        return 'get_full_url aHR0cDovL21iZmZ0ZS5vcmcveXhveXEvcmx0L2J4Yg=='

    def test_diversity_8(self):
        return 'get_type aHR0cDovL2tya2Mub3JnL2xkZnEvZ3d1ZWE='

    def test_diversity_9(self):
        return 'get_host aHR0cDovL2Z2cW5hLmlvL2txc3Zvei9oYm13bXE='

    def test_diversity_10(self):
        return 'get_host aHR0cDovL2VpcGxqci5pby9ybXB0'
