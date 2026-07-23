import unittest

# noinspection PyUnresolvedReferences
from scrapy.settings import BaseSettings


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        s = BaseSettings({'TEST_BASE': {1: 2, 2: 844}, 'TEST': BaseSettings({1: 643}, 'default')})
        s['TEST'].set(3, 884, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 2), (2, 844), (3, 884)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_2(self):
        s = BaseSettings({'TEST_BASE': {1: 5, 2: 45}, 'TEST': BaseSettings({1: 208}, 'default')})
        s['TEST'].set(3, 64, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 5), (2, 45), (3, 64)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_3(self):
        s = BaseSettings({'TEST_BASE': {1: 5, 2: 72}, 'TEST': BaseSettings({1: 590}, 'default')})
        s['TEST'].set(3, 542, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 5), (2, 72), (3, 542)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_4(self):
        s = BaseSettings({'TEST_BASE': {1: 1, 2: 405}, 'TEST': BaseSettings({1: 433}, 'default')})
        s['TEST'].set(3, 563, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 1), (2, 405), (3, 563)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_5(self):
        s = BaseSettings({'TEST_BASE': {1: 6, 2: 541}, 'TEST': BaseSettings({1: 199}, 'default')})
        s['TEST'].set(3, 108, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 6), (2, 541), (3, 108)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_6(self):
        s = BaseSettings({'TEST_BASE': {1: 4, 2: 654}, 'TEST': BaseSettings({1: 725}, 'default')})
        s['TEST'].set(3, 944, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 4), (2, 654), (3, 944)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_7(self):
        s = BaseSettings({'TEST_BASE': {1: 9, 2: 285}, 'TEST': BaseSettings({1: 68}, 'default')})
        s['TEST'].set(3, 823, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 9), (2, 285), (3, 823)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_8(self):
        s = BaseSettings({'TEST_BASE': {1: 2, 2: 686}, 'TEST': BaseSettings({1: 603}, 'default')})
        s['TEST'].set(3, 856, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 2), (2, 686), (3, 856)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_9(self):
        s = BaseSettings({'TEST_BASE': {1: 9, 2: 897}, 'TEST': BaseSettings({1: 826}, 'default')})
        s['TEST'].set(3, 970, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 9), (2, 897), (3, 970)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_10(self):
        s = BaseSettings({'TEST_BASE': {1: 8, 2: 432}, 'TEST': BaseSettings({1: 865}, 'default')})
        s['TEST'].set(3, 882, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 8), (2, 432), (3, 882)], sorted(((int(k), int(cs[k])) for k in cs)))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        s = BaseSettings({'TEST_BASE': {1: 9, 2: 104}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 175, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 9), (2, 104), (3, 175)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_2(self):
        s = BaseSettings({'TEST_BASE': {1: 1, 2: 289}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 385, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 1), (2, 289), (3, 385)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_3(self):
        s = BaseSettings({'TEST_BASE': {1: 5, 2: 241}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 549, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 5), (2, 241), (3, 549)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_4(self):
        s = BaseSettings({'TEST_BASE': {1: 8, 2: 387}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 856, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 8), (2, 387), (3, 856)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_5(self):
        s = BaseSettings({'TEST_BASE': {1: 5, 2: 338}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 672, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 5), (2, 338), (3, 672)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_6(self):
        s = BaseSettings({'TEST_BASE': {1: 1, 2: 193}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 342, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 1), (2, 193), (3, 342)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_7(self):
        s = BaseSettings({'TEST_BASE': {1: 9, 2: 221}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 615, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 9), (2, 221), (3, 615)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_8(self):
        s = BaseSettings({'TEST_BASE': {1: 5, 2: 416}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 268, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 5), (2, 416), (3, 268)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_9(self):
        s = BaseSettings({'TEST_BASE': {1: 2, 2: 779}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 46, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 2), (2, 779), (3, 46)], sorted(((int(k), int(cs[k])) for k in cs)))

    def test_diversity_10(self):
        s = BaseSettings({'TEST_BASE': {1: 4, 2: 212}, 'TEST': BaseSettings()})
        s['TEST'].set(3, 335, priority='project')
        cs = s._getcomposite('TEST')
        self.assertEqual([(1, 4), (2, 212), (3, 335)], sorted(((int(k), int(cs[k])) for k in cs)))
