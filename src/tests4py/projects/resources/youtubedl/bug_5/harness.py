import base64
import json
import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unified_timestamp

if __name__ == "__main__":
    d = json.loads(base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8"))
    print(repr(unified_timestamp(d["date"])))
