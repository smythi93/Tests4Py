from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "({}, 'OvnzmorJdeQiTAI', {})"

    def test_diversity_2(self):
        return "({}, 'JXWnCkBU', {})"

    def test_diversity_3(self):
        return "({}, 'UjazvqVmKTLVZoS', {})"

    def test_diversity_4(self):
        return "({}, 'vMTkjJ', {})"

    def test_diversity_5(self):
        return "({}, 'BzVDGJuMZvhD', {})"

    def test_diversity_6(self):
        return "({}, 'ZPHMXAE', {})"

    def test_diversity_7(self):
        return "({}, 'zxueOqsy', {})"

    def test_diversity_8(self):
        return "({}, 'inTbypj', {})"

    def test_diversity_9(self):
        return "({}, 'EAipohAynHYzv', {})"

    def test_diversity_10(self):
        return "({}, 'PfJnytz', {})"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "({'key': {'etag': '0', 'value': 'VquzIcZoOKd'}}, 'VquzIcZoOKd', {})"

    def test_diversity_2(self):
        return "({'key': {'etag': '0', 'value': 'HydMqeApgKAAHY'}}, 'HydMqeApgKAAHY', {})"

    def test_diversity_3(self):
        return "({'key': {'etag': '0', 'value': 'hDmuYowlPly'}}, 'hDmuYowlPly', {})"

    def test_diversity_4(self):
        return "({'key': {'etag': '0', 'value': 'pisrVWaFQRs'}}, 'pisrVWaFQRs', {})"

    def test_diversity_5(self):
        return "({'key': {'etag': '0', 'value': 'HTTxTk'}}, 'HTTxTk', {})"

    def test_diversity_6(self):
        return "({'key': {'etag': '0', 'value': 'vfkfufKx'}}, 'vfkfufKx', {})"

    def test_diversity_7(self):
        return "({'key': {'etag': '0', 'value': 'ApUEudUrLSbpaU'}}, 'ApUEudUrLSbpaU', {})"

    def test_diversity_8(self):
        return "({'key': {'etag': '0', 'value': 'Yngnoq'}}, 'Yngnoq', {})"

    def test_diversity_9(self):
        return "({'key': {'etag': '0', 'value': 'hyUbAtxfMfPqwT'}}, 'hyUbAtxfMfPqwT', {})"

    def test_diversity_10(self):
        return "({'key': {'etag': '0', 'value': 'XxGQyv'}}, 'XxGQyv', {})"
