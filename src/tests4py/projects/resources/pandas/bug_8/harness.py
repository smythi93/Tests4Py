import sys
import pandas
import numpy
from pandas._testing import assert_frame_equal

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

    df = pandas.DataFrame(numpy.eye(int(all_values[1])), dtype=all_values[2])
    result = df.replace(to_replace=[None, -numpy.inf, numpy.inf], value=numpy.nan)
    if assert_frame_equal(result, df) is None:
        print(all_values[0])
    else:
        print(f"Should be {all_values[0]}, but it is not")
