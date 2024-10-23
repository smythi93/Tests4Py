import unittest
import pandas
from pandas import Series, DataFrame, MultiIndex, concat
from pandas._testing import assert_frame_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        keys = ['f', 'e', 'f']
        df = DataFrame({'a': [6025, 6026, 6027], 'b': [6028, 6029, 6030]})
        s1 = Series([6031, 6032, 6033], name='c')
        s2 = Series([6034, 6035, 6036], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[6025, 6028, 6031, 6034], [6026, 6029, 6032, 6035], [6027, 6030, 6033, 6036]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_2(self):
        keys = ['e', 'f', 'f']
        df = DataFrame({'a': [8585, 8586, 8587], 'b': [8588, 8589, 8590]})
        s1 = Series([8591, 8592, 8593], name='c')
        s2 = Series([8594, 8595, 8596], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[8585, 8588, 8591, 8594], [8586, 8589, 8592, 8595], [8587, 8590, 8593, 8596]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_3(self):
        keys = ['f', 'e', 'f']
        df = DataFrame({'a': [9916, 9917, 9918], 'b': [9919, 9920, 9921]})
        s1 = Series([9922, 9923, 9924], name='c')
        s2 = Series([9925, 9926, 9927], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[9916, 9919, 9922, 9925], [9917, 9920, 9923, 9926], [9918, 9921, 9924, 9927]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_4(self):
        keys = ['e', 'f', 'f']
        df = DataFrame({'a': [1172, 1173, 1174], 'b': [1175, 1176, 1177]})
        s1 = Series([1178, 1179, 1180], name='c')
        s2 = Series([1181, 1182, 1183], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[1172, 1175, 1178, 1181], [1173, 1176, 1179, 1182], [1174, 1177, 1180, 1183]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_5(self):
        keys = ['e', 'f', 'f']
        df = DataFrame({'a': [2328, 2329, 2330], 'b': [2331, 2332, 2333]})
        s1 = Series([2334, 2335, 2336], name='c')
        s2 = Series([2337, 2338, 2339], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[2328, 2331, 2334, 2337], [2329, 2332, 2335, 2338], [2330, 2333, 2336, 2339]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_6(self):
        keys = ['e', 'f', 'f']
        df = DataFrame({'a': [6604, 6605, 6606], 'b': [6607, 6608, 6609]})
        s1 = Series([6610, 6611, 6612], name='c')
        s2 = Series([6613, 6614, 6615], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[6604, 6607, 6610, 6613], [6605, 6608, 6611, 6614], [6606, 6609, 6612, 6615]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_7(self):
        keys = ['e', 'f', 'f']
        df = DataFrame({'a': [1777, 1778, 1779], 'b': [1780, 1781, 1782]})
        s1 = Series([1783, 1784, 1785], name='c')
        s2 = Series([1786, 1787, 1788], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[1777, 1780, 1783, 1786], [1778, 1781, 1784, 1787], [1779, 1782, 1785, 1788]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_8(self):
        keys = ['e', 'f', 'f']
        df = DataFrame({'a': [2053, 2054, 2055], 'b': [2056, 2057, 2058]})
        s1 = Series([2059, 2060, 2061], name='c')
        s2 = Series([2062, 2063, 2064], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[2053, 2056, 2059, 2062], [2054, 2057, 2060, 2063], [2055, 2058, 2061, 2064]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_9(self):
        keys = ['f', 'e', 'f']
        df = DataFrame({'a': [7096, 7097, 7098], 'b': [7099, 7100, 7101]})
        s1 = Series([7102, 7103, 7104], name='c')
        s2 = Series([7105, 7106, 7107], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[7096, 7099, 7102, 7105], [7097, 7100, 7103, 7106], [7098, 7101, 7104, 7107]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_10(self):
        keys = ['f', 'e', 'f']
        df = DataFrame({'a': [2875, 2876, 2877], 'b': [2878, 2879, 2880]})
        s1 = Series([2881, 2882, 2883], name='c')
        s2 = Series([2884, 2885, 2886], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[2875, 2878, 2881, 2884], [2876, 2879, 2882, 2885], [2877, 2880, 2883, 2886]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [9292, 9293, 9294], 'b': [9295, 9296, 9297]})
        s1 = Series([9298, 9299, 9300], name='c')
        s2 = Series([9301, 9302, 9303], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[9292, 9295, 9298, 9301], [9293, 9296, 9299, 9302], [9294, 9297, 9300, 9303]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_2(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [4472, 4473, 4474], 'b': [4475, 4476, 4477]})
        s1 = Series([4478, 4479, 4480], name='c')
        s2 = Series([4481, 4482, 4483], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[4472, 4475, 4478, 4481], [4473, 4476, 4479, 4482], [4474, 4477, 4480, 4483]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_3(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [9316, 9317, 9318], 'b': [9319, 9320, 9321]})
        s1 = Series([9322, 9323, 9324], name='c')
        s2 = Series([9325, 9326, 9327], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[9316, 9319, 9322, 9325], [9317, 9320, 9323, 9326], [9318, 9321, 9324, 9327]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_4(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [86, 87, 88], 'b': [89, 90, 91]})
        s1 = Series([92, 93, 94], name='c')
        s2 = Series([95, 96, 97], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[86, 89, 92, 95], [87, 90, 93, 96], [88, 91, 94, 97]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_5(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [6532, 6533, 6534], 'b': [6535, 6536, 6537]})
        s1 = Series([6538, 6539, 6540], name='c')
        s2 = Series([6541, 6542, 6543], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[6532, 6535, 6538, 6541], [6533, 6536, 6539, 6542], [6534, 6537, 6540, 6543]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_6(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [7139, 7140, 7141], 'b': [7142, 7143, 7144]})
        s1 = Series([7145, 7146, 7147], name='c')
        s2 = Series([7148, 7149, 7150], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[7139, 7142, 7145, 7148], [7140, 7143, 7146, 7149], [7141, 7144, 7147, 7150]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_7(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [2662, 2663, 2664], 'b': [2665, 2666, 2667]})
        s1 = Series([2668, 2669, 2670], name='c')
        s2 = Series([2671, 2672, 2673], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[2662, 2665, 2668, 2671], [2663, 2666, 2669, 2672], [2664, 2667, 2670, 2673]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_8(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [8095, 8096, 8097], 'b': [8098, 8099, 8100]})
        s1 = Series([8101, 8102, 8103], name='c')
        s2 = Series([8104, 8105, 8106], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[8095, 8098, 8101, 8104], [8096, 8099, 8102, 8105], [8097, 8100, 8103, 8106]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_9(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [5103, 5104, 5105], 'b': [5106, 5107, 5108]})
        s1 = Series([5109, 5110, 5111], name='c')
        s2 = Series([5112, 5113, 5114], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[5103, 5106, 5109, 5112], [5104, 5107, 5110, 5113], [5105, 5108, 5111, 5114]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))

    def test_diversity_10(self):
        keys = ['f', 'e', 'g']
        df = DataFrame({'a': [8485, 8486, 8487], 'b': [8488, 8489, 8490]})
        s1 = Series([8491, 8492, 8493], name='c')
        s2 = Series([8494, 8495, 8496], name='d')
        result = concat([df, s1, s2], axis=1, keys=keys)
        expected_values = [[8485, 8488, 8491, 8494], [8486, 8489, 8492, 8495], [8487, 8490, 8493, 8496]]
        expected_columns = pandas.MultiIndex.from_tuples(
            [(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
        expected = DataFrame(expected_values, columns=expected_columns)
        self.assertEqual(None, assert_frame_equal(result, expected))
