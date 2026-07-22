import sys

# noinspection PyUnresolvedReferences
from youtube_dl.utils import unescapeHTML

if __name__ == "__main__":
    form = sys.argv[1]
    value = int(sys.argv[2])
    if form == "dec":
        s = "&#" + str(value) + ";"
    else:
        s = "&#x" + format(value, "x") + ";"
    print(repr(unescapeHTML(s)))
