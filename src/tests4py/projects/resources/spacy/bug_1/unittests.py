import unittest
from spacy.errors import add_codes



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__delattr__'), str)

    def test_diversity_2(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__format__'), str)

    def test_diversity_3(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__hash__'), str)

    def test_diversity_4(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__reduce__'), str)

    def test_diversity_5(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__dir__'), str)

    def test_diversity_6(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__init__'), str)

    def test_diversity_7(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__dict__'), str)

    def test_diversity_8(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__repr__'), str)

    def test_diversity_9(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__reduce_ex__'), str)

    def test_diversity_10(self):
        wrapped = add_codes(type('Errors', (object,), {'E001': 'message'}))
        self.assertNotIsInstance(getattr(wrapped, '__setattr__'), str)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        wrapped = add_codes(type('Errors', (object,), {'W292': 'aIx NCkgEe'}))
        self.assertEqual('[W292] aIx NCkgEe', getattr(wrapped, 'W292'))

    def test_diversity_2(self):
        wrapped = add_codes(type('Errors', (object,), {'T316': 'JoqfM'}))
        self.assertEqual('[T316] JoqfM', getattr(wrapped, 'T316'))

    def test_diversity_3(self):
        wrapped = add_codes(type('Errors', (object,), {'W261': 'OLSvR axoLrrZg PNqqvJx'}))
        self.assertEqual('[W261] OLSvR axoLrrZg PNqqvJx', getattr(wrapped, 'W261'))

    def test_diversity_4(self):
        wrapped = add_codes(type('Errors', (object,), {'E362': 'mPI'}))
        self.assertEqual('[E362] mPI', getattr(wrapped, 'E362'))

    def test_diversity_5(self):
        wrapped = add_codes(type('Errors', (object,), {'E565': 'Imu SYX OUtyx LeV'}))
        self.assertEqual('[E565] Imu SYX OUtyx LeV', getattr(wrapped, 'E565'))

    def test_diversity_6(self):
        wrapped = add_codes(type('Errors', (object,), {'W470': 'QzUJ'}))
        self.assertEqual('[W470] QzUJ', getattr(wrapped, 'W470'))

    def test_diversity_7(self):
        wrapped = add_codes(type('Errors', (object,), {'T264': 'KcBC'}))
        self.assertEqual('[T264] KcBC', getattr(wrapped, 'T264'))

    def test_diversity_8(self):
        wrapped = add_codes(type('Errors', (object,), {'T723': 'BeBhgbLc MAvB ipvWAd'}))
        self.assertEqual('[T723] BeBhgbLc MAvB ipvWAd', getattr(wrapped, 'T723'))

    def test_diversity_9(self):
        wrapped = add_codes(type('Errors', (object,), {'T036': 'psnjSnlV QTwTmxt vHKakyWm TLzn'}))
        self.assertEqual('[T036] psnjSnlV QTwTmxt vHKakyWm TLzn', getattr(wrapped, 'T036'))

    def test_diversity_10(self):
        wrapped = add_codes(type('Errors', (object,), {'E438': 'LsICrr lbKpd'}))
        self.assertEqual('[E438] LsICrr lbKpd', getattr(wrapped, 'E438'))
