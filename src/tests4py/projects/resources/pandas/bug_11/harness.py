import sys
import pandas
from pandas import Series, DataFrame, MultiIndex, concat
from pandas._testing import assert_frame_equal

if __name__ == "__main__":
    assert len(sys.argv) == 31
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace("{", "")
        i = i.replace("}", "")
        i = i.replace(",", "")
        all_values.append(i)
    keys = [all_values[1], all_values[2], all_values[3]]
    df = DataFrame({'a': [all_values[5], all_values[6], all_values[7]], 'b': [all_values[9], all_values[10], all_values[11]]})
    s1 = Series([all_values[12], all_values[13], all_values[14]], name='c')
    s2 = Series([all_values[15], all_values[16], all_values[17]], name='d')
    result = concat([df, s1, s2], axis=1, keys=keys)
    expected_values = [[all_values[18], all_values[19], all_values[20], all_values[21]], [all_values[22], all_values[23], all_values[24], all_values[25]], [all_values[26], all_values[27], all_values[28], all_values[29]]]
    expected_columns = pandas.MultiIndex.from_tuples([(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
    expected = DataFrame(expected_values, columns=expected_columns)
    if assert_frame_equal(result, expected) is None:
        print(all_values[0])
    else:
        print("Type Error")
