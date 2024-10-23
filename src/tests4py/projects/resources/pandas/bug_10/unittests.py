import unittest
import numpy
from pandas import Series
from pandas._testing import assert_series_equal


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        s = Series([1.4494568429267103, numpy.nan, 2.8515210392768875, 3.313283056973802, numpy.nan])
        s2 = Series([numpy.nan, 2.96615050661751, numpy.nan, 3.975492720564157])
        s.update(s2)
        expected = Series([1.4494568429267103, 2.96615050661751, 2.8515210392768875, 3.313283056973802, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_2(self):
        s = Series([0.792776790106131, numpy.nan, 0.9389951798629144, 3.210711778227913, numpy.nan])
        s2 = Series([numpy.nan, 1.6636332385322536, numpy.nan, 3.948487498542519])
        s.update(s2)
        expected = Series([0.792776790106131, 1.6636332385322536, 0.9389951798629144, 3.210711778227913, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_3(self):
        s = Series([0.08665193389171921, numpy.nan, 1.488890567618414, 2.1110514198608556, numpy.nan])
        s2 = Series([numpy.nan, 1.637423065298898, numpy.nan, 3.5406347695757403])
        s.update(s2)
        expected = Series([0.08665193389171921, 1.637423065298898, 1.488890567618414, 2.1110514198608556, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_4(self):
        s = Series([2.347951493413241, numpy.nan, 2.36322271978705, 2.600676932757657, numpy.nan])
        s2 = Series([numpy.nan, 2.5454471092893525, numpy.nan, 3.360724858578532])
        s.update(s2)
        expected = Series([2.347951493413241, 2.5454471092893525, 2.36322271978705, 2.600676932757657, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_5(self):
        s = Series([0.16263525994297845, numpy.nan, 0.5727668585593787, 2.1833384038068933, numpy.nan])
        s2 = Series([numpy.nan, 2.1274376689589145, numpy.nan, 3.2187939816808986])
        s.update(s2)
        expected = Series([0.16263525994297845, 2.1274376689589145, 0.5727668585593787, 2.1833384038068933, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_6(self):
        s = Series([0.21897454883359357, numpy.nan, 0.4678159057040777, 3.5922616883258307, numpy.nan])
        s2 = Series([numpy.nan, 0.7009315961559537, numpy.nan, 3.7303688778164372])
        s.update(s2)
        expected = Series([0.21897454883359357, 0.7009315961559537, 0.4678159057040777, 3.5922616883258307, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_7(self):
        s = Series([0.7974300163941929, numpy.nan, 1.1800408749501485, 3.151583586010025, numpy.nan])
        s2 = Series([numpy.nan, 1.5619425048589166, numpy.nan, 3.9451276898988827])
        s.update(s2)
        expected = Series([0.7974300163941929, 1.5619425048589166, 1.1800408749501485, 3.151583586010025, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_8(self):
        s = Series([1.2449967159621884, numpy.nan, 1.7774439913327338, 2.8676757208929406, numpy.nan])
        s2 = Series([numpy.nan, 2.7667326265329772, numpy.nan, 3.580359780944868])
        s.update(s2)
        expected = Series([1.2449967159621884, 2.7667326265329772, 1.7774439913327338, 2.8676757208929406, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_9(self):
        s = Series([0.023554857581998156, numpy.nan, 0.16354991093179694, 1.2815200589443705, numpy.nan])
        s2 = Series([numpy.nan, 0.5645342923737545, numpy.nan, 2.9397962728124902])
        s.update(s2)
        expected = Series(
            [0.023554857581998156, 0.5645342923737545, 0.16354991093179694, 1.2815200589443705, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_10(self):
        s = Series([0.30916895068590644, numpy.nan, 0.618961555456303, 2.6330544616865654, numpy.nan])
        s2 = Series([numpy.nan, 2.270659480371137, numpy.nan, 3.2277373080036527])
        s.update(s2)
        expected = Series([0.30916895068590644, 2.270659480371137, 0.618961555456303, 2.6330544616865654, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        s = Series([1.1677800196270653, numpy.nan, 1.3590461087448784, 3.279576756962372, numpy.nan])
        s2 = Series([numpy.nan, 1.5219830930016882, numpy.nan, 3.566134998510898])
        s.update(s2)
        expected = Series([1.1677800196270653, 1.5219830930016882, 1.3590461087448784, 3.566134998510898, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_2(self):
        s = Series([0.11942884082186145, numpy.nan, 1.6164992706283172, 2.486415404617073, numpy.nan])
        s2 = Series([numpy.nan, 2.4112865344870036, numpy.nan, 2.49431363235132])
        s.update(s2)
        expected = Series([0.11942884082186145, 2.4112865344870036, 1.6164992706283172, 2.49431363235132, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_3(self):
        s = Series([1.1086247770088662, numpy.nan, 1.8193492738962385, 2.491170719511675, numpy.nan])
        s2 = Series([numpy.nan, 2.248538597600245, numpy.nan, 3.6308465587095524])
        s.update(s2)
        expected = Series([1.1086247770088662, 2.248538597600245, 1.8193492738962385, 3.6308465587095524, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_4(self):
        s = Series([1.2129405865235428, numpy.nan, 1.645827927436465, 3.174562220468299, numpy.nan])
        s2 = Series([numpy.nan, 2.712662742048359, numpy.nan, 3.4241903934134315])
        s.update(s2)
        expected = Series([1.2129405865235428, 2.712662742048359, 1.645827927436465, 3.4241903934134315, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_5(self):
        s = Series([1.4361019136329847, numpy.nan, 1.7395342236144185, 3.157732771586031, numpy.nan])
        s2 = Series([numpy.nan, 2.3378711020040126, numpy.nan, 3.2792001192914477])
        s.update(s2)
        expected = Series([1.4361019136329847, 2.3378711020040126, 1.7395342236144185, 3.2792001192914477, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_6(self):
        s = Series([0.3948478926701141, numpy.nan, 1.6623023538236614, 3.549665363213409, numpy.nan])
        s2 = Series([numpy.nan, 2.275160314009457, numpy.nan, 3.550286958022591])
        s.update(s2)
        expected = Series([0.3948478926701141, 2.275160314009457, 1.6623023538236614, 3.550286958022591, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_7(self):
        s = Series([0.41739051493802315, numpy.nan, 1.6198953900702777, 3.115789747694797, numpy.nan])
        s2 = Series([numpy.nan, 2.545955731083464, numpy.nan, 3.2130843218321656])
        s.update(s2)
        expected = Series([0.41739051493802315, 2.545955731083464, 1.6198953900702777, 3.2130843218321656, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_8(self):
        s = Series([0.32222277533715205, numpy.nan, 1.0664663133116905, 2.2199730034961145, numpy.nan])
        s2 = Series([numpy.nan, 2.0899963561856345, numpy.nan, 2.272136271552655])
        s.update(s2)
        expected = Series([0.32222277533715205, 2.0899963561856345, 1.0664663133116905, 2.272136271552655, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_9(self):
        s = Series([1.6399183946901092, numpy.nan, 1.8519881750779466, 2.8026563877641952, numpy.nan])
        s2 = Series([numpy.nan, 2.4540671330460992, numpy.nan, 3.2591442814177993])
        s.update(s2)
        expected = Series([1.6399183946901092, 2.4540671330460992, 1.8519881750779466, 3.2591442814177993, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))

    def test_diversity_10(self):
        s = Series([0.3318957615755025, numpy.nan, 1.084416898973062, 3.4183044861312037, numpy.nan])
        s2 = Series([numpy.nan, 1.7609921895559326, numpy.nan, 3.6723509547241275])
        s.update(s2)
        expected = Series([0.3318957615755025, 1.7609921895559326, 1.084416898973062, 3.6723509547241275, numpy.nan])
        self.assertIsNone(assert_series_equal(s, expected))
