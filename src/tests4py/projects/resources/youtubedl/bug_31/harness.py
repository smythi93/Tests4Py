import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import parse_duration

if __name__ == "__main__":
    s = " ".join(sys.argv[1:])
    print(repr(parse_duration(s)))
