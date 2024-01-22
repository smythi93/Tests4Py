import sys
from thefuck.shells.fish import *
from thefuck.shells.fish import _get_aliases


if __name__ == "__main__":
    assert len(sys.argv) == 2
    fish = Fish()
    overridden = list(_get_aliases(fish._get_overridden_aliases()))

    if sys.argv[1] in overridden:
        print(sys.argv[1])
    else:
        print("Error Retrieving Fish Shell Overridden")
