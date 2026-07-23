import sys
import tempfile

# noinspection PyUnresolvedReferences
from scrapy.settings import Settings

# noinspection PyUnresolvedReferences
from scrapy.pipelines.images import ImagesPipeline

if __name__ == "__main__":
    mode = sys.argv[1]
    n = int(sys.argv[2])
    tmp = tempfile.mkdtemp()
    try:
        if mode == "default":
            pipe = ImagesPipeline(tmp, settings=Settings())
        else:
            pipe = ImagesPipeline.from_settings(
                Settings({"IMAGES_STORE": tmp, "IMAGES_EXPIRES": n})
            )
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:%s" % pipe.expires)
