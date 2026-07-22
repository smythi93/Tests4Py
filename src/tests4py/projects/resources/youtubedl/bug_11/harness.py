import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import str_to_int

if __name__ == "__main__":
    mode = sys.argv[1]
    value = sys.argv[2]
    if mode == "int":
        result = str_to_int(int(value))
    else:
        result = str_to_int(value)
    print(repr(result))
