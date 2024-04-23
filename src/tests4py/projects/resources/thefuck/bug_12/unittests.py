import unittest
from thefuck.rules.no_command import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('gu run CNaYQBCSymsiX.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('gu run yupziuoo.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('gu run ynvDa.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('gu run EbOAupaL.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('gu run KQhVZ.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('gu run kjQPDGL.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('gu run KHmmVxKERzQGpc.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('gu run ARSGpThVBQO.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('gu run tBkitY.go', '', 'gu: not found, maybe you meant "go"')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('gu run kaTrEIilpqTNb.go', '', 'gu: not found, maybe you meant "go"')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('got commit -m IEogeEW', '', 'got: not found, maybe you meant "git"')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('vom CfzzGQqxelbKU.py', '', 'vom: not found, maybe you meant "vim"')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('vom aabaJUO.py', '', 'vom: not found, maybe you meant "vim"')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('got commit -m oVUZgKT', '', 'got: not found, maybe you meant "git"')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('vom cSsmtRPwn.py', '', 'vom: not found, maybe you meant "vim"')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('vom INxwxW.py', '', 'vom: not found, maybe you meant "vim"')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('got commit -m jBgySrnKjrlVUN', '', 'got: not found, maybe you meant "git"')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('vom RlhNFbBtbO.py', '', 'vom: not found, maybe you meant "vim"')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('vom MoAwT.py', '', 'vom: not found, maybe you meant "vim"')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('sudo fucck OAoafNFNHLVCtGK', '', 'fuckk: not found, maybe you meant "fsck"')))
