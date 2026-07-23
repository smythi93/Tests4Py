import unittest

# noinspection PyUnresolvedReferences
from tqdm.utils import disp_trim


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('\x1b[90mXTHWQWSXOI\x1b[0m', disp_trim('\x1b[90mXTHWQWSXOI\x1b[0m', 921))

    def test_diversity_2(self):
        self.assertEqual('\x1b[33mNSPI\x1b[0m', disp_trim('\x1b[33mNSPI\x1b[0m', 952))

    def test_diversity_3(self):
        self.assertEqual('\x1b[90mELUJLZP\x1b[0m', disp_trim('\x1b[90mELUJLZP\x1b[0m', 405))

    def test_diversity_4(self):
        self.assertEqual('\x1b[96mCCFUSW\x1b[0m', disp_trim('\x1b[96mCCFUSW\x1b[0m', 753))

    def test_diversity_5(self):
        self.assertEqual('\x1b[32mTKG\x1b[0m', disp_trim('\x1b[32mTKG\x1b[0m', 881))

    def test_diversity_6(self):
        self.assertEqual('\x1b[0mZCBB\x1b[0m', disp_trim('\x1b[0mZCBB\x1b[0m', 447))

    def test_diversity_7(self):
        self.assertEqual('\x1b[37mIHXUSXSGF\x1b[0m', disp_trim('\x1b[37mIHXUSXSGF\x1b[0m', 971))

    def test_diversity_8(self):
        self.assertEqual('\x1b[92mNVFQQA\x1b[0m', disp_trim('\x1b[92mNVFQQA\x1b[0m', 758))

    def test_diversity_9(self):
        self.assertEqual('\x1b[0mDZGL\x1b[0m', disp_trim('\x1b[0mDZGL\x1b[0m', 355))

    def test_diversity_10(self):
        self.assertEqual('\x1b[96mRHMDIJY\x1b[0m', disp_trim('\x1b[96mRHMDIJY\x1b[0m', 705))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('VLYZXLMEGZ', disp_trim('VLYZXLMEGZ', 414))

    def test_diversity_2(self):
        self.assertEqual('NVVJX', disp_trim('NVVJX', 597))

    def test_diversity_3(self):
        self.assertEqual('KBXEGSC', disp_trim('KBXEGSC', 815))

    def test_diversity_4(self):
        self.assertEqual('VBG', disp_trim('VBG', 560))

    def test_diversity_5(self):
        self.assertEqual('NZBWHAVKK', disp_trim('NZBWHAVKK', 590))

    def test_diversity_6(self):
        self.assertEqual('NKE', disp_trim('NKE', 283))

    def test_diversity_7(self):
        self.assertEqual('XJIJAX', disp_trim('XJIJAX', 537))

    def test_diversity_8(self):
        self.assertEqual('PRSPPE', disp_trim('PRSPPE', 767))

    def test_diversity_9(self):
        self.assertEqual('LOLA', disp_trim('LOLA', 471))

    def test_diversity_10(self):
        self.assertEqual('UBRAPK', disp_trim('UBRAPK', 760))

