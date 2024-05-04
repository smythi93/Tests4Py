import sys
from pandas.core.series import Series
from pandas import period_range
from pandas import date_range
from pandas import Timedelta
from pandas._testing import assert_index_equal

if __name__ == "__main__":
    assert len(sys.argv) == 10
    expected = sys.argv[1]
    expected = expected[1:]
    expected = expected[:-1]

    freq_period_range = sys.argv[2]
    freq_period_range = freq_period_range[:-1]

    start_period_range = sys.argv[3]
    start_period_range = start_period_range[:-1]

    end_period_range = sys.argv[4]
    end_period_range = end_period_range[:-1]

    series_name = sys.argv[5]
    series_name = series_name[:-1]

    date_range_start = sys.argv[6]
    date_range_start = date_range_start[:-1]

    date_range_end = sys.argv[7]
    date_range_end = date_range_end[:-1]

    date_range_freq = sys.argv[8]
    date_range_freq = date_range_freq[:-1]

    series_to_timestamp = sys.argv[9]
    series_to_timestamp = series_to_timestamp[:-1]

    index = period_range(freq=freq_period_range, start=start_period_range, end=end_period_range)
    series = Series(1, index=index, name=series_name)
    exp_index = date_range(date_range_start, end=date_range_end, freq=date_range_freq)
    result = series.to_timestamp(how=series_to_timestamp)
    exp_index = exp_index + Timedelta(1, 'ns') - Timedelta(1, 'ns')
    assert_index_equal(result.index, exp_index)
    if result.name == expected:
        print(result.name)
    else:
        print("Assertion Error, Index length are different!")
