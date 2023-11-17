import sys

from thefuck.utils import get_all_executables

if __name__ == "__main__":
    assert len(sys.argv) == 2
    all_ex_ = get_all_executables()
    stripped_ = (sys.argv[2]).strip()
    if stripped_ in all_ex_:
        print(sys.argv[2])
    else:
        print('Not Valid')

    # assert len(sys.argv) == 2