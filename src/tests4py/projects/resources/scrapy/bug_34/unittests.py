import unittest

from scrapy.item import Item, Field


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        class T(Item):
            fields = {'vvtm': Field(default='zqiiq')}
        item = T(**{'vvtm': 'wnfqjt'})
        self.assertEqual('wnfqjt', item['vvtm'])

    def test_diversity_2(self):
        class T(Item):
            fields = {'vnue': Field(default='jzlp')}
        item = T(**{'vnue': 'ggglouj'})
        self.assertEqual('ggglouj', item['vnue'])

    def test_diversity_3(self):
        class T(Item):
            fields = {'ommsqgt': Field(default='mxrezi')}
        item = T(**{'ommsqgt': 'edi'})
        self.assertEqual('edi', item['ommsqgt'])

    def test_diversity_4(self):
        class T(Item):
            fields = {'wtfr': Field(default='mrehiiy')}
        item = T(**{'wtfr': 'pyvciul'})
        self.assertEqual('pyvciul', item['wtfr'])

    def test_diversity_5(self):
        class T(Item):
            fields = {'egugct': Field(default='xgbn')}
        item = T(**{'egugct': 'bhllt'})
        self.assertEqual('bhllt', item['egugct'])

    def test_diversity_6(self):
        class T(Item):
            fields = {'unky': Field(default='czjaezl')}
        item = T(**{'unky': 'tncjd'})
        self.assertEqual('tncjd', item['unky'])

    def test_diversity_7(self):
        class T(Item):
            fields = {'mcpcwke': Field(default='ntgtn')}
        item = T(**{'mcpcwke': 'cwmd'})
        self.assertEqual('cwmd', item['mcpcwke'])

    def test_diversity_8(self):
        class T(Item):
            fields = {'dma': Field(default='ehvjxtm')}
        item = T(**{'dma': 'kwzr'})
        self.assertEqual('kwzr', item['dma'])

    def test_diversity_9(self):
        class T(Item):
            fields = {'fwnlo': Field(default='tcd')}
        item = T(**{'fwnlo': 'syi'})
        self.assertEqual('syi', item['fwnlo'])

    def test_diversity_10(self):
        class T(Item):
            fields = {'sct': Field(default='dtfwx')}
        item = T(**{'sct': 'oeub'})
        self.assertEqual('oeub', item['sct'])


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        T = type('T', (Item,), {'tbo': Field(default='tdnfqsg')})
        item = T(**{'tbo': 'ytzaid'})
        self.assertEqual('ytzaid', item['tbo'])

    def test_diversity_2(self):
        T = type('T', (Item,), {'shyde': Field(default='rmuyidf')})
        item = T(**{'shyde': 'nik'})
        self.assertEqual('nik', item['shyde'])

    def test_diversity_3(self):
        T = type('T', (Item,), {'vpwjj': Field(default='eyrs')})
        item = T(**{'vpwjj': 'ahn'})
        self.assertEqual('ahn', item['vpwjj'])

    def test_diversity_4(self):
        T = type('T', (Item,), {'xtlwa': Field(default='bftscd')})
        item = T(**{'xtlwa': 'bjogtc'})
        self.assertEqual('bjogtc', item['xtlwa'])

    def test_diversity_5(self):
        T = type('T', (Item,), {'khyg': Field(default='bsjnbbq')})
        item = T(**{'khyg': 'ackyuvz'})
        self.assertEqual('ackyuvz', item['khyg'])

    def test_diversity_6(self):
        T = type('T', (Item,), {'kzxt': Field(default='arvush')})
        item = T(**{'kzxt': 'nyev'})
        self.assertEqual('nyev', item['kzxt'])

    def test_diversity_7(self):
        T = type('T', (Item,), {'sfp': Field(default='fbfidlj')})
        item = T(**{'sfp': 'uvw'})
        self.assertEqual('uvw', item['sfp'])

    def test_diversity_8(self):
        T = type('T', (Item,), {'neavfn': Field(default='ryemxcp')})
        item = T(**{'neavfn': 'wcjqr'})
        self.assertEqual('wcjqr', item['neavfn'])

    def test_diversity_9(self):
        T = type('T', (Item,), {'ayjz': Field(default='desgv')})
        item = T(**{'ayjz': 'dtksr'})
        self.assertEqual('dtksr', item['ayjz'])

    def test_diversity_10(self):
        T = type('T', (Item,), {'babkadn': Field(default='yxe')})
        item = T(**{'babkadn': 'vighgd'})
        self.assertEqual('vighgd', item['babkadn'])
