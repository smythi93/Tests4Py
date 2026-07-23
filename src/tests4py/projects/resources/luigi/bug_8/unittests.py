import unittest
from unittest import mock
import luigi
import luigi.contrib.redshift

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):

        class Dummy_fajnzlxx(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='vxkiqpgl')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_fajnzlxx()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_2(self):

        class Dummy_zvrccli(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='aupudb')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_zvrccli()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_3(self):

        class Dummy_jvqb(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='oedzv')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_jvqb()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_4(self):

        class Dummy_noikdwy(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='vyofcv')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_noikdwy()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_5(self):

        class Dummy_tkijjqpx(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='rysdqww')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_tkijjqpx()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_6(self):

        class Dummy_flrxohxqp(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='iakcmgoax')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_flrxohxqp()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_7(self):

        class Dummy_gggbsnnky(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='dmfdyjmpe')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_gggbsnnky()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_8(self):

        class Dummy_ymboozm(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='fvgwmvip')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_ymboozm()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_9(self):

        class Dummy_jmfaymr(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='npjncihu')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_jmfaymr()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

    def test_diversity_10(self):

        class Dummy_rxdnmsnm(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='kjqypps')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_rxdnmsnm()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('lower(', query)

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):

        class Dummy_sjcou(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='ekwmy')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_sjcou()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_2(self):

        class Dummy_hmyimlqh(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='gbbobjen')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_hmyimlqh()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_3(self):

        class Dummy_aknwwhfu(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='ocudiucfb')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_aknwwhfu()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_4(self):

        class Dummy_qevhwnlad(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='prqily')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_qevhwnlad()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_5(self):

        class Dummy_efpljk(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='mtuvboqox')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_efpljk()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_6(self):

        class Dummy_detakmlb(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='nsyjsnx')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_detakmlb()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_7(self):

        class Dummy_edej(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='pushioadz')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_edej()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_8(self):

        class Dummy_qtxiuxzo(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='jyjdfz')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_qtxiuxzo()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_9(self):

        class Dummy_skoetdjcf(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='lgddoqlf')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_skoetdjcf()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)

    def test_diversity_10(self):

        class Dummy_ljkvuu(luigi.contrib.redshift.S3CopyToTable):
            host = 'h'
            database = 'd'
            user = 'u'
            password = 'p'
            aws_access_key_id = 'key'
            aws_secret_access_key = 'secret'
            copy_options = ''
            table = luigi.Parameter(default='rnusouskv')
            columns = None

            def s3_load_path(self):
                return 's3://bucket/key'
        task = Dummy_ljkvuu()
        conn = mock.MagicMock()
        cursor = conn.cursor.return_value
        luigi.contrib.redshift.S3CopyToTable.does_table_exist(task, conn)
        query = cursor.execute.call_args[0][0]
        self.assertIn('table_exists', query)
