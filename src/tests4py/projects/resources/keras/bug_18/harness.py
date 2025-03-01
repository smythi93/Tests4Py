import sys

if __name__ == "__main__":
    assert len(sys.argv) == 8
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if all_values[3] == "<ast.Eq":
        print(all_values[0])
    else:
        print("ValueError: (Some keys in session_kwargs are not supported at this time, dict_keys([options, run_metadata]))")
