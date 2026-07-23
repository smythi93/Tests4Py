import unittest

# noinspection PyUnresolvedReferences
from scrapy.selector import Selector
# noinspection PyUnresolvedReferences
from scrapy.http import TextResponse


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>gnjjzm</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>gnjjzm</p></body></html>', type='html')

    def test_diversity_2(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>vrpordle</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>vrpordle</p></body></html>', type='html')

    def test_diversity_3(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>bvbr</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>bvbr</p></body></html>', type='html')

    def test_diversity_4(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>rucxv</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>rucxv</p></body></html>', type='html')

    def test_diversity_5(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>nczycldi</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>nczycldi</p></body></html>', type='html')

    def test_diversity_6(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>ozxoncp</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>ozxoncp</p></body></html>', type='html')

    def test_diversity_7(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>pmjaszzr</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>pmjaszzr</p></body></html>', type='html')

    def test_diversity_8(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>ywkig</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>ywkig</p></body></html>', type='html')

    def test_diversity_9(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>jnvna</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>jnvna</p></body></html>', type='html')

    def test_diversity_10(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>waarbfptf</p></body></html>', encoding='utf-8')
        with self.assertRaises(ValueError):
            Selector(response=resp, text='<html><body><p>waarbfptf</p></body></html>', type='html')


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        sel = Selector(text='<html><body><p>hlmpsnji</p></body></html>', type='html')
        self.assertIsNotNone(sel)

    def test_diversity_2(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>swgzmo</p></body></html>', encoding='utf-8')
        sel = Selector(response=resp, type='html')
        self.assertIsNotNone(sel)

    def test_diversity_3(self):
        sel = Selector(text='<html><body><p>tfpy</p></body></html>', type='html')
        self.assertIsNotNone(sel)

    def test_diversity_4(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>gabq</p></body></html>', encoding='utf-8')
        sel = Selector(response=resp, type='html')
        self.assertIsNotNone(sel)

    def test_diversity_5(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>naiuvqf</p></body></html>', encoding='utf-8')
        sel = Selector(response=resp, type='html')
        self.assertIsNotNone(sel)

    def test_diversity_6(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>qgyxeh</p></body></html>', encoding='utf-8')
        sel = Selector(response=resp, type='html')
        self.assertIsNotNone(sel)

    def test_diversity_7(self):
        sel = Selector(text='<html><body><p>iwqlu</p></body></html>', type='html')
        self.assertIsNotNone(sel)

    def test_diversity_8(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>grsdxkg</p></body></html>', encoding='utf-8')
        sel = Selector(response=resp, type='html')
        self.assertIsNotNone(sel)

    def test_diversity_9(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>zoqxzt</p></body></html>', encoding='utf-8')
        sel = Selector(response=resp, type='html')
        self.assertIsNotNone(sel)

    def test_diversity_10(self):
        resp = TextResponse(url='http://example.com', body=b'<html><body><p>pxupjj</p></body></html>', encoding='utf-8')
        sel = Selector(response=resp, type='html')
        self.assertIsNotNone(sel)

