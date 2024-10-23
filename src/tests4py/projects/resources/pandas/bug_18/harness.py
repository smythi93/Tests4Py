import random
import sys
import numpy
from pandas.api.indexers import FixedForwardWindowIndexer
from pandas import DataFrame, Series
from pandas._testing import assert_equal

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

    constructor = random.choice([Series, DataFrame])
    values = numpy.arange(10)
    values[5] = 100.0
    indexer = FixedForwardWindowIndexer(window_size=5)
    rolling = constructor(values).rolling(window=indexer, min_periods=3)
    result = rolling.apply(lambda x: x.skew())
    expected = constructor([0.0, float(all_values[1]), float(all_values[2]), float(all_values[3]),
                            float(all_values[4]), float(all_values[5]), 0.0, 0.0, numpy.nan, numpy.nan])
    if assert_equal(result, expected) is None:
        print(all_values[0])
    else:
        print("AssertionError: values are different")

