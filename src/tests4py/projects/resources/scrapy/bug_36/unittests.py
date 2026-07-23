import unittest

from scrapy.utils.misc import create_instance


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        class Obj6461(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return None
        settings = object()
        call = lambda: create_instance(Obj6461, settings, None)
        self.assertRaises(TypeError, call)

    def test_diversity_2(self):
        class Obj96720(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return None
        settings = object()
        call = lambda: create_instance(Obj96720, settings, None)
        self.assertRaises(TypeError, call)

    def test_diversity_3(self):
        class Obj73272(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return None
        settings = object()
        crawler = type('C73272', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj73272, settings, crawler)
        self.assertRaises(TypeError, call)

    def test_diversity_4(self):
        class Obj85510(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return None
        settings = object()
        crawler = type('C85510', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj85510, settings, crawler)
        self.assertRaises(TypeError, call)

    def test_diversity_5(self):
        class Obj44797(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return None
        settings = object()
        call = lambda: create_instance(Obj44797, settings, None)
        self.assertRaises(TypeError, call)

    def test_diversity_6(self):
        class Obj84322(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return None
        settings = object()
        crawler = type('C84322', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj84322, settings, crawler)
        self.assertRaises(TypeError, call)

    def test_diversity_7(self):
        class Obj53942(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return None
        settings = object()
        call = lambda: create_instance(Obj53942, settings, None)
        self.assertRaises(TypeError, call)

    def test_diversity_8(self):
        class Obj69415(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return None
        settings = object()
        crawler = type('C69415', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj69415, settings, crawler)
        self.assertRaises(TypeError, call)

    def test_diversity_9(self):
        class Obj31862(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return None
        settings = object()
        call = lambda: create_instance(Obj31862, settings, None)
        self.assertRaises(TypeError, call)

    def test_diversity_10(self):
        class Obj48015(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return None
        settings = object()
        call = lambda: create_instance(Obj48015, settings, None)
        self.assertRaises(TypeError, call)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        class Obj56114(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return cls()
        settings = object()
        call = lambda: create_instance(Obj56114, settings, None)
        self.assertIsNotNone(call())

    def test_diversity_2(self):
        class Obj74207(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return cls()
        settings = object()
        call = lambda: create_instance(Obj74207, settings, None)
        self.assertIsNotNone(call())

    def test_diversity_3(self):
        class Obj4400(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return cls()
        settings = object()
        crawler = type('C4400', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj4400, settings, crawler)
        self.assertIsNotNone(call())

    def test_diversity_4(self):
        class Obj70316(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return cls()
        settings = object()
        call = lambda: create_instance(Obj70316, settings, None)
        self.assertIsNotNone(call())

    def test_diversity_5(self):
        class Obj45804(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return cls()
        settings = object()
        call = lambda: create_instance(Obj45804, settings, None)
        self.assertIsNotNone(call())

    def test_diversity_6(self):
        class Obj73799(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return cls()
        settings = object()
        crawler = type('C73799', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj73799, settings, crawler)
        self.assertIsNotNone(call())

    def test_diversity_7(self):
        class Obj72003(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return cls()
        settings = object()
        crawler = type('C72003', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj72003, settings, crawler)
        self.assertIsNotNone(call())

    def test_diversity_8(self):
        class Obj56157(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return cls()
        settings = object()
        call = lambda: create_instance(Obj56157, settings, None)
        self.assertIsNotNone(call())

    def test_diversity_9(self):
        class Obj13666(object):

            @classmethod
            def from_settings(cls, settings, *a, **k):
                return cls()
        settings = object()
        call = lambda: create_instance(Obj13666, settings, None)
        self.assertIsNotNone(call())

    def test_diversity_10(self):
        class Obj64379(object):

            @classmethod
            def from_crawler(cls, crawler, *a, **k):
                return cls()
        settings = object()
        crawler = type('C64379', (object,), {'settings': settings})()
        call = lambda: create_instance(Obj64379, settings, crawler)
        self.assertIsNotNone(call())
