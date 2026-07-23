import unittest
import requests
from httpie.models import HTTPRequest

def run_host_count(url, name, value):
    headers = {}
    if name != '-':
        headers[name] = value
    req = requests.Request('GET', url, headers=headers).prepare()
    return HTTPRequest(req).headers.lower().count('host:')

class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(1, run_host_count('http://133.4.165.171/mgalsv', 'HOsT', 'service64.io'))

    def test_diversity_2(self):
        self.assertEqual(1, run_host_count('http://185.100.182.209/vkkdw', 'HoST', 'api738.net'))

    def test_diversity_3(self):
        self.assertEqual(1, run_host_count('http://196.136.151.198/yzt', 'host', 'httpbin522.net'))

    def test_diversity_4(self):
        self.assertEqual(1, run_host_count('http://246.109.91.107/tdi', 'HOST', 'service711.net'))

    def test_diversity_5(self):
        self.assertEqual(1, run_host_count('http://17.124.60.181/xejyxbaf', 'HOST', 'test35.com'))

    def test_diversity_6(self):
        self.assertEqual(1, run_host_count('http://249.209.53.244/grdgf', 'HOST', 'service536.io'))

    def test_diversity_7(self):
        self.assertEqual(1, run_host_count('http://171.198.137.81/bkq', 'hOst', 'server959.net'))

    def test_diversity_8(self):
        self.assertEqual(1, run_host_count('http://169.160.71.171/tiebhxc', 'hoSt', 'server538.com'))

    def test_diversity_9(self):
        self.assertEqual(1, run_host_count('http://221.212.112.173/lsqcozcz', 'HOST', 'example943.com'))

    def test_diversity_10(self):
        self.assertEqual(1, run_host_count('http://204.120.90.165/mbm', 'hosT', 'api808.io'))

class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(1, run_host_count('http://107.24.161.249/pdy', '-', 'service751.io'))

    def test_diversity_2(self):
        self.assertEqual(1, run_host_count('http://156.196.157.49/yahh', '-', 'server379.net'))

    def test_diversity_3(self):
        self.assertEqual(1, run_host_count('http://137.133.183.12/bgdbujkv', '-', 'test100.io'))

    def test_diversity_4(self):
        self.assertEqual(1, run_host_count('http://84.145.190.197/mqho', 'Host', 'server859.io'))

    def test_diversity_5(self):
        self.assertEqual(1, run_host_count('http://196.66.194.66/cajaze', 'Host', 'test419.io'))

    def test_diversity_6(self):
        self.assertEqual(1, run_host_count('http://17.72.127.184/vtnosv', 'Host', 'example584.com'))

    def test_diversity_7(self):
        self.assertEqual(1, run_host_count('http://89.7.181.19/cidze', 'Host', 'example241.io'))

    def test_diversity_8(self):
        self.assertEqual(1, run_host_count('http://252.80.74.192/pbxk', '-', 'example929.com'))

    def test_diversity_9(self):
        self.assertEqual(1, run_host_count('http://69.25.234.63/jmnynh', '-', 'api791.org'))

    def test_diversity_10(self):
        self.assertEqual(1, run_host_count('http://13.241.246.83/iihthlxl', '-', 'example618.net'))