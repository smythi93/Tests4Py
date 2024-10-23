import random
import sys
import pandas
import numpy
from pandas import Categorical, Series, DataFrame
from pandas._testing import assert_numpy_array_equal, assert_series_equal

if __name__ == "__main__":
    assert len(sys.argv) == 10
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        if i == "True":
            i = True
        if i == "False":
            i = False
        all_values.append(i)

    dice = random.randint(0, 3)
    if dice == 0:
        cat = Categorical([int(all_values[1]), int(all_values[2]), numpy.inf])
        result = cat.isna()
        expected = numpy.array([all_values[3], all_values[4], all_values[5]])
        if assert_numpy_array_equal(result, expected) is None:
            print(all_values[0])
    elif dice == 1:
        cat = Categorical([int(all_values[1]), int(all_values[2]), numpy.inf])
        result = Series(cat).isna()
        expected = Series(numpy.array([all_values[3], all_values[4], all_values[5]]))
        if assert_series_equal(result, expected) is None:
            print(all_values[0])
    elif dice == 2:
        cat = Categorical([int(all_values[1]), int(all_values[2]), pandas.NA])
        result = cat.isna()
        expected = numpy.array([all_values[6], all_values[7], all_values[8]])
        if assert_numpy_array_equal(result, expected) is None:
            print(all_values[0])
    elif dice == 3:
        cat = Categorical([int(all_values[1]), int(all_values[2]), numpy.nan])
        result = Series(cat).isna()
        expected = Series(numpy.array([all_values[6], all_values[7], all_values[8]]))
        if assert_series_equal(result, expected) is None:
            print(all_values[0])
    else:
        print("There is an unknown input or Assertion Error")
