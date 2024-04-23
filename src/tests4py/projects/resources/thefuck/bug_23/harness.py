import sys
from thefuck.utils import cache


if __name__ == "__main__":
    assert len(sys.argv) == 4 or len(sys.argv) == 8
    if len(sys.argv) == 4:
        shelve = sys.argv[1]
        shelve = shelve.replace("(", "")
        shelve = shelve[:-1]
        fn = sys.argv[2]
        fn = fn.replace(",", "")
        key = sys.argv[3]
        key = key[:-1]
        print(cache(shelve, fn, key))
    else:
        shelve = sys.argv[1]
        shelve = shelve.replace("(", "")
        shelve = shelve[:-1]
        fn = sys.argv[2]
        fn = fn.replace(",", "")
        key = sys.argv[3]
        key = key[:-1]
        print(shelve)
