import sys
from thefuck.rules.git_push import match
from thefuck.types import Command

if __name__ == "__main__":
    assert len(sys.argv) == 4
    script_parts = sys.argv[2]
    output = sys.argv[3]
    script_parts = script_parts.replace(",", "")
    output = output.replace(")", "")
    result = match(Command(script_parts, output))
    print(result)
