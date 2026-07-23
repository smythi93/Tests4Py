import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('kmogc', {'kmogc': False}))

    def test_diversity_2(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('cmhobtd', {'cmhobtd': False}))

    def test_diversity_3(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('wuyz', {'wuyz': False}))

    def test_diversity_4(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('ppts', {'ppts': False}))

    def test_diversity_5(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('!jkx', {'jkx': False}))

    def test_diversity_6(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('!sun', {'sun': False}))

    def test_diversity_7(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('qnu', {'qnu': False}))

    def test_diversity_8(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('!aunvma', {'aunvma': False}))

    def test_diversity_9(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('shli', {'shli': False}))

    def test_diversity_10(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('mjpuaczf', {'mjpuaczf': False}))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('!uyxcink', {'uyxcink': True}))

    def test_diversity_2(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('zudaww', {'zudaww': True}))

    def test_diversity_3(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('!pjsl', {'pjsl': True}))

    def test_diversity_4(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('eyzpr>487', {'eyzpr': 974}))

    def test_diversity_5(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('cijlscpp', {'cijlscpp': True}))

    def test_diversity_6(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('dqptli>343', {'dqptli': 687}))

    def test_diversity_7(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('cer>100', {'cer': 201}))

    def test_diversity_8(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('!ljmcklpa', {'ljmcklpa': True}))

    def test_diversity_9(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str('!wrm', {'wrm': True}))

    def test_diversity_10(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('gvoav>61', {'gvoav': 123}))
