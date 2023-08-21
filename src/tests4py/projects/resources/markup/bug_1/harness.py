import sys
from markup import markup


if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(markup((str, sys.argv[1:])))
