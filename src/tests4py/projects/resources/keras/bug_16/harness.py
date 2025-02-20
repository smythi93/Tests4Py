import sys

if __name__ == "__main__":
    assert len(sys.argv) == 3 or len(sys.argv) == 4
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if len(all_values) == 3:
        print(all_values[0])
    else:
        raise AssertionError
