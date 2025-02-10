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

    if all_values[1] == "None":
        print("ValueError: `steps=None` is only valid for a generator based on the `keras.utils.Sequence` class. Please specify `steps` or use the `keras.utils.Sequence` class.")
    else:
        print(all_values[0])