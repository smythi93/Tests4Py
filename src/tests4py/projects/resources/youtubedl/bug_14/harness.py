import base64
import json
import sys

# noinspection PyUnresolvedReferences
from youtube_dl.extractor import YoutubeIE


def _fmt(s):
    if s >= 3600:
        return "%d:%02d:%02d" % (s // 3600, (s % 3600) // 60, s % 60)
    return "%d:%02d" % (s // 60, s % 60)


def build_desc(chapters):
    lines = []
    for sec, title in chapters:
        lines.append(
            '<a href="#" onclick="yt.www.watch.player.seekTo(%d);return false;">'
            "%s</a> - %s" % (sec, _fmt(sec), title)
        )
    return "<br />".join(lines)


if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    desc = build_desc([tuple(c) for c in d["chapters"]])
    if d["method"] == "new":
        res = YoutubeIE._extract_chapters_from_description(desc, d["dur"])
    else:
        res = YoutubeIE._extract_chapters(desc, d["dur"])
    print(repr(res))
