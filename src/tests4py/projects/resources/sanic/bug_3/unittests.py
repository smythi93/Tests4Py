import unittest
import logging
logging.disable(logging.CRITICAL)
from sanic import Sanic

def run_url_for(name, mode, host, path):
    app = Sanic(name)
    h = None if host == '-' else host
    app.add_route(lambda request: None, path, name='r', host=h)
    return app.url_for('r', _external=mode == 'ext')

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('http://qrhei.axl/t/xklsb/aprbf', run_url_for('t4p_b3_bwvfd', 'ext', 'qrhei.axl', '/t/xklsb/aprbf'))

    def test_diversity_2(self):
        self.assertEqual('/pxuy/e/ojyyco', run_url_for('t4p_b3_jkpjur', 'noext', 'vaufkoqx', '/pxuy/e/ojyyco'))

    def test_diversity_3(self):
        self.assertEqual('http://rtv/', run_url_for('t4p_b3_kauy', 'ext', 'rtv', '/'))

    def test_diversity_4(self):
        self.assertEqual('http://ufckssde.uwuxhnom.ljtmgvo/lige', run_url_for('t4p_b3_ajuopsk', 'ext', 'ufckssde.uwuxhnom.ljtmgvo', '/lige'))

    def test_diversity_5(self):
        self.assertEqual('http://duss/cjohh/kvf', run_url_for('t4p_b3_kvbxtbm', 'ext', 'duss', '/cjohh/kvf'))

    def test_diversity_6(self):
        self.assertEqual('http://asmju/oylvf/ky/yljeo', run_url_for('t4p_b3_tgqtzs', 'ext', 'asmju', '/oylvf/ky/yljeo'))

    def test_diversity_7(self):
        self.assertEqual('http://ibfhf.tyejjo/l/fjfow', run_url_for('t4p_b3_oerkpgs', 'ext', 'ibfhf.tyejjo', '/l/fjfow'))

    def test_diversity_8(self):
        self.assertEqual('http://bhvq/z', run_url_for('t4p_b3_hrubga', 'ext', 'bhvq', '/z'))

    def test_diversity_9(self):
        self.assertEqual('http://lgg.jfqrjyu/zixk/x/nj', run_url_for('t4p_b3_umyoxlom', 'ext', 'lgg.jfqrjyu', '/zixk/x/nj'))

    def test_diversity_10(self):
        self.assertEqual('/a/x/vzx', run_url_for('t4p_b3_mjuc', 'noext', 'uakgkxn.wie.ocvftr', '/a/x/vzx'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('/', run_url_for('t4p_b3_vbaunm', 'noext', '-', '/'))

    def test_diversity_2(self):
        self.assertEqual('/', run_url_for('t4p_b3_yamtck', 'noext', '-', '/'))

    def test_diversity_3(self):
        self.assertEqual('/', run_url_for('t4p_b3_xuelo', 'noext', '-', '/'))

    def test_diversity_4(self):
        self.assertEqual('/', run_url_for('t4p_b3_krvwi', 'noext', '-', '/'))

    def test_diversity_5(self):
        self.assertEqual('/iu', run_url_for('t4p_b3_uogwpq', 'noext', '-', '/iu'))

    def test_diversity_6(self):
        self.assertEqual('/ulp/gkdxvv', run_url_for('t4p_b3_yvscv', 'noext', '-', '/ulp/gkdxvv'))

    def test_diversity_7(self):
        self.assertEqual('/tshtj/cbhaak/o', run_url_for('t4p_b3_lkvo', 'noext', '-', '/tshtj/cbhaak/o'))

    def test_diversity_8(self):
        self.assertEqual('/yaefu/ya/cmt', run_url_for('t4p_b3_aekvtzed', 'noext', '-', '/yaefu/ya/cmt'))

    def test_diversity_9(self):
        self.assertEqual('/sobjj/q/vfw', run_url_for('t4p_b3_aaobwihj', 'noext', '-', '/sobjj/q/vfw'))

    def test_diversity_10(self):
        self.assertEqual('/bhca/mk/ay', run_url_for('t4p_b3_lheqyw', 'noext', '-', '/bhca/mk/ay'))
