import unittest
from httpie.sessions import Session

def run_update(pairs):
    s = Session('/tmp/t4p_httpie_bug3_unit.json')
    s['headers'] = {}
    headers = {}
    for name, value in pairs:
        headers[name] = None if value is None else value.encode('utf8')
    s.update_headers(headers)
    return True

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertTrue(run_update([('Cache', 'uki'), ('X-Custom', None), ('Foo', 'opyfnb'), ('Referer', 'bbphu')]))

    def test_diversity_2(self):
        self.assertTrue(run_update([('Authorization', 'bgsbsz'), ('Referer', None), ('X-Test', 'cki'), ('Accept', 'dzypx')]))

    def test_diversity_3(self):
        self.assertTrue(run_update([('Accept', 'efknnfe'), ('Authorization', None), ('Bar', 'wvngki'), ('X-Token', 'miu')]))

    def test_diversity_4(self):
        self.assertTrue(run_update([('X-Api', 'xustzc'), ('Bar', 'xikah'), ('X-Token', None)]))

    def test_diversity_5(self):
        self.assertTrue(run_update([('Foo', 'pzrhxy'), ('X-Trace', None), ('X-Test', 'yikuwvn')]))

    def test_diversity_6(self):
        self.assertTrue(run_update([('Foo', None), ('Referer', 'uwqcxge'), ('Authorization', 'phg')]))

    def test_diversity_7(self):
        self.assertTrue(run_update([('X-Test', None), ('Authorization', 'tzs')]))

    def test_diversity_8(self):
        self.assertTrue(run_update([('X-Trace', None), ('Referer', 'oewzxhiy')]))

    def test_diversity_9(self):
        self.assertTrue(run_update([('X-Api', None), ('X-Token', 'shwlf'), ('X-Custom', 'jgxpng')]))

    def test_diversity_10(self):
        self.assertTrue(run_update([('X-Test', None), ('Bar', 'tnp'), ('Authorization', 'lnl')]))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertTrue(run_update([('X-Trace', 'hrj'), ('Accept', 'fgtf')]))

    def test_diversity_2(self):
        self.assertTrue(run_update([('Referer', 'bqcog'), ('Bar', 'cjxys'), ('Cache', 'ksti')]))

    def test_diversity_3(self):
        self.assertTrue(run_update([('X-Token', 'oizgy')]))

    def test_diversity_4(self):
        self.assertTrue(run_update([('Cache', 'umojg')]))

    def test_diversity_5(self):
        self.assertTrue(run_update([('X-Token', 'zwnvztog'), ('X-Api', 'sacuen'), ('Referer', 'osrgz')]))

    def test_diversity_6(self):
        self.assertTrue(run_update([('Cache', 'upwet'), ('Accept', 'bwn')]))

    def test_diversity_7(self):
        self.assertTrue(run_update([('X-Api', 'hucyshou')]))

    def test_diversity_8(self):
        self.assertTrue(run_update([('Referer', 'nyadfim')]))

    def test_diversity_9(self):
        self.assertTrue(run_update([('X-Test', 'pofophvn'), ('X-Api', 'trsqyhw')]))

    def test_diversity_10(self):
        self.assertTrue(run_update([('Cache', 'sumoki')]))