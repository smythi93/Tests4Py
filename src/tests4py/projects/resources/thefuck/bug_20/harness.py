import sys
from thefuck.types import Command
from thefuck.rules.dirty_unzip import _zip_file
from thefuck.rules.dirty_unzip import get_new_command


if __name__ == "__main__":
    assert len(sys.argv) == 3
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected[:-1]
    script = sys.argv[2]
    script = script.replace(")", "")
    if "-d" in sys.argv[1]:
        print(get_new_command(Command(script, "", "")))
    else:
        print(_zip_file(Command(script, "", "")))
