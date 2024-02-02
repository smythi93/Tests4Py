import sys
from thefuck.types import Command
from thefuck.rules.sudo import match

if __name__ == "__main__":
    assert len(sys.argv) == 5
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected.replace(",", "")
    script = sys.argv[2]
    script = script.replace(",", "")
    std_err = sys.argv[3]
    std_err = std_err.replace(std_err[(len(std_err)-1)], "")
    std_err = std_err.replace("EACCES", "EACCES,")
    std_out = sys.argv[4]
    std_out = std_out.replace(")", "")
    if expected == "True":
        expected = True
    elif expected == "False":
        expected = False
    else:
        print("Expected should be True or False")
    if expected == match(Command(script, std_err, std_out)):
        print(match(Command(script, std_err, std_out)))
    else:
        print("Check the parameters for match(Command()) function!")
