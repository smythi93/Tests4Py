import sys
from thefuck.rules.git_branch_exists import match
from thefuck.rules.git_branch_exists import get_new_command
from thefuck.types import Command

if __name__ == "__main__":
    assert len(sys.argv) == 4
    expected = sys.argv[1]
    script_parts = sys.argv[2]
    output = sys.argv[3]
    expected = expected.replace("(", "")
    expected = expected.replace(",", "")
    script_parts = script_parts.replace(",", "")
    output = output.replace(")", "")

    if "branch_name" in output:
        output = bytes(output, 'utf-8')

    if len(output) <= 4:
        output = int(output)

    expected = match(Command(script_parts, output))
    if expected is True or expected is False:
        print(match(Command(script_parts, output)))
    else:
        raise TypeError("Return value should be Boolean")
