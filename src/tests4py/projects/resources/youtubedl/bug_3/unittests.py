import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unescapeHTML


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('&iarqtdf>', unescapeHTML('&iarqtdf&gt;'))

    def test_diversity_2(self):
        self.assertEqual('&tfvjw<', unescapeHTML('&tfvjw&lt;'))

    def test_diversity_3(self):
        self.assertEqual('&qhipdn<', unescapeHTML('&qhipdn&lt;'))

    def test_diversity_4(self):
        self.assertEqual('&kwhc>', unescapeHTML('&kwhc&gt;'))

    def test_diversity_5(self):
        self.assertEqual('&fspb>', unescapeHTML('&fspb&gt;'))

    def test_diversity_6(self):
        self.assertEqual('&uei"', unescapeHTML('&uei&quot;'))

    def test_diversity_7(self):
        self.assertEqual('&klrmk>', unescapeHTML('&klrmk&gt;'))

    def test_diversity_8(self):
        self.assertEqual('&hjp&', unescapeHTML('&hjp&amp;'))

    def test_diversity_9(self):
        self.assertEqual('&nyl>', unescapeHTML('&nyl&gt;'))

    def test_diversity_10(self):
        self.assertEqual('&aumuazm&', unescapeHTML('&aumuazm&amp;'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('ijthrp', unescapeHTML('ijthrp'))

    def test_diversity_2(self):
        self.assertEqual('yhfvhn', unescapeHTML('yhfvhn'))

    def test_diversity_3(self):
        self.assertEqual('fnxlcn', unescapeHTML('fnxlcn'))

    def test_diversity_4(self):
        self.assertEqual('ovgdaa', unescapeHTML('ovgdaa'))

    def test_diversity_5(self):
        self.assertEqual('zr', unescapeHTML('zr'))

    def test_diversity_6(self):
        self.assertEqual('nlnb', unescapeHTML('nlnb'))

    def test_diversity_7(self):
        self.assertEqual('ygmpjcxa', unescapeHTML('ygmpjcxa'))

    def test_diversity_8(self):
        self.assertEqual('ioemyy', unescapeHTML('ioemyy'))

    def test_diversity_9(self):
        self.assertEqual('wqb', unescapeHTML('wqb'))

    def test_diversity_10(self):
        self.assertEqual('ygennu', unescapeHTML('ygennu'))
