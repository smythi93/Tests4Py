import base64
import json
import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import dfxp2srt


def _build_xml(cues):
    body = "\n".join(
        '<p begin="%d" end="%d">%s</p>' % (b, e, t) for b, e, t in cues
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n'
        '<body><div xml:lang="en">\n'
        + body
        + "\n</div></body></tt>"
    )


if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    xml = _build_xml([tuple(c) for c in d["cues"]])
    arg = xml.encode("utf-8") if d["mode"] == "bytes" else xml
    print(repr(dfxp2srt(arg)))
