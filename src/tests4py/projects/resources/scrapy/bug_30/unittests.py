import unittest

# noinspection PyUnresolvedReferences
import sys
import subprocess


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        tag = 632115
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_2(self):
        tag = 242872
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_3(self):
        tag = 420651
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_4(self):
        tag = 688834
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_5(self):
        tag = 988569
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_6(self):
        tag = 869076
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_7(self):
        tag = 455233
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_8(self):
        tag = 467326
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_9(self):
        tag = 960786
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_10(self):
        tag = 179156
        proc = subprocess.run([sys.executable, '-m', 'scrapy.cmdline', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        tag = 472037
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_2(self):
        tag = 7063
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_3(self):
        tag = 119458
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_4(self):
        tag = 557660
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_5(self):
        tag = 161556
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_6(self):
        tag = 459168
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_7(self):
        tag = 245636
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_8(self):
        tag = 785923
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_9(self):
        tag = 896633
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))

    def test_diversity_10(self):
        tag = 679461
        proc = subprocess.run([sys.executable, '-c', "import scrapy; print('Scrapy ' + scrapy.__version__)"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = proc.stdout.decode('utf-8', 'replace').strip()
        self.assertEqual(0, proc.returncode)
        self.assertTrue(out.startswith('Scrapy '))
