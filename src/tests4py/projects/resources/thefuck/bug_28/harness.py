import sys
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.fix_file import get_new_command
from thefuck.rules.fix_file import match


if __name__ == "__main__":
    assert len(sys.argv) == 5
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected[:-1]
    script = sys.argv[2]
    script = script.replace(",", "")
    std_out = sys.argv[3]
    std_out = std_out.replace(",", "")
    std_err = sys.argv[4]
    std_err = std_err[:-1]
    if expected == "True":
        print(get_new_command(Command(script, std_out, std_err), Settings()))
    else:
        print(match(Command(script, std_out, std_err), Settings()))
