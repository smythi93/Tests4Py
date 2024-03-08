import sys
from thefuck.shells.bash import Bash
from thefuck.shells.zsh import Zsh
# app_alias()

if __name__ == "__main__":
    assert len(sys.argv) == 4
    check = sys.argv[1]
    expected = sys.argv[2]
    expected = expected.replace(",", "")
    text = sys.argv[3]
    text = text.replace(")", "")
    if check == "(1,":
        bash = Bash()
        if expected in bash.app_alias(text):
            print(expected)
    if check == "(2,":
        zsh = Zsh()
        zsh.app_alias(text)
        if expected in zsh.app_alias(text):
            print(expected)
