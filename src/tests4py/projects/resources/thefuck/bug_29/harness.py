import sys
from thefuck.types import Settings


if __name__ == "__main__":
    assert len(sys.argv) == 2 or len(sys.argv) == 3
    expected = " ".join(sys.argv[1:])
    expected = expected.replace("{", "")
    expected = expected.replace("}", "")
    split1, split2 = expected.split(":")
    result = {split1: split2}
    settings = Settings(result)
    new_settings = settings.update()
    if result == new_settings:
        print(result)
    else:
        print("Result and Output does not match")
