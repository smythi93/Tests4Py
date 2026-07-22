import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unescapeHTML

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "fail":
        junk = sys.argv[2]
        entity = sys.argv[3]
        s = "&" + junk + "&" + entity + ";"
    else:
        s = sys.argv[2]
    print(repr(unescapeHTML(s)))
