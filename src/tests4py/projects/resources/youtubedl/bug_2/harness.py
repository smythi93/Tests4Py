import base64
import json
import sys

# noinspection PyUnresolvedReferences
from test.helper import FakeYDL

# noinspection PyUnresolvedReferences
from youtube_dl.extractor.common import InfoExtractor

# noinspection PyUnresolvedReferences
from youtube_dl.compat import compat_etree_fromstring

_MIME = {"a": "audio/mp4", "v": "video/mp4"}


def build_mpd(reps):
    sets = ""
    for code, rid, bw in reps:
        sets += (
            '<AdaptationSet mimeType="%s" codecs="mp4a.40.2">'
            '<SegmentTemplate timescale="1000000" '
            'initialization="i_$RepresentationID$.m4d" '
            'media="s_$RepresentationID$_$Number$.m4d" '
            'duration="2000000" startNumber="0"></SegmentTemplate>'
            '<Representation id="%s" bandwidth="%d"></Representation>'
            "</AdaptationSet>"
        ) % (_MIME[code], rid, bw)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="static" '
        'mediaPresentationDuration="PT10S">'
        "<Period>" + sets + "</Period></MPD>"
    )


class _IE(InfoExtractor):
    _VALID_URL = r"https?://.*"


if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    xml = build_mpd(d["reps"])
    ie = _IE(FakeYDL())
    formats = ie._parse_mpd_formats(
        compat_etree_fromstring(xml.encode("utf-8")),
        mpd_url="http://unknown/manifest.mpd",
    )
    print(repr(sorted(f["format_id"] for f in formats)))
