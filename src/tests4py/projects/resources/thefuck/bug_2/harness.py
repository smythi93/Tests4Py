import sys
from thefuck.utils import get_all_executables

if __name__ == "__main__":
    executables = get_all_executables()
    assert len(sys.argv) == 2
    if any(sys.argv[1] in s for s in executables):
        print(sys.argv[1])
