import sys
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.ls_lah import match


if __name__ == "__main__":
    assert len(sys.argv) == 3
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected[:-1]
    script = sys.argv[2]
    script = script[:-1]
    print(match(Command(script, "", ""), Settings()))
