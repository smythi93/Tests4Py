import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import strip_jsonp


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('{"tgyrepbinp":109,"tlthkvsdkm":448}', strip_jsonp('qlbbsqk({"tgyrepbinp":109,"tlthkvsdkm":448})//snoxpn'))

    def test_diversity_2(self):
        self.assertEqual('{"hoyghubth":"lzzloiwf"}', strip_jsonp('smqavqrw({"hoyghubth":"lzzloiwf"})//uaxnqm'))

    def test_diversity_3(self):
        self.assertEqual('{"xgpfcaqkjo":2340}', strip_jsonp('lawwpke({"xgpfcaqkjo":2340})//iyzc'))

    def test_diversity_4(self):
        self.assertEqual('{"rvibkkrl":"njnyoizomw"}', strip_jsonp('xwfq({"rvibkkrl":"njnyoizomw"})//myiceuc'))

    def test_diversity_5(self):
        self.assertEqual('{"luybackk":"jxxmnylf","swusfvzw":"enlpvem"}', strip_jsonp('wxwlpgcpv({"luybackk":"jxxmnylf","swusfvzw":"enlpvem"})//nwvi'))

    def test_diversity_6(self):
        self.assertEqual('{"byaniwd":1934,"myyzgzo":3325}', strip_jsonp('lcrk({"byaniwd":1934,"myyzgzo":3325})//rsh'))

    def test_diversity_7(self):
        self.assertEqual('{"dohilg":6479,"oldid":"fvjgddzwl","iefgjuqhzn":6445}', strip_jsonp('xtvedyrah({"dohilg":6479,"oldid":"fvjgddzwl","iefgjuqhzn":6445})//cisqycamg'))

    def test_diversity_8(self):
        self.assertEqual('{"lctlmlndnz":"xsupai"}', strip_jsonp('esbttpj({"lctlmlndnz":"xsupai"})//awbdv'))

    def test_diversity_9(self):
        self.assertEqual('{"rwjucgg":5813,"pcu":"plhiptseo"}', strip_jsonp('ucwtvj({"rwjucgg":5813,"pcu":"plhiptseo"})//pcwhwlyn'))

    def test_diversity_10(self):
        self.assertEqual('{"yhwkxgl":3099,"vcspprj":"jji"}', strip_jsonp('tuzklv({"yhwkxgl":3099,"vcspprj":"jji"})//jph'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('{"rgoe":244,"tujkwie":4663}', strip_jsonp('lazacy({"rgoe":244,"tujkwie":4663});'))

    def test_diversity_2(self):
        self.assertEqual('{"wcdau":"yrpince","ipnc":"kaxoqym","oimgzdkuvo":"yhrxu"}', strip_jsonp('nthwnkyh({"wcdau":"yrpince","ipnc":"kaxoqym","oimgzdkuvo":"yhrxu"});'))

    def test_diversity_3(self):
        self.assertEqual('{"pqkmb":5687,"vekwrzdrfk":"otnzgo","laoufw":4502}', strip_jsonp('qbqvihjdp({"pqkmb":5687,"vekwrzdrfk":"otnzgo","laoufw":4502});'))

    def test_diversity_4(self):
        self.assertEqual('{"iivdmjjsud":"sps","rzfyzgbhgq":4205,"zhinpnebcw":"ovmondrkz"}', strip_jsonp('ajda({"iivdmjjsud":"sps","rzfyzgbhgq":4205,"zhinpnebcw":"ovmondrkz"})'))

    def test_diversity_5(self):
        self.assertEqual('{"itxfhwgedn":8721,"oavs":7019,"zlbdr":4786}', strip_jsonp('oqcp({"itxfhwgedn":8721,"oavs":7019,"zlbdr":4786})'))

    def test_diversity_6(self):
        self.assertEqual('{"hupcqf":"rutg","khtq":"jcbymk"}', strip_jsonp('rod({"hupcqf":"rutg","khtq":"jcbymk"})'))

    def test_diversity_7(self):
        self.assertEqual('{"cgwk":4363,"uuhudebqv":3048}', strip_jsonp('xuheifnug({"cgwk":4363,"uuhudebqv":3048});'))

    def test_diversity_8(self):
        self.assertEqual('{"lswwurz":5484,"nlapy":3979}', strip_jsonp('jxcavxxr({"lswwurz":5484,"nlapy":3979});'))

    def test_diversity_9(self):
        self.assertEqual('{"nqqr":964,"yznajbm":8842,"abtjfyi":4551}', strip_jsonp('mbsyciophy({"nqqr":964,"yznajbm":8842,"abtjfyi":4551});'))

    def test_diversity_10(self):
        self.assertEqual('{"mwuy":5454}', strip_jsonp('valsb({"mwuy":5454});'))
