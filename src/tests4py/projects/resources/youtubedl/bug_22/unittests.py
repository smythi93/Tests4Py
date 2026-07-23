import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str("wgnk='nyli'", {'wgnk': 'nyli'}))

    def test_diversity_2(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str("ykwxon='qorn'", {'ykwxon': 'qorn'}))

    def test_diversity_3(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str("mojskhao!='vyushf'", {'mojskhao': 'vyushf'}))

    def test_diversity_4(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str("qye='srzy'", {'qye': 'srzy'}))

    def test_diversity_5(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str("oprazwj!='gsbh'", {'oprazwj': 'qscc wngb'}))

    def test_diversity_6(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str("wcjkaigv!='tcgxk kgmc'", {'wcjkaigv': 'euyllx uaibv'}))

    def test_diversity_7(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str("rod!='juv'", {'rod': 'juv'}))

    def test_diversity_8(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str("bkscxnp!='npfy pql'", {'bkscxnp': 'npfy pql'}))

    def test_diversity_9(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str("bhxxce!='sshuj xtyw'", {'bhxxce': 'elz'}))

    def test_diversity_10(self):
        from youtube_dl.utils import match_str
        self.assertEqual(False, match_str("fwwfejv!='kavshn'", {'fwwfejv': 'kavshn'}))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('yoonsyb=79878', {'yoonsyb': '79878'}))

    def test_diversity_2(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('cndkkxqr=89859', {'cndkkxqr': 89859}))

    def test_diversity_3(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('msgovviq=and', {'msgovviq': 'and'}))

    def test_diversity_4(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('osikr=26605', {'osikr': 26605}))

    def test_diversity_5(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('ikkt=zzf', {'ikkt': 'zzf'}))

    def test_diversity_6(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('oozwjvx=nian', {'oozwjvx': 'nian'}))

    def test_diversity_7(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('odsrllrg=87754', {'odsrllrg': 87754}))

    def test_diversity_8(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('gahsw=68330', {'gahsw': '68330'}))

    def test_diversity_9(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('kionc=80739', {'kionc': '80739'}))

    def test_diversity_10(self):
        from youtube_dl.utils import match_str
        self.assertEqual(True, match_str('ldb=rdq', {'ldb': 'rdq'}))
