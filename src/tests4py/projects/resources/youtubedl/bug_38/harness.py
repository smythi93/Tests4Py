import sys
from urllib.parse import urlencode

if __name__ == "__main__":
    mode = sys.argv[1]
    key = sys.argv[2]
    value = sys.argv[3]
    if mode == "ytdl":
        # noinspection PyUnresolvedReferences
        from youtube_dl.utils import urlencode_postdata

        result = urlencode_postdata({key: value})
    else:
        result = urlencode({key: value}).encode("ascii")
    print(repr(result))
