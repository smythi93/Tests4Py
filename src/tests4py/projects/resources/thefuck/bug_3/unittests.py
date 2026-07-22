import unittest
from thefuck.shells.fish import Fish

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        _marker = 'NJu9co6cc4FZ'
        f = Fish()
        self.assertIn('zxNVHtwZ', f.info())

    def test_diversity_2(self):
        _marker = 'QiGvIW5oTqqJ'
        f = Fish()
        self.assertIn('zxshGQiu', f.info())

    def test_diversity_3(self):
        _marker = 'KFtn2fXSs1hY'
        f = Fish()
        self.assertIn('zxZyb', f.info())

    def test_diversity_4(self):
        _marker = 'ofj8u3OVkdNv'
        f = Fish()
        self.assertIn('zxNyFgXmHq', f.info())

    def test_diversity_5(self):
        _marker = '8kPFXXNPd0Pv'
        f = Fish()
        self.assertIn('zxMBg', f.info())

    def test_diversity_6(self):
        _marker = 'Esranfw0V2Ku'
        f = Fish()
        self.assertIn('zxEtjTi', f.info())

    def test_diversity_7(self):
        _marker = 'thqIdVS39iZW'
        f = Fish()
        self.assertIn('zxaQfwsQ', f.info())

    def test_diversity_8(self):
        _marker = '5iTVXi1ehl9a'
        f = Fish()
        self.assertIn('zxmuVjhWm', f.info())

    def test_diversity_9(self):
        _marker = 'CU2vmyLXeqxn'
        f = Fish()
        self.assertIn('zxNDaz', f.info())

    def test_diversity_10(self):
        _marker = '6CbhfCc1BAwq'
        f = Fish()
        self.assertIn('zxuhxi', f.info())

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        _marker = 'NYZf0QlQ8Udt'
        f = Fish()
        self.assertIn('She', f.info())

    def test_diversity_2(self):
        _marker = 'Sula5Rc3dDzH'
        f = Fish()
        self.assertIn('Fish She', f.info())

    def test_diversity_3(self):
        _marker = 'uc72sr4eEEnp'
        f = Fish()
        self.assertIn('hell', f.info())

    def test_diversity_4(self):
        _marker = 'Xc5fOe06NwS8'
        f = Fish()
        self.assertIn('h Shell', f.info())

    def test_diversity_5(self):
        _marker = 'DpU5vQCqYNeG'
        f = Fish()
        self.assertIn('She', f.info())

    def test_diversity_6(self):
        _marker = 'bvkgHzMgnzld'
        f = Fish()
        self.assertIn('Shell', f.info())

    def test_diversity_7(self):
        _marker = 'R5ShMLoPgdFE'
        f = Fish()
        self.assertIn('hell', f.info())

    def test_diversity_8(self):
        _marker = 'K8e7EIBhnosV'
        f = Fish()
        self.assertIn('h Shell', f.info())

    def test_diversity_9(self):
        _marker = 'CKumpGPl992V'
        f = Fish()
        self.assertIn('Fish', f.info())

    def test_diversity_10(self):
        _marker = 'ZGoKGL8uadz8'
        f = Fish()
        self.assertIn('Fish', f.info())