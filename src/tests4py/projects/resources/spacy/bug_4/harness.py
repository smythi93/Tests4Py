import sys

if __name__ == "__main__":
    assert len(sys.argv) == 171 or len(sys.argv) == 181
    if len(sys.argv) == 171:
        print(sys.argv[1])
    elif len(sys.argv) == 181:
        print("Value Error")
    else:
        print("len(sys.argv) should be either 171 or 181")
