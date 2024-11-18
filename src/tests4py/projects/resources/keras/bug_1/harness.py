import sys

if __name__ == "__main__":
    assert len(sys.argv) == 7
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if all_values[2] == "<ast.Eq":
        print(all_values[0])
    else:
        print("Assertion Error")
