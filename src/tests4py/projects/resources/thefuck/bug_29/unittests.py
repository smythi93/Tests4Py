import unittest
from thefuck.types import Settings


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        settings = Settings({'XzfAQWMGZsRno, VxpzWICmx'})
        new_settings = settings.update()
        self.assertEqual({'XzfAQWMGZsRno, VxpzWICmx'}, new_settings)
    def test_diversity_2(self):
        settings = Settings({'TNcSbgpTHDaP, CmyiNBnFGYpN'})
        new_settings = settings.update()
        self.assertEqual({'TNcSbgpTHDaP, CmyiNBnFGYpN'}, new_settings)
    def test_diversity_3(self):
        settings = Settings({'anhzcgMTXGlVGl, zuqmADw'})
        new_settings = settings.update()
        self.assertEqual({'anhzcgMTXGlVGl, zuqmADw'}, new_settings)

    def test_diversity_4(self):
        settings = Settings({'ybrClZAWaGol, LholEhnooW'})
        new_settings = settings.update()
        self.assertEqual({'ybrClZAWaGol, LholEhnooW'}, new_settings)
    def test_diversity_5(self):
        settings = Settings({'RgiNdUF, cOaOP'})
        new_settings = settings.update()
        self.assertEqual({'RgiNdUF, cOaOP'}, new_settings)
    def test_diversity_6(self):
        settings = Settings({'fxSOvW, rbkSGedKTtAWNCB'})
        new_settings = settings.update()
        self.assertEqual({'fxSOvW, rbkSGedKTtAWNCB'}, new_settings)
    def test_diversity_7(self):
        settings = Settings({'lnzMcGuixAG, lDDNDxIvbJqkJP'})
        new_settings = settings.update()
        self.assertEqual({'lnzMcGuixAG, lDDNDxIvbJqkJP'}, new_settings)

    def test_diversity_8(self):
        settings = Settings({'ILrSPfCSzxzoV, FUqgGFUGxNwd'})
        new_settings = settings.update()
        self.assertEqual({'ILrSPfCSzxzoV, FUqgGFUGxNwd'}, new_settings)

    def test_diversity_9(self):
        settings = Settings({'QvalBsqqAzZu, FBKRDZghW'})
        new_settings = settings.update()
        self.assertEqual({'QvalBsqqAzZu, FBKRDZghW'}, new_settings)
    def test_diversity_10(self):
        settings = Settings({'HbrpoCOeh, ejsgcJ'})
        new_settings = settings.update()
        self.assertEqual({'HbrpoCOeh, ejsgcJ'}, new_settings)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        settings = Settings({'DvlxQtyDpA': 'zsNolylewSFnQz'})
        new_settings = settings.update()
        self.assertEqual({'DvlxQtyDpA': 'zsNolylewSFnQz'}, new_settings)
    def test_diversity_2(self):
        settings = Settings({'LEbguvrGHpFvqL': 'PNkCXfCQCBS'})
        new_settings = settings.update()
        self.assertEqual({'LEbguvrGHpFvqL': 'PNkCXfCQCBS'}, new_settings)
    def test_diversity_3(self):
        settings = Settings({'HlcBdEQeqjPhk': 'jjnuOxfCJowceio'})
        new_settings = settings.update()
        self.assertEqual({'HlcBdEQeqjPhk': 'jjnuOxfCJowceio'}, new_settings)
    def test_diversity_4(self):
        settings = Settings({'auqSOiuULLXR': 'kZZcpdxSyLnHeNT'})
        new_settings = settings.update()
        self.assertEqual({'auqSOiuULLXR': 'kZZcpdxSyLnHeNT'}, new_settings)
    def test_diversity_5(self):
        settings = Settings({'LQQQVkn': 'iynqcuFUfMinD'})
        new_settings = settings.update()
        self.assertEqual({'LQQQVkn': 'iynqcuFUfMinD'}, new_settings)

    def test_diversity_6(self):
        settings = Settings({'erpmZTeoIiKS': 'eeuRLagy'})
        new_settings = settings.update()
        self.assertEqual({'erpmZTeoIiKS': 'eeuRLagy'}, new_settings)

    def test_diversity_7(self):
        settings = Settings({'drCrgcmKIqTgG': 'zhkEhsizUbVuZtV'})
        new_settings = settings.update()
        self.assertEqual({'drCrgcmKIqTgG': 'zhkEhsizUbVuZtV'}, new_settings)

    def test_diversity_8(self):
        settings = Settings({'xITcAGpzDkPpl': 'BmpimsKjzVMtSF'})
        new_settings = settings.update()
        self.assertEqual({'xITcAGpzDkPpl': 'BmpimsKjzVMtSF'}, new_settings)

    def test_diversity_9(self):
        settings = Settings({'pbAVAuYmryZgb': 'BEdsmVdtVkD'})
        new_settings = settings.update()
        self.assertEqual({'pbAVAuYmryZgb': 'BEdsmVdtVkD'}, new_settings)

    def test_diversity_10(self):
        settings = Settings({'BKTCcf': 'QlqEFR'})
        new_settings = settings.update()
        self.assertEqual({'BKTCcf': 'QlqEFR'}, new_settings)