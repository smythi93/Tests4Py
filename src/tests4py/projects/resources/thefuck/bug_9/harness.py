import sys
from thefuck.types import Command
from thefuck.rules.git_push import get_new_command

if __name__ == "__main__":
    assert len(sys.argv) == 2
    print(get_new_command(Command()))
