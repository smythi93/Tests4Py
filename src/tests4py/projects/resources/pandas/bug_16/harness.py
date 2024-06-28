import sys
import pandas
from pandas._testing import assert_index_equal
from pandas import PeriodIndex

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

    idx = PeriodIndex([all_values[1], all_values[2], all_values[3], all_values[4]], freq='M', name='idx')
    result = idx - pandas.Period(all_values[5], freq='M')
    off = idx.freq
    exp = pandas.Index([-12 * off, -11 * off, -10 * off, -9 * off], name='idx')
    if assert_index_equal(result, exp) is None:
        print(all_values[0])
    else:
        print("AssertionError: Index are different")

