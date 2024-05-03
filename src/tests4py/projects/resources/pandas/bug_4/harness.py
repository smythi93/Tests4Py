import sys
from pandas.core.dtypes.common import is_string_dtype
from pandas.core.dtypes.common import np
import pandas

if __name__ == "__main__":
    assert len(sys.argv) == 7
    expected = sys.argv[1]
    expected = expected[1:]
    expected = expected[:-1]
    # int or string
    case1 = sys.argv[2]
    case1 = case1[:-1]
    # array -> [1, 2]
    case2 = "".join(sys.argv[3:5])
    case2 = case2[:-1]
    # array -> ['a', 'b']
    case3 = "".join(sys.argv[5:7])
    case3 = case3[:-1]
    if is_string_dtype(case1) and is_string_dtype(pandas.Series(case2)) and is_string_dtype(np.array(case3)):
        print("True")
    else:
        print("False")
