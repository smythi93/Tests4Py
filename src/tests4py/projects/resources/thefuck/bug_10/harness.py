import sys

from thefuck.types import Command
from thefuck.rules.man import get_new_command

# man.get_new_command gained a "No manual entry for X" special case on the fixed
# build: for a digit-less command whose stderr is exactly "No manual entry for
# <last_arg>" it returns the single suggestion [<last_arg> --help] (length 1),
# whereas the buggy build has no such case and always returns three suggestions
# (length 3). Reporting len(result) distinguishes the two builds. argv:
# expected-len, script, stderr.
if __name__ == "__main__":
    script = sys.argv[2]
    stderr = sys.argv[3]
    result = get_new_command(Command(script, "", stderr))
    print(len(result))
