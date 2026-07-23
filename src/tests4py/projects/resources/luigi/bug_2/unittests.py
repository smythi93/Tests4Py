import unittest
import luigi
from luigi.contrib import bigquery, gcs
from luigi.contrib.beam_dataflow import BeamDataflowJobTask


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        target = bigquery.BigQueryTarget('xcvt', 'hxpm', 'dplgomf', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'xcvt:hxpm.dplgomf')

    def test_diversity_2(self):
        target = bigquery.BigQueryTarget('jxn', 'rtmrigna', 'pjt', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'jxn:rtmrigna.pjt')

    def test_diversity_3(self):
        target = bigquery.BigQueryTarget('gqvsbm', 'rehmaa', 'ofrmdr', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'gqvsbm:rehmaa.ofrmdr')

    def test_diversity_4(self):
        target = bigquery.BigQueryTarget('xbvhquqk', 'nfp', 'uqig', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'xbvhquqk:nfp.uqig')

    def test_diversity_5(self):
        target = bigquery.BigQueryTarget('onbcru', 'fjijm', 'ldszf', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'onbcru:fjijm.ldszf')

    def test_diversity_6(self):
        target = bigquery.BigQueryTarget('icger', 'eddgo', 'kviwyn', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'icger:eddgo.kviwyn')

    def test_diversity_7(self):
        target = bigquery.BigQueryTarget('tikssqzs', 'qrjkeyj', 'cyijzc', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'tikssqzs:qrjkeyj.cyijzc')

    def test_diversity_8(self):
        target = bigquery.BigQueryTarget('jxwt', 'aivpom', 'jfmz', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'jxwt:aivpom.jfmz')

    def test_diversity_9(self):
        target = bigquery.BigQueryTarget('idjc', 'ggpi', 'qpweb', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'idjc:ggpi.qpweb')

    def test_diversity_10(self):
        target = bigquery.BigQueryTarget('udnvit', 'yfbtmwo', 'ppozzvl', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'udnvit:yfbtmwo.ppozzvl')


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        target = luigi.LocalTarget('out_lwlpdxn')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_lwlpdxn')

    def test_diversity_2(self):
        target = luigi.LocalTarget('out_huacje')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_huacje')

    def test_diversity_3(self):
        target = luigi.LocalTarget('out_zivmwmbd')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_zivmwmbd')

    def test_diversity_4(self):
        target = luigi.LocalTarget('out_nbfxvnrw')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_nbfxvnrw')

    def test_diversity_5(self):
        target = luigi.LocalTarget('out_aogmuq')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_aogmuq')

    def test_diversity_6(self):
        target = gcs.GCSTarget('gs://qwxsn/ecvqfjhl', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'gs://qwxsn/ecvqfjhl')

    def test_diversity_7(self):
        target = luigi.LocalTarget('out_ihcchn')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_ihcchn')

    def test_diversity_8(self):
        target = luigi.LocalTarget('out_fssra')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_fssra')

    def test_diversity_9(self):
        target = gcs.GCSTarget('gs://fkbd/tsm', client='fake_client')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'gs://fkbd/tsm')

    def test_diversity_10(self):
        target = luigi.LocalTarget('out_vpaf')
        self.assertEqual(BeamDataflowJobTask.get_target_path(target), 'out_vpaf')
