import sys
from middle import middle


if __name__ == "__main__":
    assert len(sys.argv) == 4
    print(middle(*tuple(map(int, sys.argv[1:]))))
