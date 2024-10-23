import sys
import numpy
from pandas import Series
from pandas._testing import assert_series_equal

if __name__ == "__main__":
    assert len(sys.argv) == 10
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        i = float(i)
        all_values.append(i)

    s = Series([all_values[0], numpy.nan, all_values[1], all_values[3], numpy.nan])
    s2 = Series([numpy.nan, all_values[2], numpy.nan, all_values[4]])
    s.update(s2)
    expected = Series([all_values[5], all_values[8], all_values[1], all_values[4], numpy.nan])
    if assert_series_equal(s, expected) is None:
        print(all_values[0])
    else:
        print("Assertion Error: Series are different")
