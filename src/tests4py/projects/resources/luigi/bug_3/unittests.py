import unittest
from luigi import TupleParameter



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((95, 202, 471, 939, 169))), (95, 202, 471, 939, 169))

    def test_diversity_2(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((916,))), (916,))

    def test_diversity_3(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((468, 49, 710))), (468, 49, 710))

    def test_diversity_4(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((322, 522, 10))), (322, 522, 10))

    def test_diversity_5(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((224, 566))), (224, 566))

    def test_diversity_6(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((577, 930))), (577, 930))

    def test_diversity_7(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((79, 362))), (79, 362))

    def test_diversity_8(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((462, 462, 776, 153, 718, 713))), (462, 462, 776, 153, 718, 713))

    def test_diversity_9(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((339, 202, 823, 402, 758, 433))), (339, 202, 823, 402, 758, 433))

    def test_diversity_10(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize((917, 360, 687, 375, 311))), (917, 360, 687, 375, 311))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((312, 785), (640, 702)))), ((312, 785), (640, 702)))

    def test_diversity_2(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((981, 230), (894, 680), (131, 695)))), ((981, 230), (894, 680), (131, 695)))

    def test_diversity_3(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((315, 568), (486, 678), (823, 291), (798, 621)))), ((315, 568), (486, 678), (823, 291), (798, 621)))

    def test_diversity_4(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((569, 363),))), ((569, 363),))

    def test_diversity_5(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((781, 94), (431, 109), (917, 831)))), ((781, 94), (431, 109), (917, 831)))

    def test_diversity_6(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((31, 851), (75, 626), (778, 709), (54, 253)))), ((31, 851), (75, 626), (778, 709), (54, 253)))

    def test_diversity_7(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((331, 125), (864, 860), (865, 711), (696, 426)))), ((331, 125), (864, 860), (865, 711), (696, 426)))

    def test_diversity_8(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((85, 81),))), ((85, 81),))

    def test_diversity_9(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((458, 947),))), ((458, 947),))

    def test_diversity_10(self):
        tp = TupleParameter()
        self.assertEqual(tp.parse(tp.serialize(((445, 918), (523, 324)))), ((445, 918), (523, 324)))
