import sys
from thefuck.types import CorrectedCommand

# The bug 24 fault is CorrectedCommand equality: the buggy version is a plain
# namedtuple (so `priority` participates in ==), while the fixed version is a
# class whose __eq__ ignores `priority`. Two commands with the same script and
# side_effect but different priority compare unequal on buggy, equal on fixed.
if __name__ == "__main__":
    assert len(sys.argv) == 6
    expected = sys.argv[1]
    script = sys.argv[2]
    side_effect = sys.argv[3]
    p1 = int(sys.argv[4])
    p2 = int(sys.argv[5])
    result = CorrectedCommand(script, side_effect, p1) == CorrectedCommand(
        script, side_effect, p2
    )
    print(result)
