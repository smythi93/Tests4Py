import sys
from thefuck.shells.fish import Fish

if __name__ == "__main__":
    assert len(sys.argv) == 2 or len(sys.argv) == 5
    sys_ = " ".join(sys.argv[1:])
    f = Fish()
    if sys_ in f._get_overridden_aliases():
        print(sys_)
    else:
        print('Error Retrieving Fish Shell Overridden')
