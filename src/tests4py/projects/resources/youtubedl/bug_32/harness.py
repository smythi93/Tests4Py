import base64
import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import strip_jsonp

if __name__ == "__main__":
    code = base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8")
    print(repr(strip_jsonp(code)))
