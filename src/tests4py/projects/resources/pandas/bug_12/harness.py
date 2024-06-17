import sys
import pandas
import numpy
from pandas._testing import assert_frame_equal

if __name__ == "__main__":
    assert len(sys.argv) == 5
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    other_column = numpy.array([float(all_values[1]), float(all_values[2]), float(all_values[3])])
    data = pandas.DataFrame({'a': pandas.array([1.0, 2.0, numpy.nan]), 'b': other_column})
    result = data.cov()
    arr = numpy.array([[0.5, 0.5], [0.5, 1.0]])
    expected = pandas.DataFrame(arr, columns=['a', 'b'], index=['a', 'b'])
    if assert_frame_equal(result, expected) is None:
        print(all_values[0])
    else:
        print("Assertion Error")
