import sys
from pandas.core.dtypes.common import is_string_dtype
from pandas.core.dtypes.common import np
import pandas

if __name__ == "__main__":
    assert len(sys.argv) == 7
    expected = sys.argv[1]
    expected = expected[1:]
    expected = expected[:-1]

