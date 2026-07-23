import base64
import json
import sys

# noinspection PyUnresolvedReferences
from youtube_dl.extractor.facebook import FacebookIE

if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    print(repr(FacebookIE.suitable(d["url"])))
