import sys
from thefuck.shells.fish import *

if __name__ == "__main__":
    assert len(sys.argv) == 4
    expected = " ".join(sys.argv[1:])
    f1 = Fish()
    fish_version = f1.info()
    if expected == fish_version:
        print(expected)
    else:
        print("Error, Fish version cannot be retrieved")
