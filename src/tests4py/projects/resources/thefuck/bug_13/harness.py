import sys
from thefuck.rules.git_branch_exists import match
from thefuck.types import Command
from thefuck.rules.git_branch_exists import get_new_command
import os

if __name__ == "__main__":
    if os.name == "nt":
        assert len(sys.argv) == 4
        expected = sys.argv[1]
        script = sys.argv[2]
        std_err = sys.argv[3]
        expected = expected.replace(expected[len(expected) - 1], "")
        expected = expected[1:]
        script = script.replace(script[len(script) - 1], "")
        std_err = std_err.replace(std_err[len(std_err) - 1], "")
        if expected == "True" or expected == "False":
            print(match(Command(script, "", std_err)))
        else:
            if expected in get_new_command(Command(script, "", std_err)):
                print(expected)

    else:
        assert len(sys.argv) == 4
        expected = sys.argv[1]
        script = sys.argv[2]
        std_err = sys.argv[3]
        expected = expected.replace(expected[len(expected) - 1], "")
        expected = expected.replace(expected[0], "")
        script = script.replace(script[len(script) - 1], "")
        std_err = std_err.replace(std_err[len(std_err) - 1], "")

        if expected == "True" or expected == "False":
            print(match(Command(script, "", std_err)))
        else:
            if expected in get_new_command(Command(script, "", std_err)):
                print(expected)
