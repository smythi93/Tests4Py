import unittest

def _t4p_text_to_word_sequence(split, words):
    import os
    import importlib.util
    path = os.path.join(os.getcwd(), 'keras', 'preprocessing', 'text.py')
    spec = importlib.util.spec_from_file_location('t4p_text', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    text = split.join(words)
    return module.text_to_word_sequence(text, split=split)


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(['cgazdve', 'ntt', 'gswevu'], _t4p_text_to_word_sequence('967', ['cgazdve', 'ntt', 'gswevu']))

    def test_diversity_2(self):
        self.assertEqual(['tiuaiuo', 'xu', 'ki', 'xzr'], _t4p_text_to_word_sequence('793', ['tiuaiuo', 'xu', 'ki', 'xzr']))

    def test_diversity_3(self):
        self.assertEqual(['cfpbid', 'hmru', 'lqcln', 'ywlrb', 'ikqpjz'], _t4p_text_to_word_sequence('62', ['cfpbid', 'hmru', 'lqcln', 'ywlrb', 'ikqpjz']))

    def test_diversity_4(self):
        self.assertEqual(['yxbnh', 'ksksun'], _t4p_text_to_word_sequence('124', ['yxbnh', 'ksksun']))

    def test_diversity_5(self):
        self.assertEqual(['ot', 'gcjscbj', 'ts', 'hj', 'jaedbr'], _t4p_text_to_word_sequence('027', ['ot', 'gcjscbj', 'ts', 'hj', 'jaedbr']))

    def test_diversity_6(self):
        self.assertEqual(['yk', 'qqrm'], _t4p_text_to_word_sequence('031', ['yk', 'qqrm']))

    def test_diversity_7(self):
        self.assertEqual(['rf', 'bbpgnpz', 'zjw', 'eya', 'oh'], _t4p_text_to_word_sequence('10', ['rf', 'bbpgnpz', 'zjw', 'eya', 'oh']))

    def test_diversity_8(self):
        self.assertEqual(['knjiz', 'qupnli', 'gd', 'ry', 'scvcs'], _t4p_text_to_word_sequence('067', ['knjiz', 'qupnli', 'gd', 'ry', 'scvcs']))

    def test_diversity_9(self):
        self.assertEqual(['yop', 'ubal', 'pin'], _t4p_text_to_word_sequence('663', ['yop', 'ubal', 'pin']))

    def test_diversity_10(self):
        self.assertEqual(['gbbnqcm', 'ebeuws', 'baaoup', 'hmgbx', 'rm'], _t4p_text_to_word_sequence('580', ['gbbnqcm', 'ebeuws', 'baaoup', 'hmgbx', 'rm']))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(['vah', 'clx', 'dfqlvf', 'sznj'], _t4p_text_to_word_sequence('9', ['vah', 'clx', 'dfqlvf', 'sznj']))

    def test_diversity_2(self):
        self.assertEqual(['fbaze', 'fmfla', 'mzmuts'], _t4p_text_to_word_sequence('4', ['fbaze', 'fmfla', 'mzmuts']))

    def test_diversity_3(self):
        self.assertEqual(['bi', 'hkc'], _t4p_text_to_word_sequence('5', ['bi', 'hkc']))

    def test_diversity_4(self):
        self.assertEqual(['zhrfq', 'kty', 'hdmhafa', 'jkdru'], _t4p_text_to_word_sequence('8', ['zhrfq', 'kty', 'hdmhafa', 'jkdru']))

    def test_diversity_5(self):
        self.assertEqual(['ppzv', 'rtkxmgd', 'wrrt', 'ybf', 'jozqww'], _t4p_text_to_word_sequence('6', ['ppzv', 'rtkxmgd', 'wrrt', 'ybf', 'jozqww']))

    def test_diversity_6(self):
        self.assertEqual(['bjpch', 'ze'], _t4p_text_to_word_sequence('1', ['bjpch', 'ze']))

    def test_diversity_7(self):
        self.assertEqual(['mfn', 'im', 'krl'], _t4p_text_to_word_sequence('6', ['mfn', 'im', 'krl']))

    def test_diversity_8(self):
        self.assertEqual(['xayldxg', 'ovql'], _t4p_text_to_word_sequence('2', ['xayldxg', 'ovql']))

    def test_diversity_9(self):
        self.assertEqual(['fehap', 'mi'], _t4p_text_to_word_sequence('9', ['fehap', 'mi']))

    def test_diversity_10(self):
        self.assertEqual(['unnxvxs', 'luhfzex'], _t4p_text_to_word_sequence('9', ['unnxvxs', 'luhfzex']))
