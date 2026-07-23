import unittest
import logging
logging.disable(logging.CRITICAL)
from sanic import Sanic

def run_named_middleware_order(name, kind, n):

    def make(i):

        def mw(request, response=None):
            return None
        mw.idx = i
        return mw
    app = Sanic(name)
    for i in range(n):
        app.register_named_middleware(make(i), ['route'], attach_to=kind)
    if kind == 'response':
        dq = app.named_response_middleware.get('route')
    else:
        dq = app.named_request_middleware.get('route')
    return [m.idx for m in dq] if dq else []

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_12_mksfb', 'response', 12))

    def test_diversity_2(self):
        self.assertEqual([3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_4_whfl', 'response', 4))

    def test_diversity_3(self):
        self.assertEqual([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_13_vfun', 'response', 13))

    def test_diversity_4(self):
        self.assertEqual([17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_18_aeevgb', 'response', 18))

    def test_diversity_5(self):
        self.assertEqual([3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_4_moophoil', 'response', 4))

    def test_diversity_6(self):
        self.assertEqual([16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_17_uqkjvs', 'response', 17))

    def test_diversity_7(self):
        self.assertEqual([13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_14_cpyrug', 'response', 14))

    def test_diversity_8(self):
        self.assertEqual([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_13_eyyqid', 'response', 13))

    def test_diversity_9(self):
        self.assertEqual([6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_7_jres', 'response', 7))

    def test_diversity_10(self):
        self.assertEqual([6, 5, 4, 3, 2, 1, 0], run_named_middleware_order('t4p_b1_response_7_tpagj', 'response', 7))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], run_named_middleware_order('t4p_b1_request_14_cuvplrq', 'request', 14))

    def test_diversity_2(self):
        self.assertEqual([0, 1], run_named_middleware_order('t4p_b1_request_2_vfxd', 'request', 2))

    def test_diversity_3(self):
        self.assertEqual([0], run_named_middleware_order('t4p_b1_response_1_vggce', 'response', 1))

    def test_diversity_4(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], run_named_middleware_order('t4p_b1_request_20_rpywzdgp', 'request', 20))

    def test_diversity_5(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], run_named_middleware_order('t4p_b1_request_10_envteqsy', 'request', 10))

    def test_diversity_6(self):
        self.assertEqual([0], run_named_middleware_order('t4p_b1_response_1_osfs', 'response', 1))

    def test_diversity_7(self):
        self.assertEqual([0, 1, 2, 3], run_named_middleware_order('t4p_b1_request_4_tfinmxdj', 'request', 4))

    def test_diversity_8(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], run_named_middleware_order('t4p_b1_request_11_msgdyfnz', 'request', 11))

    def test_diversity_9(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], run_named_middleware_order('t4p_b1_request_13_arnwwmv', 'request', 13))

    def test_diversity_10(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], run_named_middleware_order('t4p_b1_request_10_rdompofz', 'request', 10))
