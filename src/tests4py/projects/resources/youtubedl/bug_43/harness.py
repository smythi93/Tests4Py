import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import url_basename

if __name__ == "__main__":
    url = sys.argv[1]
    print(repr(url_basename(url)))
