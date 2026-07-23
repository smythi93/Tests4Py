import unittest
import logging
from sanic.log import LOGGING_CONFIG_DEFAULTS

def run_sanic_root_level(name, base, target):
    logging.getLogger().setLevel(base)
    cfg = LOGGING_CONFIG_DEFAULTS
    if 'sanic.root' in cfg['loggers']:
        cfg['loggers']['sanic.root']['level'] = target
    from sanic import Sanic
    app = Sanic(name, log_config=cfg)
    return logging.getLevelName(logging.getLogger('sanic.root').getEffectiveLevel())

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('DEBUG', run_sanic_root_level('t4p_b5_owszfwzm', 'WARNING', 'DEBUG'))

    def test_diversity_2(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_pknra', 'ERROR', 'WARNING'))

    def test_diversity_3(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_vbmzkboc', 'DEBUG', 'WARNING'))

    def test_diversity_4(self):
        self.assertEqual('DEBUG', run_sanic_root_level('t4p_b5_rduwwlq', 'ERROR', 'DEBUG'))

    def test_diversity_5(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_hbenogv', 'ERROR', 'WARNING'))

    def test_diversity_6(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_swyrtuf', 'ERROR', 'WARNING'))

    def test_diversity_7(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_mptngepj', 'CRITICAL', 'WARNING'))

    def test_diversity_8(self):
        self.assertEqual('DEBUG', run_sanic_root_level('t4p_b5_xaciyb', 'CRITICAL', 'DEBUG'))

    def test_diversity_9(self):
        self.assertEqual('ERROR', run_sanic_root_level('t4p_b5_rrrtfqxs', 'DEBUG', 'ERROR'))

    def test_diversity_10(self):
        self.assertEqual('INFO', run_sanic_root_level('t4p_b5_axgwcg', 'WARNING', 'INFO'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_vtdvvkp', 'WARNING', 'WARNING'))

    def test_diversity_2(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_udnytqjf', 'WARNING', 'WARNING'))

    def test_diversity_3(self):
        self.assertEqual('DEBUG', run_sanic_root_level('t4p_b5_phawgapd', 'DEBUG', 'DEBUG'))

    def test_diversity_4(self):
        self.assertEqual('INFO', run_sanic_root_level('t4p_b5_jpnpuuj', 'INFO', 'INFO'))

    def test_diversity_5(self):
        self.assertEqual('DEBUG', run_sanic_root_level('t4p_b5_boifbb', 'DEBUG', 'DEBUG'))

    def test_diversity_6(self):
        self.assertEqual('INFO', run_sanic_root_level('t4p_b5_wudswtxv', 'INFO', 'INFO'))

    def test_diversity_7(self):
        self.assertEqual('DEBUG', run_sanic_root_level('t4p_b5_kodw', 'DEBUG', 'DEBUG'))

    def test_diversity_8(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_xvjci', 'WARNING', 'WARNING'))

    def test_diversity_9(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_jzss', 'WARNING', 'WARNING'))

    def test_diversity_10(self):
        self.assertEqual('WARNING', run_sanic_root_level('t4p_b5_cfps', 'WARNING', 'WARNING'))
