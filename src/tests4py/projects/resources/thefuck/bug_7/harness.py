import sys
from thefuck.types import Command
from thefuck.rules.php_s import match

if __name__ == "__main__":
    assert len(sys.argv) >= 5
    result_ = sys.argv[1]
    input_ = " ".join(sys.argv[2:])
    print(match(Command(input_, "")))
