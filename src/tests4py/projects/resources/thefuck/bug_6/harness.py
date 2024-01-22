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
        output = sys.argv[3]
        expected = expected.replace(expected[len(expected) - 1], "")
        expected = expected[1:]
        script = script.replace(script[len(script) - 1], "")
        output = output.replace(output[len(output) - 1], "")
        if expected == "True" or expected == "False":
            print(match(Command(script, output)))
        else:
            if expected in get_new_command(Command(script, output)):
                print(expected)

    else:
        assert len(sys.argv) == 4
        expected = sys.argv[1]
        script = sys.argv[2]
        output = sys.argv[3]
        expected = expected.replace(expected[len(expected) - 1], "")
        expected = expected.replace(expected[0], "")
        script = script.replace(script[len(script) - 1], "")
        output = output.replace(output[len(output) - 1], "")

        if expected == "True" or expected == "False":
            print(match(Command(script, output)))
        else:
            if expected in get_new_command(Command(script, output)):
                print(expected)
