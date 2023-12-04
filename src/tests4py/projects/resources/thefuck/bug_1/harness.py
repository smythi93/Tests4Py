import sys
from thefuck.rules.pip_unknown_command import get_new_command
from thefuck.types import Command

if __name__ == "__main__":
    assert len(sys.argv) == 4
    expected = sys.argv[1]
    script = sys.argv[2]
    output = sys.argv[3]
    script = script.replace(",", "")
    output = output.replace(")", "")
    print(get_new_command(Command(script, output)))
