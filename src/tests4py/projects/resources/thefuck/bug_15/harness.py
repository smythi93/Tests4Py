import sys
from thefuck.types import Command
from thefuck.rules.git_add import match
from thefuck.rules.git_add import get_new_command

if __name__ == "__main__":
    assert len(sys.argv) == 4
    expected = sys.argv[1]
    script = sys.argv[2]
    std_err = sys.argv[3]
    expected = expected.replace(expected[len(expected) - 1], "")
    expected = expected.replace(expected[0], "")
    script = script.replace(script[len(script) - 1], "")
    if len(std_err) < 3:
        std_err = std_err.replace(")", "")
    else:
        std_err = std_err.replace("?)", "?")
    if expected == "True" or expected == "False":
        print(match(Command(script, "", std_err)))
    else:
        print(get_new_command(Command(script, "", std_err)))
