import sys

if __name__ == "__main__":
    assert len(sys.argv) == 6 or len(sys.argv) == 8
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if len(sys.argv) == 6:
        print(all_values[0])
    else:
        print(AssertionError)
