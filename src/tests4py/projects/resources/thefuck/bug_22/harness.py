import sys
from thefuck.types import SortedCorrectedCommandsSequence
from thefuck.types import CorrectedCommand
from thefuck.types import Settings

# The bug 22 fault is in SortedCorrectedCommandsSequence._realise: with an empty
# command generator the cached list is empty, and the buggy code unconditionally
# does `self._cached[0]` (IndexError). The fixed code guards with `if self._cached`.
# "empty" mode triggers the fault; "full" mode (a non-empty generator) realises
# fine on both builds.
if __name__ == "__main__":
    assert len(sys.argv) == 5
    expected = sys.argv[1]
    mode = sys.argv[2]
    script = sys.argv[3]
    priority = sys.argv[4]
    if mode == "empty":
        seq = SortedCorrectedCommandsSequence(iter([]), Settings({}))
    else:
        seq = SortedCorrectedCommandsSequence(
            iter([CorrectedCommand(script, "", int(priority))]), Settings({})
        )
    seq._realise()
    print("OK")
