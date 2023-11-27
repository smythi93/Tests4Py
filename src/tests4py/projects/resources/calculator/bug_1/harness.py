import sys
from calc import main, sqrt


if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(main((sys.argv[1])))
