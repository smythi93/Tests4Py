import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import urljoin

if __name__ == "__main__":
    mode = sys.argv[1]
    base = sys.argv[2]
    path = sys.argv[3]
    if mode[0] == "b":
        base = base.encode("utf-8")
    if mode[1] == "b":
        path = path.encode("utf-8")
    print(repr(urljoin(base, path)))
