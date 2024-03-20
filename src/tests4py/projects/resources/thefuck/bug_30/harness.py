import sys
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.open import match


if __name__ == "__main__":
    assert len(sys.argv) == 4
    script = sys.argv[1]
    script = script.replace("(", "")
    script = script[:-1]
    error = sys.argv[2]
    error = error[:-1]
    result = sys.argv[3]
    result = result.replace(")", "")
    if not match(Command(script, "", error), Settings()):
        print(False)
    else:
        print("Result is not correct")
