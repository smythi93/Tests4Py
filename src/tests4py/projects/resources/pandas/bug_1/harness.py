import sys
from pandas.core.dtypes.common import is_string_dtype
from pandas.core.dtypes.dtypes import PeriodDtype

if __name__ == "__main__":
    assert len(sys.argv) == 3
    expected = sys.argv[1]
    expected = expected[1:]
    expected = expected[:-1]
    value = sys.argv[2]
    value = value[:-1]
    if not is_string_dtype(PeriodDtype(value)):
        print(expected)
    else:
        print("Value Error")
