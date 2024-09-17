import sys
from spacy.errors import Errors

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

    if hasattr(Errors, all_values[0]):
        print(getattr(Errors, all_values[0]))
    else:
        print(f"Error: {all_values[0]} not found in Errors class.")