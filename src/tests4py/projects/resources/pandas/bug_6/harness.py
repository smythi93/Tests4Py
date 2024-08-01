import sys
from pandas import PeriodIndex, Series
from pandas._testing import assert_series_equal

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

    ser = Series([1], index=PeriodIndex([all_values[1]], name='A', freq='D'))
    grp = ser.groupby(level='A')
    result = grp.size()
    if assert_series_equal(result, ser) is None:
        print(all_values[0])
    else:
        print("Value Error")

