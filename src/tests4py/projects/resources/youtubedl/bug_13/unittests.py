import unittest

from youtube_dl.utils import urljoin


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(urljoin(None, 'rtmp://foo.de'), 'rtmp://foo.de')

    def test_diversity_2(self):
        self.assertEqual(urljoin(None, 'rtmfp://foo.de/a/b/c.txt'), 'rtmfp://foo.de/a/b/c.txt')

    def test_diversity_3(self):
        self.assertEqual(urljoin(None, 'rtmfp://foo.de'), 'rtmfp://foo.de')

    def test_diversity_4(self):
        self.assertEqual(urljoin(None, 'rsync://foo.de'), 'rsync://foo.de')

    def test_diversity_5(self):
        self.assertEqual(urljoin(None, b'rsync://foo.de'), 'rsync://foo.de')

    def test_diversity_6(self):
        self.assertEqual(urljoin(None, 'mms://foo.de/a/b.pdf'), 'mms://foo.de/a/b.pdf')

    def test_diversity_7(self):
        self.assertEqual(urljoin(None, 'mms://foo.de/'), 'mms://foo.de/')

    def test_diversity_8(self):
        self.assertEqual(urljoin(None, 'rmi://foo.de/a.pdf'), 'rmi://foo.de/a.pdf')

    def test_diversity_9(self):
        self.assertEqual(urljoin(None, 'rmi://foo.de'), 'rmi://foo.de')

    def test_diversity_10(self):
        self.assertEqual(urljoin(None, b'rtmfp://foo.de/a/b/c.pdf'), 'rtmfp://foo.de/a/b/c.pdf')


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(urljoin('http://foo.de/', '/a/b/c.txt'), 'http://foo.de/a/b/c.txt')

    def test_diversity_2(self):
        self.assertEqual(urljoin('http://foo.de/a/b/c.txt', 'rtmp://foo.de'), 'rtmp://foo.de')

    def test_diversity_3(self):
        self.assertEqual(urljoin(b'http://foo.de/', '/a/b/c.txt'), 'http://foo.de/a/b/c.txt')

    def test_diversity_4(self):
        self.assertEqual(urljoin('http://foo.de/', b'/a/b/c.txt'), 'http://foo.de/a/b/c.txt')

    def test_diversity_5(self):
        self.assertEqual(urljoin(b'http://foo.de/', b'/a/b/c.txt'), 'http://foo.de/a/b/c.txt')

    def test_diversity_6(self):
        self.assertEqual(urljoin('//foo.de/', '/a/b/c.txt'), '//foo.de/a/b/c.txt')

    def test_diversity_7(self):
        self.assertEqual(urljoin('http://foo.de/', 'a/b/c.txt'), 'http://foo.de/a/b/c.txt')

    def test_diversity_8(self):
        self.assertEqual(urljoin('http://foo.de', '/a/b/c.txt'), 'http://foo.de/a/b/c.txt')

    def test_diversity_9(self):
        self.assertEqual(urljoin(None, 'http://foo.de/a/b/c.txt'), 'http://foo.de/a/b/c.txt')

    def test_diversity_10(self):
        self.assertEqual(urljoin(None, '//foo.de/a/b/c.txt'), '//foo.de/a/b/c.txt')
