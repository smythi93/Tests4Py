import sys
from io import BytesIO
from tempfile import mkdtemp

# noinspection PyUnresolvedReferences
from PIL import Image

# noinspection PyUnresolvedReferences
from scrapy.pipelines.images import ImagesPipeline

if __name__ == "__main__":
    mode = sys.argv[1]
    r, g, b, a = (int(sys.argv[i]) for i in range(2, 6))
    buf = BytesIO()
    Image.new("RGBA", (50, 50), (r, g, b, a)).save(buf, "PNG")
    buf.seek(0)
    im = Image.open(buf)
    if mode == "palette":
        im = im.convert("P")
    pipeline = ImagesPipeline(mkdtemp(), download_func=lambda *a, **k: None)
    conv, _ = pipeline.convert_image(im)
    count, rgb = conv.getcolors()[0]
    print(",".join(map(str, rgb)))
