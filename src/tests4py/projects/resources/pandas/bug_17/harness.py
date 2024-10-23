import sys
import pytest
from pandas import date_range

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

    value = all_values[0]
    date = all_values[1]
    timezone = all_values[2]
    tz = timezone
    dti = date_range(date, periods=9, freq='-1D', name=9, tz=tz)
    msg = 'incompatible label'
    with pytest.raises(TypeError, match=msg):
        dti.insert(1, int(value))

    if date[0:2] == "17" or "18" or "19" or "20" or "21":
        print(value)
    else:
        print("OutOfBoundsDatetime")
