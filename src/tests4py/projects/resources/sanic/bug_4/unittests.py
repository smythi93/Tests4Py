import unittest
import logging
logging.disable(logging.CRITICAL)
from sanic import Sanic
from sanic.request import Request
from sanic.compat import Header

class _Transport:

    def get_extra_info(self, key):
        if key == 'sockname':
            return ('127.0.0.1', 8000)
        return None

def run_request_url_for(name, server_name, path, host_header):
    app = Sanic(name)
    if server_name != '-':
        app.config.SERVER_NAME = server_name
    app.add_route(lambda request: None, path, name='target')
    headers = Header()
    headers['Host'] = host_header
    req = Request(b'/sample', headers, '1.1', 'GET', _Transport(), app)
    return req.url_for('target')

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertTrue(run_request_url_for('t4p_b4_esltv', '-', '/fna/ewihbw', 'amhrz.lrsj:52134').startswith('http'))

    def test_diversity_2(self):
        self.assertTrue(run_request_url_for('t4p_b4_elilh', '-', '/xf/bprxn', 'kxbko.aptzo.zgvi:9497').startswith('http'))

    def test_diversity_3(self):
        self.assertTrue(run_request_url_for('t4p_b4_zstotc', '-', '/khwi', 'czzprg.azag.xabs:51923').startswith('http'))

    def test_diversity_4(self):
        self.assertTrue(run_request_url_for('t4p_b4_xwcu', '-', '/xkvgxi/fdwsh/e', 'rtmqdase.kazdnt.ilqckml:24900').startswith('http'))

    def test_diversity_5(self):
        self.assertTrue(run_request_url_for('t4p_b4_rrmmyn', '-', '/f/iy', 'yvaaugn.xvf:51000').startswith('http'))

    def test_diversity_6(self):
        self.assertTrue(run_request_url_for('t4p_b4_dnfuo', '-', '/envvv/u', 'ueg.wlikplm:15306').startswith('http'))

    def test_diversity_7(self):
        self.assertTrue(run_request_url_for('t4p_b4_zkgcb', '-', '/lotbd/as/jdsf', 'fvg.ojfwpk.kvxxw:27922').startswith('http'))

    def test_diversity_8(self):
        self.assertTrue(run_request_url_for('t4p_b4_zipkqu', '-', '/eodddk/kphk/pvjcki', 'ozrf:18367').startswith('http'))

    def test_diversity_9(self):
        self.assertTrue(run_request_url_for('t4p_b4_feaaxrar', '-', '/wbs', 'arhtb:3000').startswith('http'))

    def test_diversity_10(self):
        self.assertTrue(run_request_url_for('t4p_b4_dioyxx', '-', '/q/dmdsi', 'nrjd.oujobw.chublmk:25964').startswith('http'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertTrue(run_request_url_for('t4p_b4_obmei', 'qvb.syilnk.cmfmi:41820', '/zvwbs/on', 'obmp:28847').startswith('http'))

    def test_diversity_2(self):
        self.assertTrue(run_request_url_for('t4p_b4_dzcmknr', 'muvxqcm.pzqoc:28753', '/gp', 'yogeid.xrwst:55723').startswith('http'))

    def test_diversity_3(self):
        self.assertTrue(run_request_url_for('t4p_b4_gkoakur', 'zcttobv.rxuzkmof:13719', '/jm/epdtro/m', 'txed:43133').startswith('http'))

    def test_diversity_4(self):
        self.assertTrue(run_request_url_for('t4p_b4_qmiabpkp', 'fflb.cdvadxal:18679', '/dvzztn', 'sijghx:38860').startswith('http'))

    def test_diversity_5(self):
        self.assertTrue(run_request_url_for('t4p_b4_mzramjub', 'dwspnk:30342', '/mp', 'kpojszev.lyktgke:11519').startswith('http'))

    def test_diversity_6(self):
        self.assertTrue(run_request_url_for('t4p_b4_juvyiwo', 'tsno:30467', '/aotv/yybtm/cmysg', 'dnwdq.wtc.xdj:9900').startswith('http'))

    def test_diversity_7(self):
        self.assertTrue(run_request_url_for('t4p_b4_jtcm', 'fieo:17035', '/gbxm/trwq', 'fuppvv:19488').startswith('http'))

    def test_diversity_8(self):
        self.assertTrue(run_request_url_for('t4p_b4_jhgb', 'qyxlaon.lbnjcgka.pai:59509', '/s/ewibh', 'fesjqwt.etksfm.wucwvin:24999').startswith('http'))

    def test_diversity_9(self):
        self.assertTrue(run_request_url_for('t4p_b4_krhl', 'msoi:15210', '/zd/rucle', 'hrmfqdlh:9487').startswith('http'))

    def test_diversity_10(self):
        self.assertTrue(run_request_url_for('t4p_b4_sqhwpn', 'mlfbg:47260', '/v/g/gfw', 'vhnrlr.qfk:18616').startswith('http'))
