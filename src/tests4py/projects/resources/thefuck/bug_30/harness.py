import sys
import os
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.fix_file import match

# The bug 30 fault only manifests when an EDITOR is configured: the buggy match
# reports a fixable file whenever the stderr matches a known compiler/interpreter
# pattern, while the fixed match additionally requires that the referenced file
# actually exists on disk.
os.environ["EDITOR"] = "vim"

if __name__ == "__main__":
    assert len(sys.argv) == 4
    script = sys.argv[1]
    script = script.replace("(", "")
    script = script[:-1]
    error = sys.argv[2]
    error = error[:-1]
    result = sys.argv[3]
    result = result.replace(")", "")
    if not match(Command(script, "", error), Settings()):
        print(False)
    else:
        print("Result is not correct")
