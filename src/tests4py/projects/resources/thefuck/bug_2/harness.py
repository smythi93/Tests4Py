import sys
from thefuck.utils import get_all_executables

if __name__ == "__main__":
    print(sys.argv[0:])
    executables = get_all_executables()
    # print(executables)
