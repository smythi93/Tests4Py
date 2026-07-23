import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import urljoin

if __name__ == "__main__":
    base = sys.argv[1]
    path = sys.argv[2]
    if base == "None":
        base = None
    print(repr(urljoin(base, path)))
