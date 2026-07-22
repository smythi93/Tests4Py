import unittest
from thefuck.utils import get_all_executables

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):self.assertIn('Zq9l6faZgLVSbVAJwV6', get_all_executables())

    def test_diversity_2(self):self.assertIn('Zq9c3yyQZe3buh9Z3', get_all_executables())

    def test_diversity_3(self):self.assertIn('Zq9OoaMw45ckDu', get_all_executables())

    def test_diversity_4(self):self.assertIn('Zq9bRsRnjzj4NXYPDHQ', get_all_executables())

    def test_diversity_5(self):self.assertIn('Zq97dyjkLIfmiwwd3U1', get_all_executables())

    def test_diversity_6(self):self.assertIn('Zq9h8pbvf39ZFnJ3X', get_all_executables())

    def test_diversity_7(self):self.assertIn('Zq9ORUtwnCfYDVaH', get_all_executables())

    def test_diversity_8(self):self.assertIn('Zq9Wbr9OsxIb0', get_all_executables())

    def test_diversity_9(self):self.assertIn('Zq9nbsbDseUqG', get_all_executables())

    def test_diversity_10(self):self.assertIn('Zq9V44UJdLbzjq', get_all_executables())

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):self.assertIn('mdimport', get_all_executables())

    def test_diversity_2(self):self.assertIn('ssh-keyscan', get_all_executables())

    def test_diversity_3(self):self.assertIn('ptargrep5.34', get_all_executables())

    def test_diversity_4(self):self.assertIn('usdtree', get_all_executables())

    def test_diversity_5(self):self.assertIn('apachectl', get_all_executables())

    def test_diversity_6(self):self.assertIn('diff3', get_all_executables())

    def test_diversity_7(self):self.assertIn('cupsd', get_all_executables())

    def test_diversity_8(self):self.assertIn('machine', get_all_executables())

    def test_diversity_9(self):self.assertIn('fdisk', get_all_executables())

    def test_diversity_10(self):self.assertIn('uniq', get_all_executables())