import sys

if __name__ == "__main__":
    assert len(sys.argv) == 2 or len(sys.argv) == 3
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if len(sys.argv) == 3:
        print(all_values[0])
    else:
        print("Assertion Error - assert data_keras_home == os.path.dirname(K._config_path)")
