import unittest

# noinspection PyUnresolvedReferences
try:
    from youtube_dl.utils import fix_xml_ampersands
except ImportError:
    from youtube_dl.utils import fix_xml_all_ampersand as fix_xml_ampersands


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('zr &gt; jxxvyg', fix_xml_ampersands('zr &gt; jxxvyg'))

    def test_diversity_2(self):
        self.assertEqual('xfnqv &#65; ioemyy', fix_xml_ampersands('xfnqv &#65; ioemyy'))

    def test_diversity_3(self):
        self.assertEqual('wqb &apos; rxt', fix_xml_ampersands('wqb &apos; rxt'))

    def test_diversity_4(self):
        self.assertEqual('wison &apos; bbjvk', fix_xml_ampersands('wison &apos; bbjvk'))

    def test_diversity_5(self):
        self.assertEqual('pb &lt; ujyrjm', fix_xml_ampersands('pb &lt; ujyrjm'))

    def test_diversity_6(self):
        self.assertEqual('au &#x41; limt', fix_xml_ampersands('au &#x41; limt'))

    def test_diversity_7(self):
        self.assertEqual('suw &gt; jeqffz', fix_xml_ampersands('suw &gt; jeqffz'))

    def test_diversity_8(self):
        self.assertEqual('odzrgt &apos; jshkj', fix_xml_ampersands('odzrgt &apos; jshkj'))

    def test_diversity_9(self):
        self.assertEqual('aizd &apos; wn', fix_xml_ampersands('aizd &apos; wn'))

    def test_diversity_10(self):
        self.assertEqual('jehvhs &lt; zeazs', fix_xml_ampersands('jehvhs &lt; zeazs'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('hweyp &amp; ntpvn', fix_xml_ampersands('hweyp & ntpvn'))

    def test_diversity_2(self):
        self.assertEqual('qsnk dumodu', fix_xml_ampersands('qsnk dumodu'))

    def test_diversity_3(self):
        self.assertEqual('iy &amp; joemyy', fix_xml_ampersands('iy & joemyy'))

    def test_diversity_4(self):
        self.assertEqual('xcvmb &amp; pij', fix_xml_ampersands('xcvmb & pij'))

    def test_diversity_5(self):
        self.assertEqual('ger cbrliz', fix_xml_ampersands('ger cbrliz'))

    def test_diversity_6(self):
        self.assertEqual('xezapx ypex', fix_xml_ampersands('xezapx ypex'))

    def test_diversity_7(self):
        self.assertEqual('pkwnv &amp; krmgh', fix_xml_ampersands('pkwnv & krmgh'))

    def test_diversity_8(self):
        self.assertEqual('egyxj fxakbx', fix_xml_ampersands('egyxj fxakbx'))

    def test_diversity_9(self):
        self.assertEqual('vjx &amp; uysvi', fix_xml_ampersands('vjx & uysvi'))

    def test_diversity_10(self):
        self.assertEqual('lrbuav dje', fix_xml_ampersands('lrbuav dje'))
