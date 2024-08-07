import sys

if __name__ == "__main__":
    assert len(sys.argv) == 5
    error_match = sys.argv[4]
    value = sys.argv[1]
    value = value.replace("(", "")
    value = value.replace(",", "")
    error_match = error_match.replace(")", "")
    if error_match == "not in index":
        print("Assertion Error")
    else:
        print(value)
