import base64
import json
import os
import sys

os.environ["T4PVAR"] = "XPANDED"

# noinspection PyUnresolvedReferences
from youtube_dl import YoutubeDL

if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    ydl = YoutubeDL({"outtmpl": d["outtmpl"]})
    print(repr(ydl.prepare_filename(d["info"])))
