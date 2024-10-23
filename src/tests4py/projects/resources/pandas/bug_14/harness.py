import sys
import pandas
from pandas._testing import assert_index_equal
from datetime import timedelta

if __name__ == "__main__":
    assert len(sys.argv) == 4
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)
    index = pandas.date_range('1/1/2000', periods=int(all_values[1]), freq=all_values[2])
    shifted = index + timedelta(1)
    back = shifted + timedelta(-1)
    back = back._with_freq('infer')
    if assert_index_equal(index, back) is None:
        print(all_values[0])
    else:
        print("Value Error")
