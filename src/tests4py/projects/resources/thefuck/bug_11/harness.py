import sys
from thefuck.rules.git_push import get_new_command
from thefuck.types import Command

if __name__ == "__main__":
    assert len(sys.argv) == 4
    expected = sys.argv[1]
    command = sys.argv[2]
    std_err = sys.argv[3]
    expected = expected.replace("(", "")
    expected = expected.replace(",", "")
    command = command.replace(",", "")
    std_err = std_err.replace(")", "")
    std_err = std_err.replace("\\n", "\n")
    print(get_new_command(Command(command, "", std_err)))
