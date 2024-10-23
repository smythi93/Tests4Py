import sys

if __name__ == "__main__":
    assert len(sys.argv) == 3
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)


    def pipe(doc):
        return doc

    if all_values[1] == "TypeError":
        print(all_values[0])
    else:
        print("TypeError is not raised!")