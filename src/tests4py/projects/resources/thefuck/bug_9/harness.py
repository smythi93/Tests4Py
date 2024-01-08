import sys
from thefuck.types import Command
from thefuck.rules.git_push import get_new_command

if __name__ == "__main__":
    assert len(sys.argv) == 5
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected.replace(",", "")
    script = sys.argv[2]
    script = script.replace(",", "")
    output_stderr = sys.argv[4]
    output_stderr = output_stderr.replace(")", "")
    output_stderr = output_stderr.replace(",", "")
    output_stderr = output_stderr.replace("\\n", "\n")
    if expected == get_new_command(Command(script, "", output_stderr)):
        print(get_new_command(Command(script, "", output_stderr)))
    else:
        print("Expected and output do not match")
