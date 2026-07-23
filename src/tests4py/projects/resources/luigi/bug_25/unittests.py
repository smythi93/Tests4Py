import unittest
import luigi.contrib.redshift
from unittest import mock


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        class DummyS3CopyToTable_attr_cqqy_znmldp(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://cqqy/znmldp'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_cqqy_znmldp()
            task.run()
        self.assertTrue(True)

    def test_diversity_2(self):
        class DummyS3CopyToTable_attr_nwgjl_jtdtmzag(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://nwgjl/jtdtmzag'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_nwgjl_jtdtmzag()
            task.run()
        self.assertTrue(True)

    def test_diversity_3(self):
        class DummyS3CopyToTable_attr_lhwlwobc_ezvn(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://lhwlwobc/ezvn'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_lhwlwobc_ezvn()
            task.run()
        self.assertTrue(True)

    def test_diversity_4(self):
        class DummyS3CopyToTable_attr_nahixhsqd_nqfyrud(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://nahixhsqd/nqfyrud'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_nahixhsqd_nqfyrud()
            task.run()
        self.assertTrue(True)

    def test_diversity_5(self):
        class DummyS3CopyToTable_attr_pyfuskj_iaczsuvb(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://pyfuskj/iaczsuvb'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_pyfuskj_iaczsuvb()
            task.run()
        self.assertTrue(True)

    def test_diversity_6(self):
        class DummyS3CopyToTable_attr_wzpoyoxo_uwavqvvh(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://wzpoyoxo/uwavqvvh'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_wzpoyoxo_uwavqvvh()
            task.run()
        self.assertTrue(True)

    def test_diversity_7(self):
        class DummyS3CopyToTable_attr_balnln_pilgihhk(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://balnln/pilgihhk'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_balnln_pilgihhk()
            task.run()
        self.assertTrue(True)

    def test_diversity_8(self):
        class DummyS3CopyToTable_attr_ztxe_bqpwzp(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://ztxe/bqpwzp'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_ztxe_bqpwzp()
            task.run()
        self.assertTrue(True)

    def test_diversity_9(self):
        class DummyS3CopyToTable_attr_sccc_mjmymvjr(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://sccc/mjmymvjr'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_sccc_mjmymvjr()
            task.run()
        self.assertTrue(True)

    def test_diversity_10(self):
        class DummyS3CopyToTable_attr_video_lyfrscczv(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
            s3_load_path = 's3://video/lyfrscczv'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_attr_video_lyfrscczv()
            task.run()
        self.assertTrue(True)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        class DummyS3CopyToTable_method_myooqvlfz_cgwq(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://myooqvlfz/cgwq'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_myooqvlfz_cgwq()
            task.run()
        self.assertTrue(True)

    def test_diversity_2(self):
        class DummyS3CopyToTable_method_xckrn_ykuyceii(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://xckrn/ykuyceii'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_xckrn_ykuyceii()
            task.run()
        self.assertTrue(True)

    def test_diversity_3(self):
        class DummyS3CopyToTable_method_bzqbmvczz_jiojl(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://bzqbmvczz/jiojl'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_bzqbmvczz_jiojl()
            task.run()
        self.assertTrue(True)

    def test_diversity_4(self):
        class DummyS3CopyToTable_method_zzeooof_bceifg(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://zzeooof/bceifg'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_zzeooof_bceifg()
            task.run()
        self.assertTrue(True)

    def test_diversity_5(self):
        class DummyS3CopyToTable_method_gjvacvje_sddcbgyr(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://gjvacvje/sddcbgyr'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_gjvacvje_sddcbgyr()
            task.run()
        self.assertTrue(True)

    def test_diversity_6(self):
        class DummyS3CopyToTable_method_wabpv_uhxdjxrl(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://wabpv/uhxdjxrl'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_wabpv_uhxdjxrl()
            task.run()
        self.assertTrue(True)

    def test_diversity_7(self):
        class DummyS3CopyToTable_method_btgudqmg_rkoltabob(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://btgudqmg/rkoltabob'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_btgudqmg_rkoltabob()
            task.run()
        self.assertTrue(True)

    def test_diversity_8(self):
        class DummyS3CopyToTable_method_xgewbn_agml(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://xgewbn/agml'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_xgewbn_agml()
            task.run()
        self.assertTrue(True)

    def test_diversity_9(self):
        class DummyS3CopyToTable_method_wsachi_rhns(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://wsachi/rhns'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_wsachi_rhns()
            task.run()
        self.assertTrue(True)

    def test_diversity_10(self):
        class DummyS3CopyToTable_method_hxfohy_jmtx(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            table = 't'
            columns = (('c', 'text'),)
            aws_access_key_id = 'k'
            aws_secret_access_key = 's'
        
            def s3_load_path(self):
                return 's3://hxfohy/jmtx'
            copy_options = ''
        with mock.patch('luigi.contrib.redshift.RedshiftTarget'), mock.patch('luigi.contrib.redshift.S3CopyToTable.copy'):
            task = DummyS3CopyToTable_method_hxfohy_jmtx()
            task.run()
        self.assertTrue(True)
