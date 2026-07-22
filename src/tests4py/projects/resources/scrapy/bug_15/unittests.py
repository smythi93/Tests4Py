import unittest

from scrapy.utils.url import canonicalize_url


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://www.vuykmxqzjngsmnsbdmfjsvumgmgwtrdjrxaqswjsexzmnbmvplpogerxdgpwqtrcixm.com/wwgvp', canonicalize_url('http://www.vuykmxqzjngsmnsbdmfjsvumgmgwtrdjrxaqswjsexzmnbmvplpogerxdgpwqtrcixm.com/wwgvp'))

    def test_diversity_2(self):
        self.assertEqual('http://www.tivdtdzvcmhzxweberpduqbozciaotiyrkhwphotgaogxnxujuajcncstpxbxmyjydqjkn.com/ecmt', canonicalize_url('http://www.tivdtdzvcmhzxweberpduqbozciaotiyrkhwphotgaogxnxujuajcncstpxbxmyjydqjkn.com/ecmt'))

    def test_diversity_3(self):
        self.assertEqual('http://www.vkqryyvwczynwylwtjkqcsbzcooxekroifghsabrjcfebttqmposncpziodxkxyronfmndjltmxqhitvmswhd.com/moess/qqbji', canonicalize_url('http://www.vkqryyvwczynwylwtjkqcsbzcooxekroifghsabrjcfebttqmposncpziodxkxyronfmndjltmxqhitvmswhd.com/moess/qqbji'))

    def test_diversity_4(self):
        self.assertEqual('http://.cqxrnitm.com/bcn/aanbj', canonicalize_url('http://.cqxrnitm.com/bcn/aanbj'))

    def test_diversity_5(self):
        self.assertEqual('http://www.otprqacgfskwkxqpfswqspiyfgiqzcqtspdwjnfakpfngrnywzpwgqqdocxwfpeapmvbloiqceqirzwyxebyc.com/pmdsj', canonicalize_url('http://www.otprqacgfskwkxqpfswqspiyfgiqzcqtspdwjnfakpfngrnywzpwgqqdocxwfpeapmvbloiqceqirzwyxebyc.com/pmdsj'))

    def test_diversity_6(self):
        self.assertEqual('http://www.tvbeeztwnlcerzjftbbltcqlokbivksfvybfruyqasztkecdvelzrcybdncstvknijrdysynusbchyslxtehbcd.com/lcvfqu/qwkmz/mfwp', canonicalize_url('http://www.tvbeeztwnlcerzjftbbltcqlokbivksfvybfruyqasztkecdvelzrcybdncstvknijrdysynusbchyslxtehbcd.com/lcvfqu/qwkmz/mfwp'))

    def test_diversity_7(self):
        self.assertEqual('http://www.xktygijwluhqaiybvwwzjembesyibhcxpureyzrfxwpzrxzljkobtrgtrsdbvbepnlzxmnaetotpagrvaccfbqjn.com/rlg/urxw', canonicalize_url('http://www.xktygijwluhqaiybvwwzjembesyibhcxpureyzrfxwpzrxzljkobtrgtrsdbvbepnlzxmnaetotpagrvaccfbqjn.com/rlg/urxw'))

    def test_diversity_8(self):
        self.assertEqual('http://.biinblk.com/zpndme/qfw', canonicalize_url('http://.biinblk.com/zpndme/qfw'))

    def test_diversity_9(self):
        self.assertEqual('http://www.srpblvvvhzkicypqmjkcrtpydyizqxtfgzcfiicmnatthpivistcnnfttgaitqam.com/gymcse/zezqt', canonicalize_url('http://www.srpblvvvhzkicypqmjkcrtpydyizqxtfgzcfiicmnatthpivistcnnfttgaitqam.com/gymcse/zezqt'))

    def test_diversity_10(self):
        self.assertEqual('http://www.jivdzkzwhjjwkvydbtaymaintulromzyflvfpwfrlafhecaxuiinzrqsasgvqefbrsla.com/anhcy', canonicalize_url('http://www.jivdzkzwhjjwkvydbtaymaintulromzyflvfpwfrlafhecaxuiinzrqsasgvqefbrsla.com/anhcy'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('http://nveveq.org/fvlz/ndphxc/kesoh', canonicalize_url('http://nveveq.org/fvlz/ndphxc/kesoh'))

    def test_diversity_2(self):
        self.assertEqual('http://rgmophld.io/syx/utjfh/vq', canonicalize_url('http://rgmophld.io/syx/utjfh/vq'))

    def test_diversity_3(self):
        self.assertEqual('http://zyucqnrk.org/vxozsh/rgjjt', canonicalize_url('http://zyucqnrk.org/vxozsh/rgjjt'))

    def test_diversity_4(self):
        self.assertEqual('http://lgailld.org/vrz/we', canonicalize_url('http://lgailld.org/vrz/we'))

    def test_diversity_5(self):
        self.assertEqual('http://yfyri.io/wmb', canonicalize_url('http://yfyri.io/wmb'))

    def test_diversity_6(self):
        self.assertEqual('http://apnu.net/lcb', canonicalize_url('http://apnu.net/lcb'))

    def test_diversity_7(self):
        self.assertEqual('http://ocbvhu.org/prkmkj', canonicalize_url('http://ocbvhu.org/prkmkj'))

    def test_diversity_8(self):
        self.assertEqual('http://hct.net/evp/fon/alkq', canonicalize_url('http://hct.net/evp/fon/alkq'))

    def test_diversity_9(self):
        self.assertEqual('http://vyl.net/ue', canonicalize_url('http://vyl.net/ue'))

    def test_diversity_10(self):
        self.assertEqual('http://amrppux.com/mn/mknta/pgxdcr', canonicalize_url('http://amrppux.com/mn/mknta/pgxdcr'))
