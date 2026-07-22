import base64
import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import uppercase_escape

if __name__ == "__main__":
    s = base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8")
    print(repr(uppercase_escape(s)))
