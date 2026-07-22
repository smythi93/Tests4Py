from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQocGZjcCwgbXVnamRmdCwgZmx1c2g9VHJ1ZSkK'

    def test_diversity_2(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQoenFxeCwgZ2ZmLCBoanBuLCBmbHVzaD1UcnVlKQo='

    def test_diversity_3(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQod2ZhLCB1c2pncWQsIGVuZD0iIikK'

    def test_diversity_4(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQoenZveCwgdmt1bmdqLCBmaWxlPXN5cy5zdGRlcnIpCg=='

    def test_diversity_5(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQodGZyb3F0YywgZ215biwgZW5kPSIiKQo='

    def test_diversity_6(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQodnpseWgsIHF6Y3NpeWQsIGVuZD0iIikK'

    def test_diversity_7(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQoZnl1c2JqLCBhY2NzLCB4d3djamZpLCBmbHVzaD1UcnVlKQo='

    def test_diversity_8(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQoYWt1enJrcCwgdWR1Y2h3cCwganNkY2IsIGZpbGU9c3lzLnN0ZGVycikK'

    def test_diversity_9(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQobXV6bSwga3Flc2pnZCwgcmZzLCBmaWxlPXN5cy5zdGRlcnIpCg=='

    def test_diversity_10(self):
        return 'ZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgoKcHJpbnQocmhtaHR2YXcsIGVuZD0iIikK'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'aXd1dW1zID0gWzYsIDJdCg=='

    def test_diversity_2(self):
        return 'aXd5ID0gNgo='

    def test_diversity_3(self):
        return 'ZGVmIHRma3oob3VmcWcpOgogICAgcmV0dXJuIDYK'

    def test_diversity_4(self):
        return 'emd1ID0gOAo='

    def test_diversity_5(self):
        return 'ZGVmIHJqZihhZG9xeSk6CiAgICByZXR1cm4gNgo='

    def test_diversity_6(self):
        return 'c2VkcnYgPSA5Cg=='

    def test_diversity_7(self):
        return 'Z3l1ZHAgPSAzCg=='

    def test_diversity_8(self):
        return 'c3FncyA9IFs1LCA4XQo='

    def test_diversity_9(self):
        return 'Z2RndyA9IDIK'

    def test_diversity_10(self):
        return 'ZGVmIGFzcWUocWxnZWwpOgogICAgcmV0dXJuIDcK'
