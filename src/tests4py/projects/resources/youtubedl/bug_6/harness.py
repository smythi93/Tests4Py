import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import parse_dfxp_time_expr

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "none":
        te = None
    elif mode == "empty":
        te = ""
    else:
        te = sys.argv[2]
    print(repr(parse_dfxp_time_expr(te)))
