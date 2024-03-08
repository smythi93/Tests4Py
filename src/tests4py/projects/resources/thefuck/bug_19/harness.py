import sys
from thefuck.types import Command
from thefuck.rules.git_push_force import match, get_new_command

if __name__ == "__main__":
    assert len(sys.argv) == 5
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected.replace(",", "")
    script = sys.argv[2]
    script = script.replace(",", "")
    std_err = sys.argv[4]
    if len(std_err) < 25:
        std_err = std_err.replace(")", "")
    else:
        std_err = std_err.replace(" )", " ")

    std_err = std_err.replace("\\n", "\n")
    if expected == "True":
        print(match(Command(script, "", std_err)))
    else:
        print(get_new_command(Command(script, "", std_err)))
