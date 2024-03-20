import sys
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.vagrant_up import get_new_command


if __name__ == "__main__":
    assert len(sys.argv) == 4 or len(sys.argv) == 5
    if len(sys.argv) == 4:
        expected = sys.argv[1]
        expected = expected.replace("(", "")
        expected = expected[:-1]
        script = sys.argv[2]
        script = script.replace(",", "")
        std_out = sys.argv[3]
        std_out = std_out[:-1]
        print(get_new_command(Command(script, "", std_out), Settings()))
    elif len(sys.argv) == 5:
        expected = " ".join(sys.argv[1:3])
        expected = expected.replace("(", "")
        expected = expected[:-1]
        script = sys.argv[3]
        script = script.replace(",", "")
        script = script[:-1]
        std_out = sys.argv[4]
        std_out = std_out[:-1]
        print(get_new_command(Command(script, "", std_out), Settings()))

    else:
        print("ASSERTION ERROR")
