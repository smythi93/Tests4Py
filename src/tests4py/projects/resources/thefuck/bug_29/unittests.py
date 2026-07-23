import unittest
from thefuck.types import Settings


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('dnjzyez', Settings({'ubogcrkgs': 'dnjzyez'}).update(**{'ubogcrkgs': 'ujzzyzux'})['ubogcrkgs'])

    def test_diversity_2(self):
        self.assertEqual('zgxthrzgwi', Settings({'lkwtcozzi': 'zgxthrzgwi'}).update(**{'lkwtcozzi': 'hmbxmqhjx'})['lkwtcozzi'])

    def test_diversity_3(self):
        self.assertEqual('dmohflhdh', Settings({'gihzekpvb': 'dmohflhdh'}).update(**{'gihzekpvb': 'hixjukx'})['gihzekpvb'])

    def test_diversity_4(self):
        self.assertEqual('uibcunrh', Settings({'yyyes': 'uibcunrh'}).update(**{'yyyes': 'ptetlrrkssx'})['yyyes'])

    def test_diversity_5(self):
        self.assertEqual('emypbpqo', Settings({'qdezhtmb': 'emypbpqo'}).update(**{'qdezhtmb': 'ezndfzdyjzx'})['qdezhtmb'])

    def test_diversity_6(self):
        self.assertEqual('phvkdihx', Settings({'areoybqhg': 'phvkdihx'}).update(**{'areoybqhg': 'lqggvx'})['areoybqhg'])

    def test_diversity_7(self):
        self.assertEqual('kwwtclb', Settings({'alwrajnnhe': 'kwwtclb'}).update(**{'alwrajnnhe': 'qjbzpwrx'})['alwrajnnhe'])

    def test_diversity_8(self):
        self.assertEqual('vpxgdrqm', Settings({'mbddhpzysz': 'vpxgdrqm'}).update(**{'mbddhpzysz': 'iqzlfastx'})['mbddhpzysz'])

    def test_diversity_9(self):
        self.assertEqual('guwwagss', Settings({'hjgzjchxxv': 'guwwagss'}).update(**{'hjgzjchxxv': 'vcogxkbiux'})['hjgzjchxxv'])

    def test_diversity_10(self):
        self.assertEqual('ydxrn', Settings({'brtbetubq': 'ydxrn'}).update(**{'brtbetubq': 'zynnitmggxx'})['brtbetubq'])


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('zvwbpdxk', Settings({'tuvqttelsb': 'zvwbpdxk'}).update(**{'tuvqttelsb': 'zvwbpdxk'})['tuvqttelsb'])

    def test_diversity_2(self):
        self.assertEqual('txbxl', Settings({'nnohs': 'txbxl'}).update(**{'nnohs': 'txbxl'})['nnohs'])

    def test_diversity_3(self):
        self.assertEqual('rxprfrswd', Settings({'zngnwjkmk': 'rxprfrswd'}).update(**{'zngnwjkmk': 'rxprfrswd'})['zngnwjkmk'])

    def test_diversity_4(self):
        self.assertEqual('kirqg', Settings({'jitgvfeu': 'kirqg'}).update(**{'jitgvfeu': 'kirqg'})['jitgvfeu'])

    def test_diversity_5(self):
        self.assertEqual('ilshvwckq', Settings({'ssxtwexf': 'ilshvwckq'}).update(**{'ssxtwexf': 'ilshvwckq'})['ssxtwexf'])

    def test_diversity_6(self):
        self.assertEqual('qpgkedcsse', Settings({'pokfebf': 'qpgkedcsse'}).update(**{'pokfebf': 'qpgkedcsse'})['pokfebf'])

    def test_diversity_7(self):
        self.assertEqual('cuhssxzsi', Settings({'xgfjv': 'cuhssxzsi'}).update(**{'xgfjv': 'cuhssxzsi'})['xgfjv'])

    def test_diversity_8(self):
        self.assertEqual('wwwesuhb', Settings({'yidfixc': 'wwwesuhb'}).update(**{'yidfixc': 'wwwesuhb'})['yidfixc'])

    def test_diversity_9(self):
        self.assertEqual('kndcxrsvml', Settings({'cxazil': 'kndcxrsvml'}).update(**{'cxazil': 'kndcxrsvml'})['cxazil'])

    def test_diversity_10(self):
        self.assertEqual('hbzoyb', Settings({'lsfti': 'hbzoyb'}).update(**{'lsfti': 'hbzoyb'})['lsfti'])
