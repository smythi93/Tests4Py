import unittest
import os
import tempfile
from luigi.file import LocalFileSystem



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        base = tempfile.mkdtemp(prefix='t4p_psgf_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_psgf', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_2(self):
        base = tempfile.mkdtemp(prefix='t4p_lqelrlf_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_lqelrlf', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_3(self):
        base = tempfile.mkdtemp(prefix='t4p_fzhlzpkcr_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_fzhlzpkcr', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_4(self):
        base = tempfile.mkdtemp(prefix='t4p_rfazsz_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_rfazsz', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_5(self):
        base = tempfile.mkdtemp(prefix='t4p_ordzonk_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_ordzonk', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_6(self):
        base = tempfile.mkdtemp(prefix='t4p_dnrgxz_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_dnrgxz', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_7(self):
        base = tempfile.mkdtemp(prefix='t4p_zxqgusetk_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_zxqgusetk', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_8(self):
        base = tempfile.mkdtemp(prefix='t4p_hlkcpg_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_hlkcpg', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_9(self):
        base = tempfile.mkdtemp(prefix='t4p_wbljffohu_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_wbljffohu', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_10(self):
        base = tempfile.mkdtemp(prefix='t4p_edrewkku_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'newdir_edrewkku', 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        base = tempfile.mkdtemp(prefix='t4p_tudlly_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_2(self):
        base = tempfile.mkdtemp(prefix='t4p_mppv_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_3(self):
        base = tempfile.mkdtemp(prefix='t4p_jtabrn_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_4(self):
        base = tempfile.mkdtemp(prefix='t4p_leghgkc_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_5(self):
        base = tempfile.mkdtemp(prefix='t4p_dvtfkhtsk_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_6(self):
        base = tempfile.mkdtemp(prefix='t4p_zedapjbw_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_7(self):
        base = tempfile.mkdtemp(prefix='t4p_phlrph_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_8(self):
        base = tempfile.mkdtemp(prefix='t4p_yeibsclr_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_9(self):
        base = tempfile.mkdtemp(prefix='t4p_kyyfcd_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))

    def test_diversity_10(self):
        base = tempfile.mkdtemp(prefix='t4p_lbrmzb_')
        src = os.path.join(base, 'src.txt')
        open(src, 'w').close()
        dest = os.path.join(base, 'dest.txt')
        LocalFileSystem().move(src, dest)
        self.assertTrue(os.path.exists(dest))
