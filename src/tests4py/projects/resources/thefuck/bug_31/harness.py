import sys
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.git_diff_staged import get_new_command


if __name__ == "__main__":
    assert len(sys.argv) == 3
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected[:-1]
    script = sys.argv[2]
    script = script[:-1]
    if len(script) < 5:
        script = int(script)
    if expected == get_new_command(Command(script, "", ""), Settings()):
        print(get_new_command(Command(script, "", ""), Settings()))
    else:
        print("Input as integer does not give an output")
