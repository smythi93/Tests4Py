import sys
from pandas import pandas, CategoricalIndex
import numpy

if __name__ == "__main__":
    assert len(sys.argv) == 2
    dti = pandas.date_range(sys.argv[1], periods=100).insert(0, pandas.NaT)
    ci = CategoricalIndex(dti)
    if pandas.NaT in ci and numpy.nan in ci and None in ci:
        print(sys.argv[1])
    else:
        print("Requirements are not met!")
