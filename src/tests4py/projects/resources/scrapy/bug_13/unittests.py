import unittest

# noinspection PyUnresolvedReferences
import tempfile
from scrapy.settings import Settings
from scrapy.pipelines.images import ImagesPipeline


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        tmp = tempfile.mkdtemp(prefix='img57004_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_2(self):
        tmp = tempfile.mkdtemp(prefix='img58515_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_3(self):
        tmp = tempfile.mkdtemp(prefix='img22494_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_4(self):
        tmp = tempfile.mkdtemp(prefix='img59104_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_5(self):
        tmp = tempfile.mkdtemp(prefix='img982_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_6(self):
        tmp = tempfile.mkdtemp(prefix='img15032_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_7(self):
        tmp = tempfile.mkdtemp(prefix='img69807_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_8(self):
        tmp = tempfile.mkdtemp(prefix='img20294_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_9(self):
        tmp = tempfile.mkdtemp(prefix='img57495_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)

    def test_diversity_10(self):
        tmp = tempfile.mkdtemp(prefix='img30804_')
        pipe = ImagesPipeline(tmp, settings=Settings())
        self.assertEqual(90, pipe.expires)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 98340}))
        self.assertEqual(98340, pipe.expires)

    def test_diversity_2(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 85032}))
        self.assertEqual(85032, pipe.expires)

    def test_diversity_3(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 34540}))
        self.assertEqual(34540, pipe.expires)

    def test_diversity_4(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 77259}))
        self.assertEqual(77259, pipe.expires)

    def test_diversity_5(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 82122}))
        self.assertEqual(82122, pipe.expires)

    def test_diversity_6(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 27732}))
        self.assertEqual(27732, pipe.expires)

    def test_diversity_7(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 73681}))
        self.assertEqual(73681, pipe.expires)

    def test_diversity_8(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 44351}))
        self.assertEqual(44351, pipe.expires)

    def test_diversity_9(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 57066}))
        self.assertEqual(57066, pipe.expires)

    def test_diversity_10(self):
        tmp = tempfile.mkdtemp()
        pipe = ImagesPipeline.from_settings(Settings({'IMAGES_STORE': tmp, 'IMAGES_EXPIRES': 84292}))
        self.assertEqual(84292, pipe.expires)
