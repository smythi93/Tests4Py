import sys
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.mkdir_p import get_new_command


if __name__ == "__main__":
    assert len(sys.argv) == 3
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected[:-1]
    script = sys.argv[2]
    script = script.replace(",", "")
    script = script[:-1]
    if expected == get_new_command(Command(script, "", ""), Settings()):
        print(expected)
    else:
        print("Expected was ", expected, ", Output was ", get_new_command(Command(script, "", ""), Settings()))
