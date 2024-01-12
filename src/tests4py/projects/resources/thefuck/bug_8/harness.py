import sys
from thefuck.rules.dnf_no_such_command import match
from thefuck.types import Command

if __name__ == "__main__":
    assert len(sys.argv) == 4
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected.replace(",", "")
    script = sys.argv[2]
    script = script.replace(",", "")
    output = sys.argv[3]
    output = output.replace(")", "")
    output = output.replace("\\n", "\n")
    print(match(Command(script, output)))
