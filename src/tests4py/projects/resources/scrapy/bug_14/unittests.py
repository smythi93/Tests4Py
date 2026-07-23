import unittest

# noinspection PyUnresolvedReferences
from scrapy.http import Response
# noinspection PyUnresolvedReferences
from scrapy.utils.gz import is_gzipped


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/X-Gzip'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_2(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'APPLICATION/GZIP'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_3(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'Application/GZip'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_4(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/x-gzip;charset=qtn'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_5(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/gzip;charset=hgtr'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_6(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/X-GZIP;charset=mwkxg'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_7(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/x-gzip;charset=jguqd'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_8(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/gzip;charset=rhabpah'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_9(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/X-GZIP;charset=kzlpwr'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_10(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/x-gzip;charset=pqj'})
        self.assertEqual(True, is_gzipped(response))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/x-gzip'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_2(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/gzip'})
        self.assertEqual(True, is_gzipped(response))

    def test_diversity_3(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/gziptmr'})
        self.assertEqual(False, is_gzipped(response))

    def test_diversity_4(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'text/lfunc'})
        self.assertEqual(False, is_gzipped(response))

    def test_diversity_5(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'image/hde'})
        self.assertEqual(False, is_gzipped(response))

    def test_diversity_6(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/gzipcncmrn'})
        self.assertEqual(False, is_gzipped(response))

    def test_diversity_7(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'text/ilkvgk'})
        self.assertEqual(False, is_gzipped(response))

    def test_diversity_8(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'image/wybdso'})
        self.assertEqual(False, is_gzipped(response))

    def test_diversity_9(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'application/gzipvkz'})
        self.assertEqual(False, is_gzipped(response))

    def test_diversity_10(self):
        response = Response('http://www.example.com', headers={'Content-Type': 'text/joy'})
        self.assertEqual(False, is_gzipped(response))

