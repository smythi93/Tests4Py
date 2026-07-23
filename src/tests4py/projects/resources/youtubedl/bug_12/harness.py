import base64
import json
import sys

# noinspection PyUnresolvedReferences
from test.helper import FakeYDL


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
    info = {
        "formats": d["formats"],
        "id": "testid",
        "title": "t",
        "extractor": "testex",
        "extractor_key": "TestEx",
    }
    ydl = YDL({"format": d["format"]})
    ydl.process_ie_result(dict(info))
    print(repr(ydl.downloaded_info_dicts[0]["format_id"]))
