import unittest
import httpie.downloads

def run_unique_filename(orig, attempt, max_len):
    httpie.downloads.get_filename_max_length = lambda directory: max_len

    def exists(filename):
        if exists.attempt == attempt:
            return False
        exists.attempt += 1
        return True
    exists.attempt = 0
    return httpie.downloads.get_unique_filename(orig, exists)

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('LLLLLLLLL-1', run_unique_filename('LLLLLLLLLLLLLLL', 1, 11))

    def test_diversity_2(self):
        self.assertEqual('J.log-10', run_unique_filename('JJJJJJJJJJJJJJJJ.log', 10, 8))

    def test_diversity_3(self):
        self.assertEqual('TTTTT-5', run_unique_filename('TTTTTTTTTTTTTTTTTTTTTTT', 5, 7))

    def test_diversity_4(self):
        self.assertEqual('JJJJJ-1', run_unique_filename('JJJJJJJJJJJJJJJ', 1, 7))

    def test_diversity_5(self):
        self.assertEqual('BBBB-1', run_unique_filename('BBBBBBBBBBBBBBBBBBBBBBBB', 1, 6))

    def test_diversity_6(self):
        self.assertEqual('FFFFFFFFF-10', run_unique_filename('FFFFFFFFFFFFFFFF', 10, 12))

    def test_diversity_7(self):
        self.assertEqual('BBBB.log', run_unique_filename('BBBBBBBBBBBBBBBBBBBBBBBBBBBB.log', 0, 8))

    def test_diversity_8(self):
        self.assertEqual('BBBB.txt-2', run_unique_filename('BBBBBBBBBBBBBBBBBBBBBBBB.txt', 2, 10))

    def test_diversity_9(self):
        self.assertEqual('XXXX.txt-1', run_unique_filename('XXXXXXXXXXXXXXXXXXXXXXXXXX.txt', 1, 10))

    def test_diversity_10(self):
        self.assertEqual('CCCCCCC-5', run_unique_filename('CCCCCCCCCCCCCCCCCCCCCCCC', 5, 9))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('tlqscvxo-10', run_unique_filename('tlqscvxo', 10, 255))

    def test_diversity_2(self):
        self.assertEqual('lirmv-10', run_unique_filename('lirmv', 10, 255))

    def test_diversity_3(self):
        self.assertEqual('dxjpk.png-10', run_unique_filename('dxjpk.png', 10, 255))

    def test_diversity_4(self):
        self.assertEqual('iana-2', run_unique_filename('iana', 2, 255))

    def test_diversity_5(self):
        self.assertEqual('qumtmwge.bar-5', run_unique_filename('qumtmwge.bar', 5, 255))

    def test_diversity_6(self):
        self.assertEqual('wzz.png-10', run_unique_filename('wzz.png', 10, 255))

    def test_diversity_7(self):
        self.assertEqual('rocr.bar-5', run_unique_filename('rocr.bar', 5, 255))

    def test_diversity_8(self):
        self.assertEqual('cxgn-10', run_unique_filename('cxgn', 10, 255))

    def test_diversity_9(self):
        self.assertEqual('zhplvy.txt', run_unique_filename('zhplvy.txt', 0, 255))

    def test_diversity_10(self):
        self.assertEqual('wzvelolk.png-5', run_unique_filename('wzvelolk.png', 5, 255))