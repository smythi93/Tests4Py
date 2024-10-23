import unittest
import pytest
from pandas import date_range


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('1249-11-28', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 8186)

    def test_diversity_2(self):
        tz = 'dateutil/US/Pacific'
        dti = date_range('1239-9-1', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 8929)

    def test_diversity_3(self):
        tz = 'Asia/Tokyo'
        dti = date_range('1429-4-1', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 6347)

    def test_diversity_4(self):
        tz = 'Asia/Tokyo'
        dti = date_range('1418-6-13', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 2356)

    def test_diversity_5(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('1537-12-18', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 1855)

    def test_diversity_6(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('1505-4-11', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 4011)

    def test_diversity_7(self):
        tz = 'dateutil/US/Pacific'
        dti = date_range('1527-2-28', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 1427)

    def test_diversity_8(self):
        tz = 'UTC'
        dti = date_range('1495-6-24', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 7237)

    def test_diversity_9(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('1195-6-18', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 7569)

    def test_diversity_10(self):
        tz = 'Asia/Tokyo'
        dti = date_range('1199-3-20', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 2477)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        tz = 'UTC'
        dti = date_range('1727-6-3', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 127)

    def test_diversity_2(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('2067-7-11', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 3775)

    def test_diversity_3(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('1812-1-11', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 163)

    def test_diversity_4(self):
        tz = 'US/Eastern'
        dti = date_range('2196-6-25', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 8318)

    def test_diversity_5(self):
        tz = 'UTC'
        dti = date_range('1939-8-11', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 4328)

    def test_diversity_6(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('1966-9-20', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 6133)

    def test_diversity_7(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('1816-8-10', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 1902)

    def test_diversity_8(self):
        tz = 'US/Eastern'
        dti = date_range('1977-5-26', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 8008)

    def test_diversity_9(self):
        tz = 'Asia/Tokyo'
        dti = date_range('2063-9-11', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 7067)

    def test_diversity_10(self):
        tz = 'dateutil/Asia/Singapore'
        dti = date_range('2099-4-23', periods=9, freq='-1D', name=9, tz=tz)
        msg = 'incompatible label'
        with pytest.raises(TypeError, match=msg):
            dti.insert(1, 7356)
