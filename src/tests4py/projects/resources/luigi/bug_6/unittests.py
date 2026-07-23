import unittest
import luigi



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        class Task_tuple_dicts_szxpj_qfvdn(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_dicts_szxpj_qfvdn(args=({'szxpj': 'qfvdn'}, {'qfvdn': 'szxpj'}))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_2(self):
        class Task_tuple_dicts_kfwzotag_drdycb(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_dicts_kfwzotag_drdycb(args=({'kfwzotag': 'drdycb'}, {'drdycb': 'kfwzotag'}))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_3(self):
        class Task_tuple_dicts_qvtsiils_fpqnvvxt(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_dicts_qvtsiils_fpqnvvxt(args=({'qvtsiils': 'fpqnvvxt'}, {'fpqnvvxt': 'qvtsiils'}))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_4(self):
        class Task_tuple_dicts_opjt_jqrsf(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_dicts_opjt_jqrsf(args=({'opjt': 'jqrsf'}, {'jqrsf': 'opjt'}))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_5(self):
        class Task_tuple_dicts_clbsewee_koiy(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_dicts_clbsewee_koiy(args=({'clbsewee': 'koiy'}, {'koiy': 'clbsewee'}))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_6(self):
        class Task_tuple_dicts_igpfqu_rktbho(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_dicts_igpfqu_rktbho(args=({'igpfqu': 'rktbho'}, {'rktbho': 'igpfqu'}))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_7(self):
        class Task_list_dicts_jgitmqaq_ukrbmgxk(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_dicts_jgitmqaq_ukrbmgxk(args=[{'jgitmqaq': 'ukrbmgxk'}, {'ukrbmgxk': 'jgitmqaq'}])
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_8(self):
        class Task_list_dicts_hlpzkfz_btll(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_dicts_hlpzkfz_btll(args=[{'hlpzkfz': 'btll'}, {'btll': 'hlpzkfz'}])
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_9(self):
        class Task_list_dicts_hsqhv_akcn(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_dicts_hsqhv_akcn(args=[{'hsqhv': 'akcn'}, {'akcn': 'hsqhv'}])
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_10(self):
        class Task_list_dicts_xazpox_glx(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_dicts_xazpox_glx(args=[{'xazpox': 'glx'}, {'glx': 'xazpox'}])
        self.assertIsInstance(hash(inst.args), int)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        class Task_tuple_nested_jtiirks_cuoz(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_nested_jtiirks_cuoz(args=(('jtiirks', 'cuoz'), ('cuoz', 'jtiirks')))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_2(self):
        class Task_tuple_flat_xriltmyf_bhcvqjp(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_flat_xriltmyf_bhcvqjp(args=('xriltmyf', 'bhcvqjp'))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_3(self):
        class Task_list_nested_sval_faq(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_nested_sval_faq(args=[['sval', 'faq'], ['faq', 'sval']])
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_4(self):
        class Task_tuple_flat_bniy_sdlg(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_flat_bniy_sdlg(args=('bniy', 'sdlg'))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_5(self):
        class Task_tuple_nested_zcxa_omgd(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_nested_zcxa_omgd(args=(('zcxa', 'omgd'), ('omgd', 'zcxa')))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_6(self):
        class Task_tuple_flat_roffy_zvuoi(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_flat_roffy_zvuoi(args=('roffy', 'zvuoi'))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_7(self):
        class Task_list_nested_kmrn_sip(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_nested_kmrn_sip(args=[['kmrn', 'sip'], ['sip', 'kmrn']])
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_8(self):
        class Task_tuple_nested_zsdzmq_hbktegl(luigi.Task):
            args = luigi.TupleParameter()
        inst = Task_tuple_nested_zsdzmq_hbktegl(args=(('zsdzmq', 'hbktegl'), ('hbktegl', 'zsdzmq')))
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_9(self):
        class Task_list_nested_ranq_ucqlafg(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_nested_ranq_ucqlafg(args=[['ranq', 'ucqlafg'], ['ucqlafg', 'ranq']])
        self.assertIsInstance(hash(inst.args), int)

    def test_diversity_10(self):
        class Task_list_nested_hofcfe_eqnevgbo(luigi.Task):
            args = luigi.ListParameter()
        inst = Task_list_nested_hofcfe_eqnevgbo(args=[['hofcfe', 'eqnevgbo'], ['eqnevgbo', 'hofcfe']])
        self.assertIsInstance(hash(inst.args), int)
