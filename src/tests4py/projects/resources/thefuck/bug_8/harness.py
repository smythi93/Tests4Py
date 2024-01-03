import sys
from thefuck.rules.defn_no_such_command import _get_operations

if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(_get_operations())
