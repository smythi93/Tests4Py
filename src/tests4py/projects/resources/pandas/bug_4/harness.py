import sys
from pandas import pandas, Index, MultiIndex
import numpy
from pandas._testing import assert_index_equal, assert_numpy_array_equal

if __name__ == "__main__":
    assert len(sys.argv) == 21
    list_values = []
    for i in sys.argv[2:]:
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        i = i.replace(",", "")
        i = int(i)
        list_values.append(i)

    midx = pandas.MultiIndex.from_product([numpy.arange(4), numpy.arange(4)], names=['a', 'b'])
    idx = pandas.Index(list_values[0:3], name='b')
    jidx, lidx, ridx = midx.join(idx, how='inner', return_indexers=True)
    exp_idx = pandas.MultiIndex.from_product([numpy.arange(4), [1, 2]], names=['a', 'b'])
    exp_lidx = numpy.array(list_values[3:11], dtype=numpy.intp)
    exp_ridx = numpy.array(list_values[11:19], dtype=numpy.intp)
    assert_index_equal(jidx, exp_idx)
    if assert_numpy_array_equal(lidx, exp_lidx) is None:
        print("None")
    else:
        print("AssertionError: numpy array are different")
