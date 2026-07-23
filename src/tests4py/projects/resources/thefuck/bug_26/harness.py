import sys

from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.vagrant_up import get_new_command

# vagrant_up.get_new_command returns a *list* of suggestions on the fixed build
# when the command names a machine (>= 3 whitespace-separated parts) and a
# *string* otherwise; the buggy build always returns a string. We report
# isinstance(result, list), which distinguishes the two builds independently of
# the exact ``shells.and_`` formatting. get_new_command only reads
# command.script, so the output/settings are inert placeholders.
if __name__ == "__main__":
    script = sys.argv[2]
    result = get_new_command(Command(script, "", ""), Settings())
    print(isinstance(result, list))
