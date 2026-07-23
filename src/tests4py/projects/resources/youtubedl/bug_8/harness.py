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
    formats = [
        {
            "format_id": i,
            "ext": "mp4",
            "url": "http://_/",
            "vcodec": "h264",
            "acodec": "aac",
            "tbr": t,
        }
        for i, t in d["fmts"]
    ]
    info = {
        "formats": formats,
        "id": "testid",
        "title": "t",
        "extractor": "testex",
        "extractor_key": "TestEx",
    }
    ydl = YDL({"format": d["format"]})
    ydl.process_ie_result(dict(info))
    print(repr([x["format_id"] for x in ydl.downloaded_info_dicts]))
