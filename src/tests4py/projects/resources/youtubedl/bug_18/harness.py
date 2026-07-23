import base64
import json
import sys

# noinspection PyUnresolvedReferences
from test.helper import FakeYDL

# noinspection PyUnresolvedReferences
from youtube_dl.extractor.common import InfoExtractor


class YDL(FakeYDL):
    def __init__(self, *a, **k):
        super(YDL, self).__init__(*a, **k)
        self.downloaded_info_dicts = []

    def process_info(self, info_dict):
        self.downloaded_info_dicts.append(info_dict)

    def to_screen(self, msg):
        pass


if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    ydl = YDL()

    class Foo1IE(InfoExtractor):
        _VALID_URL = r"foo1:"

        def _real_extract(self, url):
            return {
                "_type": "url_transparent",
                "url": "foo2:",
                "ie_key": "Foo2",
                "title": d["t_title"],
                "id": d["t_id"],
            }

    class Foo2IE(InfoExtractor):
        _VALID_URL = r"foo2:"

        def _real_extract(self, url):
            return {"_type": "url", "url": "foo3:", "ie_key": "Foo3"}

    class Foo3IE(InfoExtractor):
        _VALID_URL = r"foo3:"

        def _real_extract(self, url):
            return {
                "formats": [{"url": "http://localhost/sample.mp4"}],
                "id": d["final_id"],
                "title": "foo3 title",
                "extractor": "testex",
                "extractor_key": "TestEx",
            }

    ydl.add_info_extractor(Foo1IE(ydl))
    ydl.add_info_extractor(Foo2IE(ydl))
    ydl.add_info_extractor(Foo3IE(ydl))
    ydl.extract_info("foo1:")
    print(repr(ydl.downloaded_info_dicts[0][d["field"]]))
