import unittest

# noinspection PyUnresolvedReferences
from scrapy.item import Item, Field


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        class Item_oruw(Item):
        
            def method(self):
                return super().__init__
        item = Item_oruw()
        self.assertIsNotNone(item)

    def test_diversity_2(self):
        class Item_czvxry(Item):
        
            def method(self):
                return super().__init__
        item = Item_czvxry()
        self.assertIsNotNone(item)

    def test_diversity_3(self):
        class Item_bxesisn(Item):
        
            def method(self):
                return super().__init__
        item = Item_bxesisn()
        self.assertIsNotNone(item)

    def test_diversity_4(self):
        class Item_cywgj(Item):
        
            def method(self):
                return super().__init__
        item = Item_cywgj()
        self.assertIsNotNone(item)

    def test_diversity_5(self):
        class Item_jhclbp(Item):
        
            def method(self):
                return super().__init__
        item = Item_jhclbp()
        self.assertIsNotNone(item)

    def test_diversity_6(self):
        class Item_wgwxkyua(Item):
        
            def method(self):
                return super().__init__
        item = Item_wgwxkyua()
        self.assertIsNotNone(item)

    def test_diversity_7(self):
        class Item_jjy(Item):
        
            def method(self):
                return super().__init__
        item = Item_jjy()
        self.assertIsNotNone(item)

    def test_diversity_8(self):
        class Item_lkolue(Item):
        
            def method(self):
                return super().__init__
        item = Item_lkolue()
        self.assertIsNotNone(item)

    def test_diversity_9(self):
        class Item_ewkr(Item):
        
            def method(self):
                return super().__init__
        item = Item_ewkr()
        self.assertIsNotNone(item)

    def test_diversity_10(self):
        class Item_gws(Item):
        
            def method(self):
                return super().__init__
        item = Item_gws()
        self.assertIsNotNone(item)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        class Item_swax(Item):
            name = Field()
        item = Item_swax(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_2(self):
        class Item_ofoudjaw(Item):
            name = Field()
        item = Item_ofoudjaw(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_3(self):
        class Item_hqvbs(Item):
            name = Field()
        item = Item_hqvbs(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_4(self):
        class Item_rjhpuc(Item):
            name = Field()
        item = Item_rjhpuc(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_5(self):
        class Item_plpruyc(Item):
            name = Field()
        item = Item_plpruyc(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_6(self):
        class Item_ylf(Item):
            name = Field()
        item = Item_ylf(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_7(self):
        class Item_palax(Item):
            name = Field()
        item = Item_palax(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_8(self):
        class Item_nvdqg(Item):
            name = Field()
        item = Item_nvdqg(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_9(self):
        class Item_zeilj(Item):
            name = Field()
        item = Item_zeilj(name='x')
        self.assertEqual('x', item['name'])

    def test_diversity_10(self):
        class Item_blfvjnn(Item):
            name = Field()
        item = Item_blfvjnn(name='x')
        self.assertEqual('x', item['name'])
