import sys
from thefuck.shells.bash import Bash
from thefuck.shells.zsh import Zsh

if __name__ == "__main__":
    assert len(sys.argv) == 3
    bash = Bash()
    result = sys.argv[1]
    result = result[1:]
    result = result[:-1]
    alias = sys.argv[2]
    alias = alias[:-1]
    if result in bash.app_alias(alias):
        print(result)
    else:
        print("Expected and Result do not match")

