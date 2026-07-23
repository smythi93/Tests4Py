import unittest
from io import BytesIO
from tempfile import mkdtemp

# noinspection PyUnresolvedReferences
from PIL import Image
# noinspection PyUnresolvedReferences
from scrapy.pipelines.images import ImagesPipeline


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (146, 20, 124, 96)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (214, 167, 206))], conv.getcolors())

    def test_diversity_2(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (9, 0, 37, 199)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (63, 56, 85))], conv.getcolors())

    def test_diversity_3(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (150, 120, 194, 125)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (204, 189, 225))], conv.getcolors())

    def test_diversity_4(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (81, 197, 5, 99)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (187, 232, 158))], conv.getcolors())

    def test_diversity_5(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (125, 50, 186, 135)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (186, 146, 218))], conv.getcolors())

    def test_diversity_6(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (137, 138, 174, 54)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (230, 230, 238))], conv.getcolors())

    def test_diversity_7(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (49, 144, 141, 97)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (177, 213, 212))], conv.getcolors())

    def test_diversity_8(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (169, 156, 175, 52)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (237, 235, 239))], conv.getcolors())

    def test_diversity_9(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (108, 85, 23, 122)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (185, 174, 144))], conv.getcolors())

    def test_diversity_10(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (104, 64, 113, 54)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        im = im.convert('P')
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (223, 215, 225))], conv.getcolors())


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (100, 149, 49, 41)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (230, 238, 222))], conv.getcolors())

    def test_diversity_2(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (102, 184, 249, 243)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (109, 187, 249))], conv.getcolors())

    def test_diversity_3(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (99, 14, 185, 92)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (199, 168, 230))], conv.getcolors())

    def test_diversity_4(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (220, 155, 182, 180)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (230, 184, 203))], conv.getcolors())

    def test_diversity_5(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (61, 45, 101, 59)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (210, 206, 219))], conv.getcolors())

    def test_diversity_6(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (137, 159, 100, 127)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (196, 207, 178))], conv.getcolors())

    def test_diversity_7(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (247, 114, 70, 182)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (249, 154, 123))], conv.getcolors())

    def test_diversity_8(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (107, 6, 96, 229)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (122, 31, 112))], conv.getcolors())

    def test_diversity_9(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (86, 8, 170, 172)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (141, 88, 198))], conv.getcolors())

    def test_diversity_10(self):
        buf = BytesIO()
        Image.new('RGBA', (50, 50), (156, 191, 193, 165)).save(buf, 'PNG')
        buf.seek(0)
        im = Image.open(buf)
        pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
        conv, _ = pipeline.convert_image(im)
        self.assertEqual('RGB', conv.mode)
        self.assertEqual([(2500, (191, 214, 215))], conv.getcolors())

