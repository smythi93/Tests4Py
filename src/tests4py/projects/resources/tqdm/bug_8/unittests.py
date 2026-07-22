import unittest

# noinspection PyUnresolvedReferences
from tqdm import tqdm


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        res = tqdm.format_meter(3915, 4004, 116.53, bar_format='rrvb{bar}fpRW')
        self.assertTrue(res.startswith('rrvb'))
        self.assertTrue(res.endswith('fpRW'))

    def test_diversity_2(self):
        res = tqdm.format_meter(331, 4560, 188.93, bar_format='WXxgbUD{bar}FsPYw')
        self.assertTrue(res.startswith('WXxgbUD'))
        self.assertTrue(res.endswith('FsPYw'))

    def test_diversity_3(self):
        res = tqdm.format_meter(691, 4165, 115.36, bar_format='QsfARgQh{bar}ozNa')
        self.assertTrue(res.startswith('QsfARgQh'))
        self.assertTrue(res.endswith('ozNa'))

    def test_diversity_4(self):
        res = tqdm.format_meter(1842, 2072, 84.2, bar_format='gkheC{bar}aZGTgM')
        self.assertTrue(res.startswith('gkheC'))
        self.assertTrue(res.endswith('aZGTgM'))

    def test_diversity_5(self):
        res = tqdm.format_meter(1003, 4494, 173.85, bar_format='HldDJO{bar}ZKf')
        self.assertTrue(res.startswith('HldDJO'))
        self.assertTrue(res.endswith('ZKf'))

    def test_diversity_6(self):
        res = tqdm.format_meter(2016, 4479, 182.28, bar_format='toNKzKg{bar}LCq')
        self.assertTrue(res.startswith('toNKzKg'))
        self.assertTrue(res.endswith('LCq'))

    def test_diversity_7(self):
        res = tqdm.format_meter(1199, 1421, 105.76, bar_format='mqjoFUfM{bar}TKE')
        self.assertTrue(res.startswith('mqjoFUfM'))
        self.assertTrue(res.endswith('TKE'))

    def test_diversity_8(self):
        res = tqdm.format_meter(426, 2819, 93.93, bar_format='afRSJo{bar}NUFnUe')
        self.assertTrue(res.startswith('afRSJo'))
        self.assertTrue(res.endswith('NUFnUe'))

    def test_diversity_9(self):
        res = tqdm.format_meter(1115, 2950, 72.04, bar_format='vIuin{bar}TSkTbeb')
        self.assertTrue(res.startswith('vIuin'))
        self.assertTrue(res.endswith('TSkTbeb'))

    def test_diversity_10(self):
        res = tqdm.format_meter(929, 1038, 83.14, bar_format='mdiI{bar}esZLrsVl')
        self.assertTrue(res.startswith('mdiI'))
        self.assertTrue(res.endswith('esZLrsVl'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        res = tqdm.format_meter(57, 2069, 179.02, bar_format='bYLTH{n_fmt}RiIp')
        self.assertTrue(res.startswith('bYLTH'))
        self.assertTrue(res.endswith('RiIp'))

    def test_diversity_2(self):
        res = tqdm.format_meter(924, 2306, 130.73, bar_format='Hyh{n_fmt}SIiLbjbG')
        self.assertTrue(res.startswith('Hyh'))
        self.assertTrue(res.endswith('SIiLbjbG'))

    def test_diversity_3(self):
        res = tqdm.format_meter(1102, 1859, 178.0, bar_format='YjTedK{n_fmt}NcA')
        self.assertTrue(res.startswith('YjTedK'))
        self.assertTrue(res.endswith('NcA'))

    def test_diversity_4(self):
        res = tqdm.format_meter(21, 116, 123.27, bar_format='gSWMSIst{n_fmt}ovULbqU')
        self.assertTrue(res.startswith('gSWMSIst'))
        self.assertTrue(res.endswith('ovULbqU'))

    def test_diversity_5(self):
        res = tqdm.format_meter(1702, 4614, 3.09, bar_format='vYyPK{n_fmt}fmAgeSg')
        self.assertTrue(res.startswith('vYyPK'))
        self.assertTrue(res.endswith('fmAgeSg'))

    def test_diversity_6(self):
        res = tqdm.format_meter(1210, 4532, 172.16, bar_format='mGCn{n_fmt}DgoiZG')
        self.assertTrue(res.startswith('mGCn'))
        self.assertTrue(res.endswith('DgoiZG'))

    def test_diversity_7(self):
        res = tqdm.format_meter(609, 3261, 177.52, bar_format='YbsoD{n_fmt}MyUWh')
        self.assertTrue(res.startswith('YbsoD'))
        self.assertTrue(res.endswith('MyUWh'))

    def test_diversity_8(self):
        res = tqdm.format_meter(832, 1801, 10.1, bar_format='Xcg{n_fmt}inAW')
        self.assertTrue(res.startswith('Xcg'))
        self.assertTrue(res.endswith('inAW'))

    def test_diversity_9(self):
        res = tqdm.format_meter(241, 1670, 188.01, bar_format='lMqJdU{n_fmt}CvBSI')
        self.assertTrue(res.startswith('lMqJdU'))
        self.assertTrue(res.endswith('CvBSI'))

    def test_diversity_10(self):
        res = tqdm.format_meter(270, 1214, 13.59, bar_format='DYfcGgU{n_fmt}EGWYLQSE')
        self.assertTrue(res.startswith('DYfcGgU'))
        self.assertTrue(res.endswith('EGWYLQSE'))

