import unittest
import luigi
import luigi.contrib.redshift
from unittest import mock

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        class Dummy_none_mxciytngw(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='mxciytngw')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_mxciytngw()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_2(self):

        class Dummy_none_dzyxcr(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='dzyxcr')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_dzyxcr()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_3(self):

        class Dummy_none_ltxtoasy(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='ltxtoasy')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_ltxtoasy()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_4(self):

        class Dummy_none_hcrondo(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='hcrondo')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_hcrondo()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_5(self):

        class Dummy_none_bskwkszm(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='bskwkszm')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_bskwkszm()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_6(self):

        class Dummy_none_uzaoxc(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='uzaoxc')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_uzaoxc()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_7(self):

        class Dummy_none_gtwfz(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='gtwfz')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_gtwfz()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_8(self):

        class Dummy_none_kypvempe(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='kypvempe')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_kypvempe()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_9(self):

        class Dummy_none_rcemffj(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='rcemffj')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_rcemffj()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_10(self):

        class Dummy_none_jfpfiyz(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='jfpfiyz')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_none_jfpfiyz()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):

        class Dummy_cols_qpoivhng(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='qpoivhng')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_qpoivhng()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_2(self):

        class Dummy_cols_rowg(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='rowg')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_rowg()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_3(self):

        class Dummy_cols_xdihpqg(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='xdihpqg')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_xdihpqg()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_4(self):

        class Dummy_cols_roppcppe(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='roppcppe')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_roppcppe()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_5(self):

        class Dummy_cols_plavpxe(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='plavpxe')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_plavpxe()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_6(self):

        class Dummy_cols_uzvpir(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='uzvpir')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_uzvpir()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_7(self):

        class Dummy_cols_ujgzyfjx(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='ujgzyfjx')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_ujgzyfjx()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_8(self):

        class Dummy_cols_jmokwaqix(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='jmokwaqix')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_jmokwaqix()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_9(self):

        class Dummy_cols_nthtl(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='nthtl')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_nthtl()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)

    def test_diversity_10(self):

        class Dummy_cols_nqov(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='nqov')
            columns = (('a', 'int'), ('b', 'varchar'))

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_cols_nqov()
        luigi.contrib.redshift.S3CopyToTable.copy(task, mock.Mock(), 's3://bucket/key')
        self.assertTrue(True)
