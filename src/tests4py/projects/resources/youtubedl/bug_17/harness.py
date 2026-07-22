import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import cli_bool_option

if __name__ == "__main__":
    present = sys.argv[1]
    boolval = sys.argv[2]
    key = sys.argv[3]
    option = sys.argv[4]
    if present == "no":
        params = {}
    else:
        params = {key: boolval == "True"}
    print(repr(cli_bool_option(params, option, key)))
