import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import parse_iso8601

if __name__ == "__main__":
    date_str = sys.argv[1]
    print(repr(parse_iso8601(date_str)))
