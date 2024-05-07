import sys
from pandas import DataFrame


if __name__ == "__main__":
    assert len(sys.argv) == 9 or len(sys.argv) == 12

    expected = sys.argv[1]
    expected = expected[1:]
    expected = expected[:-1]

    dict_key = sys.argv[2]
    dict_key = dict_key[1:]
    dict_key = dict_key[:-1]

    dict_value1 = sys.argv[3]
    dict_value1 = dict_value1[1:]
    dict_value1 = dict_value1[:-1]

    dict_value2 = sys.argv[4]
    dict_value2 = dict_value2[:-3]

    tuple_value1 = sys.argv[5]
    tuple_value1 = tuple_value1[2:]
    tuple_value1 = tuple_value1[:-1]

    tuple_value2 = sys.argv[6]
    tuple_value2 = tuple_value2[:-2]

    tuple_value3 = sys.argv[7]
    tuple_value3 = tuple_value3[1:]
    tuple_value3 = tuple_value3[:-1]

    tuple_value4 = sys.argv[8]
    tuple_value4 = tuple_value4[:-3]

    if len(sys.argv) == 9:
        df = DataFrame({dict_key: [dict_value1, dict_value2]}, index=[(tuple_value1, tuple_value2), (tuple_value3, tuple_value4)])
        if expected == str(df.index.nlevels):
            print(expected)
    elif len(sys.argv) == 12:
        df = DataFrame({dict_key: [dict_value1, dict_value2]}, index=[(tuple_value1, tuple_value2), (tuple_value3, tuple_value4)])
        if expected == str(df.at[(tuple_value1, tuple_value2), dict_key]):
            print(expected)
    else:
        print("sys.argv length should be 9 or 12")
