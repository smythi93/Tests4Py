import sys
from thefuck.types import Command
from thefuck.rules.man import get_new_command

if __name__ == "__main__":
    assert len(sys.argv) >= 5
    if len(sys.argv) == 5:
        expected = sys.argv[1]
        expected = expected.replace(expected[len(expected) - 1], "")
        expected = expected.replace(expected[0], "")
        script = sys.argv[2]
        script = script.replace(script[len(script) - 1], "")
        std_out = sys.argv[3]
        std_out = std_out.replace(std_out[len(std_out) - 1], "")
        std_err = sys.argv[4]

        print(get_new_command(Command(script, std_out, std_err)))

    else:
        expected = " ".join(sys.argv[1:4])
        expected = expected.replace("([", "[")
        expected = expected.replace("],", "]")
        script = sys.argv[4]
        script = script.replace(script[len(script) - 1], "")

        std_out = sys.argv[5]
        std_out = std_out.replace(std_out[len(std_out) - 1], "")

        std_err = sys.argv[6]
        if "\\n" in std_err:
            std_err = std_err.replace("\\n)", "\n")
        else:
            std_err = std_err.replace(")", "")

        print(get_new_command(Command(script, std_out, std_err)))


